# DEFAULT_STAGES = "novo"

import json
import os

class stage_status:
    DEFAULT_STAGE = ["novo", "contato feito", "visita agendada", "proposta feita", "vendido ou alugado"]
    contador_file = os.path.join("data", "status_cont.json")
    contador = 0

    def __init__ (self):
        
        #carrega o contador salvo se existir
        stage_status.contador = self.carregar_contador()
        if stage_status.contador == len(stage_status.DEFAULT_STAGE):
            stage_status.contador = 0

        self.stages = stage_status.DEFAULT_STAGE[stage_status.contador]
        stage_status.contador += 1
        #salva o contador
        self.salvar_contador(stage_status.contador)

    def __str__ (self):
        return self.stages
    
    @classmethod #método p/ própria classe
    def carregar_contador(cls):
        if os.path.exists(cls.contador_file):
            with open (cls.contador_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f) #transformar em python
                except json.JSONDecodeError:
                    return 0
                
        return 0
    
    @classmethod
    def salvar_contador(cls, value):

        with open (cls.contador_file, "w", encoding="utf-8") as f:
            json.dump(value, f) #transforma em json