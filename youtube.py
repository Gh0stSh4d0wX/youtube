import yt_dlp
from tqdm import tqdm

# Crear un objeto yt_dlp con la opción de la máxima resolución
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
}

def descargar_video(url, formato):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info['title']
        print(f"Descargando: {video_title} en formato {formato}")
        
        # Configurar el formato de salida según la elección del usuario
        ydl_opts['format'] = f'bestvideo[ext={formato}]+bestaudio[ext=webm]/best[ext={formato}/webm]/best'
        
        # Agregar la barra de progreso
        with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=f'Descargando {video_title}') as progress_bar:
            ydl_opts['progress_hooks'] = [lambda d: progress_bar.update(d['downloaded_bytes'])]
            ydl.download([url])
        
        print("Descarga completada")

if __name__ == "__main__":
    url = input("Introduce el enlace del video de YouTube: ")
    
    formatos_disponibles = ["mp4", "webm", "mkv", "avi", "flv", "mov", "ogg", "3gp", "mp3", "m4a"]
    formato = input(f"Selecciona el formato de salida ({', '.join(formatos_disponibles)}): ").lower()
    
    if formato not in formatos_disponibles:
        print("Formato no válido. Elige uno de los formatos disponibles.")
    else:
        descargar_video(url, formato)
