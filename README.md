# Script Python => Join .webm

Script desarrolado en Pyhon parar unir archivos de video y audio con la extension .webm utilizando la biblioteca moviepy.

# Requisitos

Este proyecto requiere Python 3 y las siguientes bibliotecas:

- moviepy
- argparse

# Instalación

1. Clona este repositorio en tu máquina local:

   ```bash copyable
   git clone https://github.com/CodeGeekR/Join_webm.git

   ```

2. Navega hasta el directorio del proyecto en la terminal:

   ```bash copyable
   cd <ruta_carpeta>
   ```

3. Ejecuta el siguiente comando para crear un nuevo entorno virtual:

   ```bash copyable
   python -m venv env
   ```

4. Activa el entorno virtual ejecutando el siguiente comando:

   - En Windows:

     ```bash copyable
     env\Scripts\activate.bat
     ```

   - En macOS o Linux:

     ```bash copyable
     source env/bin/activate
     ```

5. Para instalar las bibliotecas necesarias, puede utilizar los siguientes comandos:

   ```bash copyable
   pip install -r requirements.txt
   ```

# Uso

- Para utilizar este proyecto, ejecute el archivo main.py con los siguientes argumentos:

  ```bash copyable
  python main.py </ruta/video.webm> </ruta/audio.webm>
  ```

Este comando combinará el archivo de video <video.webm> y el archivo de audio <audio.webm> en un archivo de salida video.mp4 que se copiara en la misma carpeta de origen del video.

## Contribuye

¡Te invito a contribuir a este proyecto y hacerlo aún mejor! 😊

Si te gusta este proyecto, no olvides darle una Star ⭐️ en GitHub.

Si deseas contribuir con código, sigue estos pasos:

Haz un fork de este repositorio.
Crea una rama con tu nueva funcionalidad: git checkout -b feature/nueva-funcionalidad.
Realiza tus cambios y realiza commits: git commit -m "Añade nueva funcionalidad".
Envía tus cambios a tu repositorio remoto: git push origin feature/nueva-funcionalidad.
Abre un Pull Request en este repositorio principal.
Si encuentras algún problema o tienes alguna sugerencia, abre un Issue en el repositorio. Estaré encantado de ayudarte.

Comparte este proyecto con tus amigos y colegas.

Agradecimientos
¡Gracias por tu interés en este proyecto! Esperamos que sea útil y te diviertas explorando y contribuyendo. Si tienes alguna pregunta, no dudes en contactarme.
