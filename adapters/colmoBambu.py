from statistics import median
from entites.propriedadesGeometricas import Geometria

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
        
        D = median([self.e1.diametroMedio(),self.e2.diametroMedio()])
        
        if(65*D <= self.L):
            return(D)
        
        else:
            return("A barra não pode ser tratada como prismática, 65*D > L")
        