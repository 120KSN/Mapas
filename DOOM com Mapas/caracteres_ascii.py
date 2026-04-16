from Módulos.Mapas import *

"""
🟥🟧🟨🟩🟦🟪🟫⬛⬜
"""
tamanho_padrao = 5

def escrever_a(x, y):
    mapa.linha([x + 1, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 1], [x, y + 4], "⬛")
    mapa.linha([x + 3, y + 1], [x + 3, y + 4], "⬛")
    mapa.linha([x, y + 2], [x + 3, y + 2], "⬛")

def escrever_b(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 2], [x + 2, y + 2], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")
    mapa.pintar([x + 3, y + 1], "⬛")
    mapa.pintar([x + 3, y + 3], "⬛")

def escrever_c(x, y):
    mapa.linha([x + 1, y], [x + 3, y], "⬛")
    mapa.linha([x + 1, y + 4], [x + 3, y + 4], "⬛")
    mapa.linha([x, y + 1], [x, y + 3], "⬛")

def escrever_d(x, y):
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x + 3, y + 1], [x + 3, y + 3], "⬛")

def escrever_e(x, y):
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 2], [x + 2, y + 2], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")
    mapa.linha([x, y], [x, y + 4], "⬛")

def escrever_f(x, y):
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 2], [x + 2, y + 2], "⬛")
    mapa.linha([x, y], [x, y + 4], "⬛")

def escrever_g(x, y):
    mapa.linha([x + 1, y], [x + 3, y], "⬛")
    mapa.linha([x, y + 1], [x, y + 3], "⬛")
    mapa.linha([x + 1, y + 4], [x + 3, y + 4], "⬛")
    mapa.linha([x + 3, y + 2], [x + 3, y + 4], "⬛")
    mapa.linha([x + 2, y + 2], [x + 3, y + 2], "⬛")

def escrever_h(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 4], "⬛")
    mapa.linha([x, y + 2], [x + 3, y + 2], "⬛")

def escrever_i(x, y):
    mapa.linha([x + 2, y], [x + 2, y + 4], "⬛")

def escrever_j(x, y):
    mapa.linha([x, y + 3], [x + 2, y + 4], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 3], "⬛")

def escrever_k(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x + 1, y + 2], [x + 3, y], "⬛")
    mapa.linha([x + 1, y + 2], [x + 3, y + 4], "⬛")

def escrever_l(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")

def escrever_m(x, y, tamanho_fonte):

    proporcao = tamanho_fonte / tamanho_padrao

    mapa.linha([x, y], [x, y + round(proporcao * 5 - 1)], "⬛")
    mapa.linha([x + round(proporcao * 5 - 1), y], [x + round(proporcao * 5 - 1), y + round(proporcao * 5 - 1)], "⬛")
    mapa.linha([x, y], [x + round(proporcao * 3 - 1), y + round(proporcao * 3 - 1)], "⬛")
    mapa.linha([x + round(proporcao * 3 - 1), y + round(proporcao * 3 - 1)], [x + round(proporcao * 5 - 1), y], "⬛")

def escrever_n(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 4], "⬛")
    mapa.linha([x, y], [x + 3, y + 3], "⬛")

def escrever_o(x, y):
    mapa.linha([x + 1, y], [x + 2, y], "⬛")
    mapa.linha([x + 1, y + 4], [x + 2, y + 4], "⬛")
    mapa.linha([x, y + 1], [x, y + 3], "⬛")
    mapa.linha([x + 3, y + 1], [x + 3, y + 3], "⬛")

def escrever_p(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 2], [x + 2, y + 2], "⬛")
    mapa.pintar([x + 3, y + 1], "⬛")

def escrever_q(x, y):
    mapa.linha([x + 1, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 1], [x, y + 3], "⬛")
    mapa.linha([x + 3, y + 1], [x + 3, y + 2], "⬛")
    mapa.linha([x + 1, y + 4], [x + 3, y + 2], "⬛")
    mapa.pintar([x + 3, y + 4], "⬛")

def escrever_r(x, y):
    mapa.linha([x, y], [x, y + 4], "⬛")
    mapa.linha([x, y], [x + 2, y], "⬛")
    mapa.linha([x, y + 2], [x + 2, y + 2], "⬛")
    mapa.pintar([x + 3, y + 1], "⬛")
    mapa.linha([x, y + 1], [x + 3, y + 4], "⬛")

def escrever_s(x, y):
    mapa.linha([x + 1, y], [x + 3, y], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")
    mapa.linha([x, y + 1], [x + 3, y + 3], "⬛")

def escrever_t(x, y):
    mapa.linha([x, y], [x + 4, y], "⬛")
    mapa.linha([x + 2, y], [x + 2, y + 4], "⬛")

def escrever_u(x, y):
    mapa.linha([x, y], [x, y + 3], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 3], "⬛")
    mapa.linha([x + 1, y + 4], [x + 2, y + 4], "⬛")

def escrever_v(x, y):
    mapa.linha([x, y], [x, y + 1], "⬛")
    mapa.linha([x + 1, y + 2], [x + 1, y + 3], "⬛")
    mapa.linha([x + 4, y], [x + 4, y + 1], "⬛")
    mapa.linha([x + 3, y + 2], [x + 3, y + 3], "⬛")
    mapa.pintar([x + 2, y + 4], "⬛")

def escrever_w(x, y):
    mapa.linha([x, y], [x, y + 2], "⬛")
    mapa.linha([x + 1, y + 3], [x + 1, y + 4], "⬛")
    mapa.linha([x + 2, y], [x + 2, y + 2], "⬛")
    mapa.linha([x + 3, y + 3], [x + 3, y + 4], "⬛")
    mapa.linha([x + 4, y], [x + 4, y + 2], "⬛")

def escrever_x(x, y):
    mapa.linha([x, y], [x, y + 1], "⬛")
    mapa.linha([x, y + 3], [x, y + 4], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 1], "⬛")
    mapa.linha([x + 3, y + 3], [x + 3, y + 4], "⬛")
    mapa.linha([x + 1, y + 2], [x + 2, y + 2], "⬛")

def escrever_y(x, y):
    mapa.linha([x, y], [x, y + 2], "⬛")
    mapa.linha([x + 3, y], [x + 3, y + 3], "⬛")
    mapa.linha([x, y + 2], [x + 3, y + 2], "⬛")
    mapa.linha([x, y + 4], [x + 2, y + 4], "⬛")

def escrever_z(x, y):
    mapa.linha([x, y], [x + 3, y], "⬛")
    mapa.linha([x, y + 4], [x + 3, y + 4], "⬛")
    mapa.linha([x, y + 3], [x + 3, y + 1], "⬛")

if __name__ == "__main__":
    tamanho_x = 96
    tamanho_y = 48
    mapa = Mapa("Teste", tamanho_x, tamanho_y, "⬜")
    mapa.mostrar()

    escrever_m(0, 0, 10)

    mapa.mostrar()