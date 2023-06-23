import os
import time
import pyfiglet
from termcolor import colored

os.system("clear")

def banner():
    banner = r"""
 _______                             _      _ _
|__   __|                           | |    (_) |
   | | ___ _ __ _ __ ___  _   ___  _| |     _| |__  _ __ __ _ _ __ _   _
   | |/ _ \ '__| '_ ` _ \| | | \ \/ / |    | | '_ \| '__/ _` | '__| | | |
   | |  __/ |  | | | | | | |_| |>  <| |____| | |_) | | | (_| | |  | |_| |
   |_|\___|_|  |_| |_| |_|\__,_/_/\_\______|_|_.__/|_|  \__,_|_|   \__, |
                                                                    __/ |
                                                                   |___/
"""
    colored_banner = colored(banner, "magenta")
    print(colored_banner)

banner()

instagram = colored("Instagram: ", "green") + colored("@coderfenrir", "yellow")
github = colored("GitHub: ", "green") + colored("coderfenrir", "yellow")
version = colored("Version: ", "green") + colored("1.0", "yellow")

print(instagram)
print(github)
print(version)

libraries = ['numpy', 'pandas', 'matplotlib', 'seaborn',
'scikit-learn', 'tensorflow', 'keras', 'colorama', 'vim',
'selenium', 'cython', 'colored', 'python', 'python2', 'git', 'nmap',
'flask', 'beautifulsoup', 'urllib3', 'requests', 'opencv-python']

def show_libraries():
    print("Aşağıdaki kütüphaneler kurulacak:")
    for lib in libraries:
        print(f" - {lib}")

    while True:
        choice = input("Kütüphane listesini görmek ister misiniz? (E/H)").lower()
        if choice == "e":
            print("Kütüphane listesi:")
            os.system("pip freeze")
            break
        elif choice == "h":
            break

def install_libraries():
    for lib in libraries:
        os.system(f"pip install {lib}")
        print(f"{lib} yüklendi.")

def get_confirmation():
    while True:
        choice = input("Kütüphaneleri yüklemek istiyor musunuz? (E/H)").lower()
        if choice == "e":
            return True
        elif choice == "h":
            return False

def main():
    print("Python için popüler kütüphaneleri tek bir tuşla yükleyin!")
    print("--------------------------------------------------------")
    show_libraries()
    if get_confirmation():
        install_libraries()
        print("--------------------------------------------------------")
        print("Tüm kütüphaneler yüklendi.")
    else:
        print("İşlem iptal edildi.")

if __name__ == '__main__':
    main()