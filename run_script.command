#!/bin/bash
# Obtener la ruta del directorio donde se encuentra el archivo run_script.command
dir_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Ingrese la ruta del archivo de video:"
read video_path

echo "Ingrese la ruta del archivo de audio:"
read audio_path

# Construir la ruta del archivo main.py utilizando la ruta del directorio
main_path="$dir_path/main.py"

python3 "$main_path" "$video_path" "$audio_path"