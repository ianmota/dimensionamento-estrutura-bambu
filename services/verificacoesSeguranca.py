from adapters.colmoBambu import colmoDeBambu
from adapters.consideracoesCalculo import *
from entites.carregamento import *
coeficientes = jsonRead("database/tabelaCoeficientes.json")

class VerificacoesSeguranca():
    def __init__(self,id:int,carregamento:Carregamento,propriedades_fisicas:PropriedadesFisicas,calculo_elemento:ConsideracoesDeCalculo,bambu:colmoDeBambu) -> None:
        """Determina se o colmo indicado está resistindo aos esforços que são solicitados
        Args:
            id (int)
            carregamento (Carregamento)
            propriedades_fisicas (PropriedadesFisicas)
            calculo_elemento (ConsideracoesDeCalculo)
            bambu (colmoDeBambu)
        """
        self.id = id
        self.carregamento = carregamento
        self.propriedadesFisicas = propriedades_fisicas
        self.calculo = calculo_elemento
        self.bambu = bambu
    
    def __str__(self) -> str:
        return(f"segurança({self.Seguranca()})")
    
    def __repr__(self) -> str:
        return({"segurança":self.Seguranca(),"fcd":self.fcd()})
    
    def fcd(self) -> float:
        """Retorna a resistência máxima do colmo
        Returns:
            fcd(float):
        """
        fcd1 = self.carregamento.kmod()*self.propriedadesFisicas.fco/coeficientes["ym"][self.carregamento.resistencia]  
        fcd2 = min([fcd1,self.calculo.ForcaEuler()/self.bambu.Area()])
        
        if(self.bambu.Esbeltez()<=30):
            return(fcd1)
        elif(30<self.bambu.Esbeltez()<=150):
            return(fcd2)
    
    def Seguranca(self) -> dict:
        """Indica se o colmo em questão passa na verificação de segurança
        Returns:
            dict(bool)
        """
        if(self.bambu.Esbeltez()<=30):
            
            if(self.calculo.TensaoNormal()<=self.fcd()):
                return({"segurança":True})
            else:
                return({"segurança":False})
        elif(30<self.bambu.Esbeltez()<=150):
            if(self.calculo.FlexaoNormal()<=self.fcd()):
                return({"segurança":True})
            else:
                return({"segurança":False})