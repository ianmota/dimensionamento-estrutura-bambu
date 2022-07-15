from entites.propriedadesGeometricas import *
from entites.propriedadesFisicas import *
from math import pi,pow,sqrt

class colmoDeBambu():
    def __init__(self,id:int,geometria1:Geometria,geometria2:Geometria,comprimento:float,propfisica:PropriedadesFisicas) -> None:
        """Cria um colmo de bambu com todos os seus elementos a partir das propriedades geometricas e físicas
        """
        self.id = id
        self.e1 = geometria1
        self.e2 = geometria2
        self.L = comprimento
        self.p_fisicas = propfisica
    
    def __repr__(self) -> str:
        return(f"Bambu{self.id}({self.e1},{self.e2},{self.p_fisicas},{self.L} {self.e1.un})")
    
    def __str__(self) -> str:
        return(f"Bambu{self.id}({self.e1},{self.e2},{self.p_fisicas},{self.L} {self.e1.un})")
    
    def DiametroExterno(self) -> float:
        """calcula o diametro do colmo como uma barra prismática quando possível
        Returns:
            diâmetro do colmo(float)
        """
        D = median([self.e1.diametroMedio(),self.e2.diametroMedio()])
        return(D)

    def Espessura(self) -> float:
        """Determina a espessura do colmo considerando uma barra prismática
        Returns:
            Espessura(float)
        """
        t = median([self.e1.espessuraMedia(),self.e2.espessuraMedia()])
        return(t)
        
    def DiametroInterno(self) -> float:
        """Calcula o diâmetro interno do colmo prismático
        Returns:
            Diâmetro interno(float)
        """
        d = self.DiametroExterno() - 2*self.Espessura()
        return(d)
        
    def MomentoDeInercia(self) -> float:
        """Calcula o momento de inércia do colmo
        Returns:
            Momento de inércia(float) 
        """
        I = pi*(pow(self.DiametroExterno(),4)-pow(self.DiametroInterno(),4))/64
        return(I)
    
    def Area(self) -> float:
        """determina a área da secção do colmo
        Returns:
            Área(float)
        """
        Ai = pi*(pow(self.DiametroExterno(),2)-pow(self.DiametroInterno(),2))/4
        return(Ai)
        
    def Conicidade(self) -> float:
        """determina a conicidade do colmo com base nas extremidades
        Returns:
            conicidade(float)
        """
        cmax = max([self.e1.diametroMaior, self.e1.diametroMenor, self.e2.diametroMaior,self.e2.diametroMenor])
        cmin = min([self.e1.diametroMaior, self.e1.diametroMenor, self.e2.diametroMaior,self.e2.diametroMenor])
        c = 100*(cmax-cmin)/self.L
        return(c)
    
    def RaioDeGiracao(self) -> float:
        """calcula o raio de giração do colmo
        Returns:
            raio de giração(float) 
        """
        i = sqrt(self.MomentoDeInercia()/self.Area())
        return(i)
    
    def Esbeltez(self) -> float:
        """calcula a esbeltez do colmo
        Returns:
            esbeltez(float)
        """
        e = self.L/self.RaioDeGiracao()
        return(e)
    
    def un_area(self) -> str:
        """retorna a unidade da área
        Returns:
            unidade area(str)
        """
        return(f"{self.e1.un}^2")
    
    def un_inercia(self) -> str:
        """retorna a unidade do momento de inercia
        Returns:
            unidade inercia(str)
        """
        return(f"{self.e1.un}^4")
    
    def un_linear(self) -> str:
        """retorna a unidade linear
        Returns:
            unidade linear(str)
        """
        return(f"{self.e1.un}")