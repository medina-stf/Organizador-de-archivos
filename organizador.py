import os
import shutil

#Diccionario de tipos de archivo por categoría
tipos = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "PDF": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documentos": [".docx", ".doc", ".txt", ".xlsx", ".pptx"]
}

#Diccionario para contar archivos movidos por categoría
resumen = {}

def organizar_archivos(ruta):
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()
            movido = False

            for categoria, extensiones in tipos.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(ruta, categoria)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
                    resumen[categoria] = resumen.get(categoria, 0) + 1
                    movido = True
                    break

            if not movido:
                carpeta_otros = os.path.join(ruta, "Otros")
                os.makedirs(carpeta_otros, exist_ok=True)
                shutil.move(ruta_completa, os.path.join(carpeta_otros, archivo))
                resumen["Otros"] = resumen.get("Otros", 0) + 1

#Solicita al usuario la carpeta
carpeta_objetivo = input("Escribe la ruta de la carpeta que quieres organizar: ").strip()

#Verifica que exista
if not os.path.isdir(carpeta_objetivo):
    print("La ruta no es válida o no existe.")
else:
    organizar_archivos(carpeta_objetivo)

    # Mostrar resumen
    print("\nOrganización completada.\nResumen de archivos movidos:")
    for categoria, cantidad in resumen.items():
        print(f"{categoria}: {cantidad} archivo(s)")
