class Mapa:
    def __init__(self, nome, tamanho_x, tamanho_y, cor):
        # Inicia a classe Mapa e cria o mapa inicial, definindo seu nome, tamanho, e cor inicial dos quadrados que o compõem
        linha = ""
        self.nome = nome
        self.x = tamanho_x
        self.y = tamanho_y
        self.cor = cor
        self.mapa = []
        for i in range(self.x):
            linha += self.cor
        for i in range(self.y):
            self.mapa.append(linha)

    def mostrar(self):
        # Mostra o mapa, linha por linha
        print(self.nome)
        for i in range(self.y):
            print(self.mapa[i])
    
    def pintar(self, xy, cor):
        mapa = list(self.mapa[xy[1]])
        mapa[xy[0]] = cor
        self.mapa[xy[1]] = "".join(mapa)

    def linha_horizontal(self, x1, x2, y, cor):
        # Desenha uma linha horizontal no mapa
        mapa_temp = list(self.mapa[y])
        for i in range(x1, x2+1):
            mapa_temp[i] = cor
        self.mapa[y] = "".join(mapa_temp)

    def linha_vertical(self, y1, y2, x, cor):
        # Desenha uma linha vertical no mapa
        for i in range(y1, y2+1):
            mapa = list(self.mapa[i])
            mapa[x] = cor
            self.mapa[i] = "".join(mapa)

    def linha(self, xy1, xy2, cor):
        # Desenha uma linha no mapa(menos eficiente que linha_horizontal e linha_vertical, mas muito importante para desenhar linhas além das duas)
        if xy1[0] == xy2[0]:
            self.linha_vertical(min(xy1[1], xy2[1]), max(xy1[1], xy2[1]), xy1[0], cor)
            return
        if xy1[1] == xy2[1]:
            self.linha_horizontal(min(xy1[0], xy2[0]), max(xy1[0], xy2[0]), xy1[1], cor)
            return
        if xy1[0] > xy2[0]:
            xy1, xy2 = xy2, xy1
        
        mapa1 = []
        for i in range(self.y):
            mapa1.append(list(self.mapa[i]))

        coeficiente_angular = (xy2[1]-xy1[1])/(xy2[0]-xy1[0])
        y = xy1[1]
        for x in range(xy1[0], xy2[0]+1):
            y = coeficiente_angular*(x-xy1[0])+xy1[1]
            mapa1[int(round(y))][x] = cor

        self.mapa = []
        for i in range(len(mapa1)):
            self.mapa.append("".join(mapa1[i]))
    
    def limpar_mapa(self, cor):
        # Limpar o mapa com a cor desejada
        linha = self.cor * self.x
        self.mapa = []
        for i in range(self.y):
            self.mapa.append(linha)

if __name__ == "__main__":
    mapa = Mapa("Mapa1", 13, 13, "⬜")
    mapa.mostrar()
    mapa.linha_horizontal(3, 8, 1, "⬛")
    mapa.mostrar()
    mapa.linha_vertical(3, 8, 1, "⬛")
    mapa.mostrar()
    mapa.linha([1, 1], [6, 6], "⬛")
    mapa.mostrar()
    mapa.pintar([8, 8], "⬛")
    mapa.mostrar()
    mapa.limpar_mapa("⬜")
    mapa.mostrar()
