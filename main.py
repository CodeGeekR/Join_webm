import argparse
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Crear un objeto ArgumentParser para manejar los argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Unir archivos de video y audio en un archivo .mp4")

# Agregar los argumentos de línea de comandos
parser.add_argument("video", help="Ruta del archivo de video")
parser.add_argument("audio", help="Ruta del archivo de audio")

# Obtener los argumentos de línea de comandos
args = parser.parse_args()

# Verificar que el archivo de audio exista
if not os.path.isfile(args.audio):
    print(f"El archivo de audio {args.audio} no existe.")
    exit()

# Verificar que el archivo de video exista
if not os.path.isfile(args.video):
    print(f"El archivo de video {args.video} no existe.")
    exit()
    

# Cargar el archivo de video y el archivo de audio
video = VideoFileClip(args.video)
audio = AudioFileClip(args.audio)

# Unir el archivo de video y el archivo de audio
video_with_audio = video.set_audio(audio)

# Ruta de salida del archivo .mp4
output_path = os.path.expanduser("~/Downloads/video.mp4")

# Guardar el archivo de video con audio en formato .mp4
video_with_audio.write_videofile(output_path, codec="libx264")