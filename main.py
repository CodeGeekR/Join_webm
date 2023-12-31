import argparse
from moviepy.editor import VideoFileClip, AudioFileClip, VideoClip
import os
import moviepy.video.fx.all as vfx
import moviepy.video.tools.cuts as cuts
import moviepy.video.compositing.CompositeVideoClip as CompositeVideoClip

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

# Configurar el codificador de video con el backend de pyopencl
VideoClip._resize_with = "pyopencl"

# Construir la ruta de salida del archivo de video
output_path = os.path.splitext(args.video)[0] + ".mp4"

# output_path = os.path.expanduser("~/Downloads/video.mp4")
video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=4)