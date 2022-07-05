from entites.carregamento import *
from adapters.colmoBambu import *

class DimensionamentoSimples():
    def __init__(self,carga:Carregamento,bambu:colmoDeBambu) -> None:
        self.nd = carga.carga
        self.md = carga.md
        self.bambu = bambu

    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def PilarCurto(self):
        tensao = self.nd.carga/self.bambu.Area()
        return(tensao)
    
        

        