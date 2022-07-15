from statistics import median

class Geometria():
    def __init__(self,id:int,d1:float,d2:float,t1:float,t2:float,unidade:str) -> None:
        """Defini as dimensões da geometria de uma extremidade do colmo de bambu
        """
        self.id = id
        self.diametroMenor = d1
        self.diametroMaior = d2
        self.espessuraMenor = t1
        self.espessuraMaior = t2
        self.un = unidade
        
    def __repr__(self) -> dict:
        return(f"G{self.id}({self.diametroMedio()},{self.espessuraMedia()}) {self.un}")
    
    def __str__(self) -> str:
        return(f"G{self.id}({self.diametroMedio()},{self.espessuraMedia()}) {self.un}")
    
    def diametroMedio(self) -> float:
        """calcula o diametro medio da extremidade
        Returns:
            diâmetro médio(float) 
        """
        dM = median([self.diametroMenor,self.diametroMenor])
        return(dM)
    
    def espessuraMedia(self) -> float:
        """calcula a espessura media da extremidade
        Returns:
            espessura média(float) 
        """
        eM = median([self.espessuraMenor,self.espessuraMaior])
        return(eM)