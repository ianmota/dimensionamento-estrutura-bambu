from services.coeficientesRead import *
coeficientes = jsonRead("database/tabelaCoeficientes.json")

class Carregamento():
    def __init__(self,id:int,nd:float,tipo:str,ur:str,unidade:str,md:float) -> None:
        self.id = id
        self.carga = nd
        self.tipo = tipo
        self.ur = ur
        self.unidade = unidade
        self.md = md
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def kmod(self):
        kmod1 = coeficientes["kmod1"][self.tipo]
        kmod2 = coeficientes["kmod2"][self.ur]
        kmod3 = coeficientes["kmod3"]
        return(kmod1*kmod2*kmod3)
        
    
    
        