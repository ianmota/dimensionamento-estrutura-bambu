from statistics import median
from entites.propriedadesGeometricas import Geometria
from services.verificacoesNormativas import BarraPrismatica

class colmoDeBambu():
    def __init__(self,geometria1:Geometria,geometria2:Geometria,comprimento:float) -> None:
        self.e1 = geometria1
        self.e2 = geometria2
        self.L = comprimento
    
    def __repr__(self) -> str:
        pass
    
    def __str__(self) -> str:
        pass
    
    def DiametroExterno(self) -> float:
        """calcula o diametro do colmo como uma barra prismática quando possível

        Returns:
            float: diâmetro do colmo
        """
        
        self.D = median([self.e1.diametroMedio(),self.e2.diametroMedio()])
        return(BarraPrismatica(self.D,self.L,self.D))

    def Espessura(self) -> float:
        t = median([self.e1.espessuraMedia(),self.e2.espessuraMedia()])
        return(BarraPrismatica(self.D,self.L,t))
        
    def DiametroInterno(self) -> float:
        d = self.DiametroExterno() - 2*self.Espessura()
        return(BarraPrismatica(self.D,self.L,d))
        