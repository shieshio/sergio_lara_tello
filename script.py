#!/usr/bin/env python3

import os

# Constantes
NOMBRE_COMPLETO = "sergio_lara" 
EXTENSION_OBJETIVO = ".log"

def filtrar_y_renombrar_logs():
    
    # Para obtener una lista de archivos en el directorio actual
    archivos = os.listdir(".")
    
    # Aquí se filtran solo archivos que terminen en .log
    archivos_log = []
    for archivo in archivos:
        if archivo.endswith(EXTENSION_OBJETIVO):
            archivos_log.append(archivo)
    
    # Se verifica si existen archivos para procesar
    if len(archivos_log) == 0:
        print("No se encontraron archivos .log en el directorio actual.")
        return
    
    # Se ordenan los archivos alfabéticamente para mantener consistencia
    archivos_log.sort()
    
    print(f"Se encontraron {len(archivos_log)} archivo(s) .log")
    print("-" * 50)
    
    # Se renombra con una numeración incremental
    contador = 1
    for archivo_original in archivos_log:
        # Para evitar renombrar archivos ya procesados por el script
        if archivo_original.startswith(NOMBRE_COMPLETO + "_"):
            continue
        
        # Se genera el nuevo nombre con formato del ejercicio
        nuevo_nombre = f"{NOMBRE_COMPLETO}_{contador}{EXTENSION_OBJETIVO}"
        
        try:
            # Se ejecuta el renombrado
            os.rename(archivo_original, nuevo_nombre)
            print(f"[{contador}] {archivo_original} → {nuevo_nombre}")
            contador += 1
        except Exception as error:
            print(f"[ERROR] No se pudo renombrar '{archivo_original}': {error}")
    
    print("-" * 50)
    print(f"Proceso completado. Se renombraron {contador - 1} archivo(s).")

# Ejecución principal
if __name__ == "__main__":
    print("=" * 50)
    print("SCRIPT DE RENOMBRADO DE ARCHIVOS .LOG")
    print("=" * 50)
    print()
    filtrar_y_renombrar_logs()