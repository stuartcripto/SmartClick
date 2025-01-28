import pyautogui
import time
import tkinter as tk
from threading import Thread
import json
import os
import keyboard  


COORDS_FILE = "coordenadas.json"


auto_click_ativo = False
intervalo_click = 0.001  


def salvar_coordenadas(coordenadas):
    with open(COORDS_FILE, "w") as file:
        json.dump(coordenadas, file)
    print("Coordenadas salvas:", coordenadas)


def carregar_coordenadas():
    if os.path.exists(COORDS_FILE):
        with open(COORDS_FILE, "r") as file:
            return json.load(file)
    return {}


def capturar_coordenadas():
    coordenadas = {}
    
    input("Posicione o mouse no local do lead e pressione ENTER.")
    coordenadas["lead"] = pyautogui.position()
    print(f"Coordenada do lead gravada: {coordenadas['lead']}")

    
    input("Posicione o mouse no botão concluir e pressione ENTER.")
    coordenadas["concluir"] = pyautogui.position()
    print(f"Coordenada do concluir gravada: {coordenadas['concluir']}")

    salvar_coordenadas(coordenadas)


def executar_auto_click(coordenadas):
    global auto_click_ativo
    if not coordenadas:
        print("As coordenadas não foram gravadas. Grave antes de iniciar.")
        return

    auto_click_ativo = True
    print("Iniciando Auto-Click... Pressione F5 para parar.")

    while auto_click_ativo:
     
        pyautogui.click(coordenadas["lead"])
        time.sleep(intervalo_click)

       
        pyautogui.click(coordenadas["concluir"])
        time.sleep(intervalo_click)


def iniciar_auto_click():
    coordenadas = carregar_coordenadas()
    if not coordenadas:
        print("Nenhuma coordenada salva. Grave-as primeiro.")
        return
    thread = Thread(target=executar_auto_click, args=(coordenadas,))
    thread.start()


def parar_auto_click():
    global auto_click_ativo
    auto_click_ativo = False
    print("Auto-Click parado.")


keyboard.add_hotkey("F5", parar_auto_click)


def criar_app():
    root = tk.Tk()
    root.title("SmartClick")
    root.geometry("400x350")
    root.configure(bg="#1e1e2f")  


    marca = tk.Label(
        root,
        text="StuartCripto",
        font=("Arial", 10, "italic"),
        fg="#666",
        bg="#1e1e2f"
    )
    marca.place(relx=0.5, rely=0.95, anchor="center")

  
    titulo = tk.Label(
        root,
        text="Smart-Clicker",
        font=("Helvetica", 20, "bold"),
        fg="#ffffff",
        bg="#1e1e2f"
    )
    titulo.pack(pady=10)


    subtitulo = tk.Label(
        root,
        text="Automatize seus cliques com facilidade",
        font=("Helvetica", 12),
        fg="#bbbbbb",
        bg="#1e1e2f"
    )
    subtitulo.pack(pady=5)

   
    btn_gravar = tk.Button(
        root,
        text="Gravar Coordenadas",
        font=("Arial", 12),
        bg="#007acc",
        fg="#ffffff",
        activebackground="#005f99",
        activeforeground="#ffffff",
        command=capturar_coordenadas
    )
    btn_gravar.pack(pady=15, ipadx=10, ipady=5)

    
    btn_iniciar = tk.Button(
        root,
        text="Iniciar Auto-Click",
        font=("Arial", 12),
        bg="#28a745",
        fg="#ffffff",
        activebackground="#1c7a34",
        activeforeground="#ffffff",
        command=iniciar_auto_click
    )
    btn_iniciar.pack(pady=15, ipadx=10, ipady=5)

   
    btn_parar = tk.Button(
        root,
        text="Parar Auto-Click",
        font=("Arial", 12),
        bg="#dc3545",
        fg="#ffffff",
        activebackground="#a71d2a",
        activeforeground="#ffffff",
        command=parar_auto_click
    )
    btn_parar.pack(pady=15, ipadx=10, ipady=5)

   
    root.mainloop()


if __name__ == "__main__":
    criar_app()
