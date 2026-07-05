from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Problema:
    tipo: str
    quant: int = 1

@dataclass
class Empresa:
    nome: str
    acu_nota: int
    cont_nota: int
    acu_tempo: int
    cont_tempo: int
    lista_problemas: List[Problema] = field(default_factory=list)

    def registrar_problema(self, tipo_problema: str) -> None:
        for p in self.lista_problemas:
            if p.tipo == tipo_problema:
                p.quant += 1
                return
        self.lista_problemas.append(Problema(tipo=tipo_problema))

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
    