# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
import math


# CLASSES
# grafo matriz  --  rotulado ou não
# grafo nao direcionado -- rotulado ou não
# Implementar uma classe Vértice

class GrafoMatriz:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.rotulado = False  # servirá de verificação nos métodos abaixo
        # matriz de adjacência
        if rotulado:
            self.rotulado = True
            self.adj: list[list[float]] = [[math.inf for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insere_a(self, v, w, rotulo=-1):  # rotulo -1 é para quando não se sabe o peso daquela aresta
        if self.rotulado and self.adj[v][w] == math.inf:
            self.adj[v][w] = rotulo
            self.m += 1
        if not self.rotulado and self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1  # atualiza qtd arestas

    def insere_v(self):
        self.n += 1
        if self.rotulado:
            for linha in self.adj:
                linha.append(math.inf)
            self.adj.append([math.inf for i in range(self.n)])
        else:
            self.adj.append([0 for i in range(self.n)])

    # remove uma aresta v->w do Grafo
    def remove_a(self, v, w):
        # testa se temos a aresta
        if not self.rotulado and self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1  # atualiza qtd arestas
        if self.rotulado and self.adj[v][w] != math.inf:
            self.adj[v][w] = math.inf
            self.m -= 1

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    def show(self):
        print(f"\n n: {self.n:2d} m: {self.m:2d} r: {self.rotulado}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} | ", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida
    # Apresentando apenas os valores 0 ou 1
    def show_min(self):
        print(f"\n n: {self.n:2d} m: {self.m:2d} r: {self.rotulado}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f" {self.adj[i][w]} |", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    def in_degree(self, v: int) -> int:
        return len([linha for linha in self.adj if linha[v] != 0 and linha[v] != math.inf])

    def out_degree(self, v: int) -> int:
        return len([sai for sai in self.adj[v] if sai != 0 and sai != math.inf])

    def is_fonte(self, v: int) -> int:
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return 1
        return 0

    def is_sorvedouro(self, v) -> int:
        if self.in_degree(v) > 0 and self.out_degree(v) == 0:
            return 1
        return 0

    def is_simetrico(self) -> int:
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
                else:
                    return 1

    def remover(self, v: int) -> int:
        if v < self.n:
            # Remove as arestas
            for _ in range(0, len(self.adj[v])):
                self.remove_a(v, _)
                self.remove_a(_, v)
            # Remove os vértices
            for linha in self.adj:
                del linha[v]
            del self.adj[v]
            self.n -= 1
            return 1
        else:
            return 0

    def completo(self) -> int:  # dei ctrl c ctrl v
        checa = 1
        for i in range(self.n):
            for w in range(self.n):
                if i != w:
                    if self.adj[i][w] != 0 and self.adj[i][w] != math.inf:
                        continue
                    else:
                        checa = 0
                        break
        if checa == 1:
            return 1
        else:
            return 0

    @staticmethod
    def visitar_no(no: int):
        print(f"Estamos visitando o nó {no}")

    @staticmethod
    def marcar_no(marcados, no):
        marcados.append(no)
        return marcados

    def no_adjacente(self, no, marcados):
        adjs = self.adj[no]
        for _ in range(self.n):
            if (adjs[_] != 0 and adjs[_] != math.inf) and _ not in marcados:
                return _
        return -1

    def nos_adjacentes(self, no, marcados):
        return [index for index, valor in enumerate(self.adj[no]) if (valor != 0 and valor != math.inf) and marcados]

    def percurso_profundidade(self, v_inicio):
        marcados = []
        p = Pilha()
        self.visitar_no(v_inicio)
        marcados = self.marcar_no(marcados, v_inicio)
        p.push(v_inicio)
        while not p.is_empty():
            no_atual = p.pop()
            no_seguinte = self.no_adjacente(no_atual, marcados)
            while no_seguinte != -1:
                self.visitar_no(no_seguinte)
                p.push(no_atual)
                self.marcar_no(marcados, no_seguinte)
                no_atual = no_seguinte
                no_seguinte = self.no_adjacente(no_seguinte, marcados)



class TGrafoND:
    TAM_MAX_DEFAULT = 100
    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n
        self.m = 0
        self.rotulado = False

        if rotulado:
            self.rotulado = True
            self.adj = [[math.inf for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

    def insere_v(self):
        self.n += 1
        if self.rotulado:
            for linha in self.adj:
                linha.append(math.inf)
            self.adj.append([math.inf for i in range(self.n)])
        else:
            self.adj.append([0 for i in range(self.n)])

    def insere_a(self, v, w, valor: float = 1):
        if self.rotulado and self.adj[v][w] == math.inf:
            self.adj[v][w], self.adj[w][v] = valor, valor
            self.m += 1
        if not self.rotulado and self.adj[v][w] == 0:
            self.adj[v][w], self.adj[w][v] = valor, valor
            self.m += 1

    def remove_a(self, v, w):
        if self.rotulado and self.adj[v][w] != math.inf:
            self.adj[v][w], self.adj[w][v] = math.inf, math.inf
            self.m -= 1
        if not self.rotulado and self.adj[v][w] != 0:
            self.adj[v][w], self.adj[w][v] = 0, 0
            self.m -= 1

    def show(self):
        if self.rotulado:
            print(f"\n n: {self.n:2d} ", end="")
            print(f"m: {self.m:2d}\n")
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] != math.inf:
                        print(f"Adj[{i:2d},{w:2d}] = ", self.adj[i][w], end=" ")
                    else:
                        print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
                print("\n")
            print("\nfim da impressao do grafo.")
        else:
            print(f"\n n: {self.n:2d} ", end="")
            print(f"m: {self.m:2d}\n")
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] == 1:
                        print(f"Adj[{i:2d},{w:2d}] = 1 ", end="")
                    else:
                        print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
                print("\n")
            print("\nfim da impressao do grafo.")

    def show_min(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.rotulado:
                    if self.adj[i][w] != math.inf:
                        print(" ", self.adj[i][w], end=" ")
                    else:
                        print(" 0 ", end="")
                else:
                    if self.adj[i][w] == 1:
                        print(" 1 ", end="")
                    else:
                        print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    def in_degree(self, v: int) -> int:
        return len([linha for linha in self.adj if linha[v] != 0 and linha[v] != math.inf])

    def out_degree(self, v: int) -> int:
        return len([sai for sai in self.adj[v] if sai != 0 and sai != math.inf])

    def is_fonte(self, v: int) -> int:
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return 1
        return 0

    def is_sorvedouro(self, v: int) -> int:
        if self.in_degree(v) > 0 and self.out_degree(v) == 0:
            return 1
        return 0

    @staticmethod
    def is_simetrico() -> int:
        return 1

    def remover(self, v: int) -> int:
        if v < self.n:
            # Remove as arestas
            for _ in range(0, len(self.adj[v])):
                self.remove_a(v, _)
                self.remove_a(_, v)
            # Remove os vértices
            for linha in self.adj:
                del linha[v]
            del self.adj[v]
            self.n -= 1
            return 1
        else:
            return 0

    def completo(self) -> int:  # dei ctrl c ctrl v
        checa = 1
        for i in range(self.n):
            for w in range(self.n):
                if i != w:
                    if self.adj[i][w] != 0 and self.adj[i][w] != math.inf:
                        continue
                    else:
                        checa = 0
                        break
        if checa == 1:
            return 1
        else:
            return 0

        
class GrafoMatriz:
# para gravar no txt
    def to_str(self) -> str:
        s = f"{self.n} {self.rotulado}\n"
        for i in range(self.n):
            for w in range(self.n):
                s += f"{self.adj[i][w]} "
            s += "\n"
        return s

    def save(self, nomeTxt: str):
        with open(nomeTxt, "w") as f:
            f.write(self.to_str())

    @classmethod
    def load(cls, nomeTxt: str) -> "GrafoMatriz":
        with open(nomeTxt) as f:
            n, rotulado = map(int, f.readline().strip().split())
            grafo = cls(n=n, rotulado=bool(rotulado))
            for i in range(n):
                linha = list(map(float, f.readline().strip().split()))
                for w in range(n):
                    grafo.adj[i][w] = linha[w]
                    if linha[w] != 0:
                        grafo.m += 1
        return grafo

    def insere_a(self, v, w, rotulo=-1):
        if self.rotulado:
            if self.adj[v][w] == math.inf:
                self.adj[v][w] = rotulo
                self.adj[w][v] = rotulo  
                self.m += 1
        else:
            if self.adj[v][w] == 0:
                self.adj[v][w] = 1
                self.adj[w][v] = 1  
                self.m += 1
                
    def remover(self, v: int) -> int:
        if v < self.n:
            # Remove as arestas
            for _ in range(0, len(self.adj[v])):
                self.remove_a(v, _)
                self.remove_a(_, v)
            # Remove os vértices
            for linha in self.adj:
                del linha[v]
            del self.adj[v]
            self.n -= 1
            return 1
        else:
            return 0
