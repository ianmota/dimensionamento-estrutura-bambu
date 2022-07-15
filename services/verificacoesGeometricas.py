from adapters.colmoBambu import *

class VerificacoesGeometricas():
    def __init__(self,bambu:colmoDeBambu) -> None:
        """Verifica as condições da geometria do colmo de bambu seguindo as prescrições
        da NBR 16828-1
        Args:
            id (int): 
            bambu (colmoDeBambu):
        """
        self.bambu = bambu
    
    def __str__(self) -> str:
        c = self.ComprimentoMax().values()
        co = self.ConicidadeMax().values()
        e = self.EsbeltezMax().values()
        return(f"(Prismático({c}),Conicidade({co}),Esbeltez({e}))")
    
    def __repr__(self) -> dict:
        c = self.ComprimentoMax().values()
        co = self.ConicidadeMax().values()
        e = self.EsbeltezMax().values()
        return({"verificacao geometrica":[c,co,e]})
    
    def ComprimentoMax(self)->dict:
        """Verifica se o colmo em questão pode ser usado como elemento esturtural L<65D
        Returns:
        {"prismatica":bool}
        """
        if(self.bambu.L <= 65*self.bambu.DiametroExterno()):
            return({"prismatica":True})
        
        else:
            return({"prismatica":False})

    def ConicidadeMax(self)->dict:
        """Verifica a conicidade do elemento, para uso estrutural deve ter conicidade < 1%
        Returns:
        {"conicidade":bool}
        """
        if(self.bambu.Conicidade() <=1):
            return({"conicidade":True})
        else:
            return({"conicidade":False})
    
    def EsbeltezMax(self)->dict:
        """Verifica se a esbeltez está dentro do limite <150
        returns:
        {"esbeltez":bool}
        """
        if(self.bambu.Esbeltez() <= 150):
            return({"esbeltez":True})
        else:
            return({"esbeltez":False})


