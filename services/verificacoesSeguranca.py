from adapters.dimensionamentoPilar import *

class VerificacoesSeguranca():
    def __init__(self,dimensionamento:Dimensionamento) -> None:
        """Determina se o colmo indicado está resistindo aos esforços que são solicitados
        Args:
            id (int)
            carregamento (Carregamento)
            propriedades_fisicas (PropriedadesFisicas)
            calculo_elemento (ConsideracoesDeCalculo)
            bambu (colmoDeBambu)
        """
        self.dimensionamento = dimensionamento
        self.resistenciaBambu = self.dimensionamento.tensao.resistencia_bambu
    def __str__(self) -> str:
        return(f"segurança({self.Seguranca()})")
    
    def __repr__(self) -> str:
        return({"segurança":self.Seguranca(),"fcd":self.fcd()})
    
    def fcd(self) -> float:
        """Retorna a resistência máxima do colmo
        Returns:
            fcd(float):
        """
        fcd1 = self.resistenciaBambu.fd()
        fcd2 = min([fcd1,self.resistenciaBambu.ForcaEuler()/self.resistenciaBambu.bambu.Area()])
        
        if(self.dimensionamento.tensao.resistencia_bambu.bambu.Esbeltez()<=30):
            return(fcd1)
        elif(30<self.dimensionamento.tensao.resistencia_bambu.bambu.Esbeltez()<=150):
            return(fcd2)
    
    def Seguranca(self) -> dict:
        """Indica se o colmo em questão passa na verificação de segurança
        Returns:
            dict(bool)
        """
        if(self.dimensionamento.classificacaoPilar()<=self.fcd()):
            return({"segurança":True})
        else:
            return({"segurança":False})