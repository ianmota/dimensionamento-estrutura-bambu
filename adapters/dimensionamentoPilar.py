from adapters.tensoes import *

class Dimensionamento():
    def __init__(self,tensoes:Tensoes) -> None:
        self.tensao = tensoes
        
    def __str__(self) -> str:
        return(f"P({self.classificacaoPilar()}{self.tensao.un_tensao()})")
    
    def __repr__(self) -> str:
        pass
    
    def classificacaoPilar(self):
        if(self.tensao.resistencia_bambu.bambu.Esbeltez()<=30):
            return(self.pilarCurto())
        if(30<self.tensao.resistencia_bambu.bambu.Esbeltez()):
            return(self.pilarMedio())
            
    def pilarCurto(self):
        return(self.tensao.TensaoNormal())
    
    def pilarMedio(self):
        return(self.tensao.FlexaoNormal())

        