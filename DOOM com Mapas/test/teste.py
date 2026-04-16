import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Módulos.Mapas import *
import time
import random
import keyboard

"""
🟥🟧🟨🟩🟦🟪🟫⬛⬜
"""

def detectar_movimento(movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo):
    if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
        movimento_esquerda = True
        movimento_direita = False
        movimento_cima = False
        movimento_baixo = False
    elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
        movimento_esquerda = False
        movimento_direita = True
        movimento_cima = False
        movimento_baixo = False
    elif keyboard.is_pressed("w") or keyboard.is_pressed("up"):
        movimento_esquerda = False
        movimento_direita = False
        movimento_cima = True
        movimento_baixo = False
    elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
        movimento_esquerda = False
        movimento_direita = False
        movimento_cima = False
        movimento_baixo = True

    return movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo

def movimento(x, y, movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo):
    if movimento_esquerda:
        x -= 1
    elif movimento_direita:
        x += 1
    elif movimento_cima:
        y -= 1
    elif movimento_baixo:
        y += 1

    return x, y

tamanho_x = 96
tamanho_y = 48
mapa = Mapa("Teste", tamanho_x, tamanho_y, "⬜")
x = random.randint(0, len(mapa.mapa[0])-1)
y = random.randint(0, len(mapa.mapa)-1)

movimento_esquerda = False
movimento_direita = False
movimento_cima = False
movimento_baixo = False

for i in range(100000):
    mapa.limpar_mapa("⬜")
    frame_inicio = time.time()
    movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo = detectar_movimento(movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo)
    x, y = movimento(x, y, movimento_esquerda, movimento_direita, movimento_cima, movimento_baixo)
    if x < 0 or y < 0 or x > (tamanho_x - 1) or y > (tamanho_y - 1):
        print("Você bateu na parede!")
        break
    print("\033[H", end="")  # move cursor pro topo
    mapa.pintar([x, y], "⬛")
    mapa.mostrar()
    time.sleep(0.1)