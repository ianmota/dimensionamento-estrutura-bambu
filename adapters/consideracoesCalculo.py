from entites.carregamento import *
from adapters.colmoBambu import *
from math import pi

class ConsideracoesDeCalculo():
    def __init__(self,carga:Carregamento,bambu:colmoDeBambu) -> None:
        self.nd = carga.carga
        self.ngk = carga.carga
        self.m1d = carga.md
        self.y = bambu.DiametroExterno()/2
        self.I = bambu.MomentoDeInercia()
        self.L = bambu.L
        self.fcok = bambu.fcok
        self.D = bambu.DiametroExterno()
        self.area = bambu.Area()
        self.kmod = carga.kmod()
        self.ym = carga.GamaM()
        self.eb = bambu.eb
        self.nqk = 0
        self.esbeltez = bambu.Esbeltez()
        
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def TensaoNormal(self):
        tensao = self.nd/self.area
        return(tensao)
    
    def FlexaoSimples(self):
        flexao = self.MomentoDeCalculo()*self.y/self.I
        return(flexao)
    
    def FlexaoNormal(self):
        return(self.TensaoNormal()+self.FlexaoSimples())
    
    def ExcentricidadeAcidental(self):
        ea = self.L/100
        return(ea)
    
    def ExcentricidadeInicial(self):
        ei = self.D/20
        return(ei)
    
    def ExcentricidadeDeFluencia(self):
        eu = max([self.ExcentricidadeAcidental(),self.ExcentricidadeInicial])
        a = 0.8*(self.ngk + 0.9*self.nqk)/(self.ForcaEuler()-(self.ngk + 0.9*self.nqk))
        return(eu*(2.718**a -1))
        
    def Excentricidade(self):
        if(self.esbeltez >= 70):
            ec = self.ExcentricidadeDeFluencia()
        else:
            ec = 0
        return(self.ExcentricidadeAcidental+self.ExcentricidadeInicial + ec)
    
    def ResistenciaDeCalculo(self):
        fcod = self.kmod*self.fcok/self.ym
        return(fcod)
    
    def ForcaEuler(self):
        fe =  (pi**2*self.eb*self.I)/self.L**2
        return(fe)
    
    def TensaoLimite(self):
        return(min([self.ResistenciaDeCalculo(),self.ForcaEuler()]))
    
    def ForcaLimite(self):
        return(self.TensaoLimite()*self.area)
    
    def MomentoDeCalculo(self):
        md = self.nd*self.Excentricidade()/(1- self.nd/self.ForcaLimite())
        return(md)
