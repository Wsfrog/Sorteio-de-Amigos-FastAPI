import random
from typing import List, Dict

class SorteadorService:
    def realizar_sorteio(self, nomes: List[str]) -> Dict[str, str]:
        
        participantes = nomes[:]
        random.shuffle(participantes)
        pares = {}
        quantidade = len(participantes)

        for i in range(quantidade):
            amigo_atual = participantes[i]
            amigo_secreto = participantes[(i + 1) % quantidade]
            pares[amigo_atual] = amigo_secreto
            
        return pares