from re import T
from statistics import median
from entites.propriedadesGeometricas import Geometria
from entites.propriedadesFisicas import *
from math import pi,pow,sqrt

class colmoDeBambu():
    def __init__(self,id:int,geometria1:Geometria,geometria2:Geometria,comprimento:float,propfisica:PropriedadesFisicas) -> None:
        self.id = id
        self.e1 = geometria1
        self.e2 = geometria2
        self.L = comprimento
        self.fcok = propfisica.fco
        self.eb = propfisica.elasticidadeCompressaoParalela()
    
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
        return(D)

    def Espessura(self) -> float:
        t = median([self.e1.espessuraMedia(),self.e2.espessuraMedia()])
        return(t)
        
    def DiametroInterno(self) -> float:
        d = self.DiametroExterno() - 2*self.Espessura()
        return(d)
        
    def MomentoDeInercia(self) -> float:
        I = pi*(pow(self.DiametroExterno(),4)-pow(self.DiametroInterno(),4))/64
        return(I)
    
    def Area(self) -> float:
        Ai = pi*(pow(self.DiametroExterno(),2)-pow(self.DiametroInterno(),2))/4
        return(Ai)
        
    def Conicidade(self) -> float:
        cmax = max([self.e1.diametroMaior, self.e1.diametroMenor, self.e2.diametroMaior,self.e2.diametroMenor])
        cmin = min([self.e1.diametroMaior, self.e1.diametroMenor, self.e2.diametroMaior,self.e2.diametroMenor])
        c = 100*(cmax-cmin)/self.L
        return(c)
    
    def RaioDeGiracao(self) -> float:
        i = sqrt(self.MomentoDeInercia()/self.Area())
        return(i)
    
    def Esbeltez(self) -> float:
        e = self.L/self.RaioDeGiracao()
        return(e)