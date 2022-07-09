from services.coeficientesRead import *
coeficientes = jsonRead("database/tabelaCoeficientes.json")

class Carregamento():
    def __init__(self,id:int,nd:float,tipo_carga:str,ur:str,unidade:str,md:float,tipo_resistencia:str) -> None:
        self.id = id
        self.carga = nd
        self.tipo_carga = tipo_carga
        self.ur = ur
        self.unidade = unidade
        self.md = md
        self.resistencia = tipo_resistencia
        
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def kmod(self):
        kmod1 = coeficientes["kmod1"][self.tipo_carga]
        kmod2 = coeficientes["kmod2"][self.ur]
        kmod3 = coeficientes["kmod3"]
        return(kmod1*kmod2*kmod3)
    
    def GamaM(self):
        ym = coeficientes["ym"][self.resistencia]
        return(ym)
    
    
        