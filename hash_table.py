from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Problema:
    tipo: str
    quant: int = 1

@dataclass
class Empresa:
    nome: str
    cont_nota: int
    acu_tempo: int
    cont_tempo: int
    acu_nota: int = 0
    lista_problemas: List[Problema] = field(default_factory=list)

    def registrar_problema(self, tipo_problema: str) -> None:
        for p in self.lista_problemas:
            if p.tipo == tipo_problema:
                p.quant += 1
                return
        self.lista_problemas.append(Problema(tipo=tipo_problema))

@dataclass
class SimpleEmpresa:
    nome: str
    nota: float

@dataclass
class Node:
    empresa: Empresa
    next: Optional['Node'] = None

class MaxHeapTop150:
    def __init__(self, capacidade: int = 150):
        self.capacidade = capacidade
        self.heap: List[SimpleEmpresa] = []

    def _pai(self, i: int) -> int:
        return (i - 1) // 2

    def _filho_esquerdo(self, i: int) -> int:
        return (2 * i) + 1

    def _filho_direito(self, i: int) -> int:
        return (2 * i) + 2

    def _comparar(self, a: SimpleEmpresa, b: SimpleEmpresa) -> bool:
        if a.nota != b.nota:
            return a.nota > b.nota
        return a.nome > b.nome

    def _sift_up(self, indice: int):
        pai = self._pai(indice)
        
        while indice > 0 and self._comparar(self.heap[indice], self.heap[pai]):
            self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
            
            indice = pai
            pai = self._pai(indice)

    def _sift_down(self, indice: int):
        tamanho = len(self.heap)
        
        while True:
            maior = indice
            esq = self._filho_esquerdo(indice)
            dir = self._filho_direito(indice)

            if esq < tamanho and self._comparar(self.heap[esq], self.heap[maior]):
                maior = esq
                
            if dir < tamanho and self._comparar(self.heap[dir], self.heap[maior]):
                maior = dir

            if maior != indice:
                self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
                indice = maior 
            else:
                break

    def processar_empresa(self, empresa: SimpleEmpresa):
        
        if len(self.heap) < self.capacidade:
            self.heap.append(empresa)
            self._sift_up(len(self.heap) - 1)
            
        else:
            if self._comparar(self.heap[0], empresa):
                self.heap[0] = empresa
                self._sift_down(0)

    def obter_resultado_ordenado(self) -> List[SimpleEmpresa]:
        return sorted(self.heap, key=lambda e: (e.nota, e.nome))

class HashTable:
    def __init__(self, tamanho: int = 1009):
            self.tamanho: int = tamanho
            self.tabela: List[Optional[Node]] = [None] * self.tamanho
    def hash_function(self, nome_empresa: str) -> int:
        hash_value = 5381
        for char in nome_empresa:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.tamanho
    def busca(self, nome_empresa: str) -> Optional[Empresa]:
         indice = self.hash_function(nome_empresa)
         atual = self.tabela[indice]
        
         while atual is not None:
            if atual.empresa.nome == nome_empresa:
                return atual.empresa
            atual = atual.next
         return None
    def inserir(self, nova_empresa: Empresa) -> None:
        indice = self.hash_function(nova_empresa.nome)
        
        #Caso base: Se a célula ta vazia
        if self.tabela[indice] is None:
            self.tabela[indice] = Node(empresa=nova_empresa)
            return
        
        #Senão: Criar nodo na lista encadeada
        atual = self.tabela[indice]

        while True:
            #Eliminando caso a empresa já esteja cadastrada.
            if atual.empresa.nome == nova_empresa.nome:  
                atual.empresa.acu_nota += nova_empresa.acu_nota
                atual.empresa.acu_tempo += nova_empresa.acu_tempo #Na hora de mostrar, basta printar a divisão do acu/cont
                atual.empresa.cont_nota += 1
                atual.empresa.cont_tempo += 1
                if nova_empresa.lista_problemas:
                    problema_atual = nova_empresa.lista_problemas[0]
                    atual.empresa.registrar_problema(problema_atual.tipo)
                return

            if atual.next is None:
                break
            atual = atual.next
        atual.next = Node(empresa=nova_empresa)

    def excluir(self, nome_empresa: str) -> bool:

        indice = self.hash_function(nome_empresa)
        atual = self.tabela[indice]
        anterior: Optional[Node] = None #O ponteiro que vai seguir o atual
        
        while atual is not None:
            if atual.empresa.nome == nome_empresa:

                if anterior is None:
                    self.tabela[indice] = atual.next

                else:
                    anterior.next = atual.next
                
                return True
            
            anterior = atual
            atual = atual.next

        return False
    def ranking(self) -> List[SimpleEmpresa]:
        processador_heap = MaxHeapTop150(capacidade=150)

        for p in self.tabela:
            atual = p

            while atual is not None:
                nota_empresa = atual.empresa.acu_nota / atual.empresa.cont_nota if atual.empresa.cont_nota > 0 else 0.0
                nome_empresa = atual.empresa.nome
                
                empresa = SimpleEmpresa(
                    nome = nome_empresa,
                    nota = nota_empresa
                )

                processador_heap.processar_empresa(empresa)
                atual = atual.next

        return processador_heap.obter_resultado_ordenado()
    
def imprimir_ranking(lista_top_piores: List[SimpleEmpresa]):
    if not lista_top_piores:
        print("\nO ranking está vazio. Nenhuma empresa para exibir.")
        return

    print(f"\n========================================")
    print(f" RANKING: {len(lista_top_piores)} PIORES EMPRESAS")
    print(f"========================================")
    
    for i, emp in enumerate(lista_top_piores, start=1):
        nome_formatado = emp.nome[:20].ljust(22) 
        print(f"{i:02d}º | {nome_formatado} | Nota Média: {emp.nota:.2f}")
    
    print(f"========================================\n")



