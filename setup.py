from setuptools import setup

APP = ['SmartClick.py']  # Seu script Python principal
DATA_FILES = []  # Se tiver arquivos adicionais como imagens ou arquivos de configuração
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pyautogui', 'keyboard', 'tkinter'],  # Adicione suas dependências aqui
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},  # Para PyInstaller, configure adequadamente
    setup_requires=['py2app'],
)
