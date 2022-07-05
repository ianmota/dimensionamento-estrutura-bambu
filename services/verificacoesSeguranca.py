from adapters.colmoBambu import *
from adapters.dimensionamentoBambu import *
from entites.carregamento import *
coeficientes = jsonRead("database/tabelaCoeficientes.json")

class VerificacoesSeguranca():
    def __init__(self,kmod:Carregamento,fcok:colmoDeBambu,tensao:DimensionamentoSimples) -> None:
        self.kmod = kmod.kmod()
        self.fcok = fcok.fcok
        self.tensaoPilarCurto = tensao.PilarCurto()
    
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def ResistenciaCompressao(self):
        resistencia = self.kmod*self.fcok/coeficientes["ym"]["fc0k"]
        return(resistencia)
    
    def PilarCurto(self):
        if self.tensaoPilarCurto <= self.ResistenciaCompressao():
            return(f"O pilar resiste aos esforços: {self.tensaoPilarCurto} <= {self.ResistenciaCompressao()}")
        else:
            return(f"O pilar entra em colapso: {self.tensaoPilarCurto}> {self.ResistenciaCompressao()}")