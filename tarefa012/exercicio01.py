import random
import time
import sys

def quick_sort_iterativo(vetor):
    if len(vetor) <= 1:
        return vetor
    pilha = [(0, len(vetor) - 1)]
    while pilha:
        inicio, fim = pilha.pop()
        if inicio >= fim:
            continue
        pivo = vetor[fim]
        i = inicio
        for j in range(inicio, fim):
            if vetor[j] < pivo:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                i += 1
        vetor[i], vetor[fim] = vetor[fim], vetor[i]
        pilha.append((inicio, i - 1))
        pilha.append((i + 1, fim))

def quick_sort_recursivo(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1
    if inicio >= fim:
        return
    pivo = vetor[fim]
    i = inicio
    for j in range(inicio, fim):
        if vetor[j] < pivo:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[fim] = vetor[fim], vetor[i]
    quick_sort_recursivo(vetor, inicio, i - 1)
    quick_sort_recursivo(vetor, i + 1, fim)
    return vetor
    
class Teste:
    def __init__(self):
        self.vetores = [
            [random.randint(0, 100) for _ in range(100)],
            [random.randint(0, 1000) for _ in range(1000)],
            [random.randint(0, 10000) for _ in range(10000)]
        ]
    
    def testar_algoritmos(self):
        for vetor in self.vetores:
            print(f"Vetor com {len(vetor)} elementos:")
            for algoritmo in [quick_sort_iterativo, quick_sort_recursivo]:
                inicio = time.time()
                algoritmo(vetor)
                fim = time.time()
                print(f"{algoritmo.__name__}: {fim - inicio:.5f} segundos")
            print()
            
sys.setrecursionlimit(10000)
Teste().testar_algoritmos()