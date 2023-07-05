import argparse
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import imageio.plugins.ffmpeg as ffmpeg

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

# Configurar el codificador de video con el backend de metal2
ffmpeg_version_info = ffmpeg.get_ffmpeg_version_info()
ffmpeg.add_command("-vcodec", "h264_videotoolbox", "-b:v", "5000k", "-profile:v", "high", "-pix_fmt", "yuv420p", "-movflags", "faststart")

# Codificar el video con Metal2
output_path = os.path.splitext(args.video)[0] + ".mp4"
video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")