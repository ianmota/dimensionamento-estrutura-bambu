from entites.carregamento import *
from entites.resistenciaBambu import *

class Tensoes():
    def __init__(self,carga:Carregamento,resistencia:Resistencia) -> None:
        """Calcula as tensões no colmo em decorrência do carregamento e de suas propriedades
        Args:
            carga (Carregamento)
            resistencia (Resistencia)
        """
        self.carregamento = carga
        self.resistencia_bambu = resistencia
        
    def __str__(self) -> str:
        return(f"T({self.TensaoNormal()}{self.un_tensao()},{self.FlexaoNormal()}{self.un_tensao()},{self.MomentoDeCalculo()}{self.un_momento()})")
    
    def __repr__(self) -> str:
        return(f"T({self.TensaoNormal()}{self.un_tensao()},{self.FlexaoNormal()}{self.un_tensao()},{self.MomentoDeCalculo()}{self.un_momento()})")
    
    def TensaoNormal(self)->float:
        """calcula a tensão normal no colmo
        """
        tensao = self.carregamento.nd/self.resistencia_bambu.bambu.Area()
        return(tensao)
    
    def FlexaoSimples(self)->float:
        """calcula a flexão (simples) no colmo
        """
        flexao = self.MomentoDeCalculo()*self.resistencia_bambu.bambu.DiametroExterno()/(2*self.resistencia_bambu.bambu.MomentoDeInercia())
        return(flexao)
    
    def FlexaoNormal(self)->float:
        """calcula a flexão composta no colmo
        """
        return(self.TensaoNormal()+self.FlexaoSimples())
    
    def ExcentricidadeAcidental(self)->float:
        """calcula a excentricidade acidental no colmo
        """
        ea = self.resistencia_bambu.bambu.L/100
        return(ea)
    
    def ExcentricidadeInicial(self)->float:
        """calcula a excentricidade inicial no colmo
        """
        ei = self.resistencia_bambu.bambu.DiametroExterno()/20
        return(ei)
    
    def ExcentricidadeDeFluencia(self)->float:
        """calcula a excentricidade de fluencia no colmo
        """
        eu = max([self.ExcentricidadeAcidental(),self.ExcentricidadeInicial()])
        a = 0.8*(self.carregamento.carga_permanente + 0.9*self.carregamento.carga_acidental)/(self.ForcaEuler()-(self.carregamento.carga_permanente + 0.9*self.carregamento.carga_acidental))
        return(eu*(2.718**a -1))
        
    def Excentricidade(self)->float:
        """calcula a excentricidade no colmo
        """
        if(self.resistencia_bambu.bambu.Esbeltez() >= 70):
            ec = self.ExcentricidadeDeFluencia()
        else:
            ec = 0
        return(self.ExcentricidadeAcidental()+self.ExcentricidadeInicial() + ec)
    
    def TensaoLimite(self)->float:
        """calcula a tensão limite no colmo
        """
        return(min([self.resistencia_bambu.fd(),self.resistencia_bambu.ForcaEuler()]))
    
    def ForcaLimite(self)->float:
        """calcula a força limite no colmo
        """
        return(self.TensaoLimite()*self.resistencia_bambu.bambu.Area())
    
    def MomentoDeCalculo(self)->float:
        """determina o momento de cálculo no colmo
        """
        md = self.carregamento.nd*self.Excentricidade()/(1- self.carregamento.nd/self.ForcaLimite())
        return(md)

    def un_forca(self):
        return(self.carregamento.unidade)
    
    def un_momento(self):
        return(f"{self.carregamento.unidade}{self.resistencia_bambu.bambu.e1.un}")
    
    def un_tensao(self):
        return(f"{self.carregamento.unidade}/{self.resistencia_bambu.bambu.e1.un}^2")