from statistics import median

class Geometria():
    def __init__(self,d1:float,d2:float,t1:float,t2:float) -> None:
        self.diametroMenor = d1
        self.diametroMaior = d2
        self.espessuraMenor = t1
        self.espessuraMaior = t2
        
    def __repr__(self) -> dict:
        pass
    
    def __str__(self) -> str:
        pass
    
    def diametroMedio(self) -> float:
        """calcula o diametro medio da extremidade
        Returns:
            float: diâmetro médio
        """
        dM = median([self.diametroMenor,self.diametroMenor])
        return(dM)
    
    def espessuraMedia(self) -> float:
        """calcula a espessura media da extremidade

        Returns:
            float: espessura média
        """
        eM = median([self.espessuraMenor,self.espessuraMaior])
        return(eM)