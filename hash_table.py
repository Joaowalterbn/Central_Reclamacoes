from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Empresa:
    nome: str
    problema: str
    score: int

@dataclass
class Node:
    empresa: Empresa
    next: Optional['Node'] = None

class HashTable:
    def __init__(self, tamanho: int = 53):
            self.tamanho: int = tamanho
            self.tabela: List[Optional[Node]] = [None] * self.tamanho
    def hash_fuction(self, nome_empresa: str) -> int:
        hash_value = 5381
        for char in nome_empresa:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.tamanho
    def busca(self, nome_empresa: str) -> Optional[Empresa]:
         indice = self.hash_fuction(nome_empresa)
         atual = self.tabela[indice]
        
         while atual is not None:
            if atual.empresa.nome == nome_empresa:
                return atual.empresa 
            atual = atual.next
            
         return None
    def inserir(self, nova_empresa: Empresa) -> None:
        indice = self.hash_fuction(nova_empresa.nome)
        
        #Caso base: Se a célula ta vazia
        if self.tabela[indice] is None:
            self.tabela[indice] = Node(empresa=nova_empresa)
            return
        
        #Senão: Criar nodo na lista encadeada
        atual = self.tabela[indice]

        while True:
            if atual.empresa.nome == nova_empresa.nome: #Eliminando caso a empresa já esteja cadastrada. 
                return
            #OBS.: Temos que ver como fazer para acrescentar a reclamação mesmo que a empresa já esteja lá

            if atual.next is None:
                break
            atual = atual.next
        atual.next = Node(empresa=nova_empresa)