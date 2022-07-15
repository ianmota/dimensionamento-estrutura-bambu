from adapters.colmoBambu import *

class Resistencia():
    def __init__(self,id:int,colmo_bambu:colmoDeBambu,p_fisica:str,umidade:str) -> None:
        """Determina as propriedades de cálculo do colmo
        Args:
            id (int): 
            colmo_bambu (colmoDeBambu):
            p_fisica (str):fc0k,ft0k,fv0k,ft90k,fmk
            umidade (str):ur<75;75<ur<85;saturado
        """
        self.id = id
        self.bambu = colmo_bambu
        self.p_fisica = p_fisica
        self.ur = umidade
        
    def __str__(self) -> str:
        return(f"R{self.id}({self.bambu},{self.fd()})")
    
    def __repr__(self) -> str:
        return(f"R{self.id}({self.bambu},{self.fd()})")
    
    def kmod(self)->float:
        """Calcula o coeficiente de majoração
        """
        kmod1 = tabelaCoeficientes["kmod1"]["permanente"]
        kmod2 = tabelaCoeficientes["kmod2"][self.ur]
        kmod3 = tabelaCoeficientes["kmod3"]
        return(kmod1*kmod2*kmod3)
    
    def ym(self)->float:
        """Calcula o coeficiente de minoração
        """
        return(tabelaCoeficientes["ym"][self.p_fisica])
    
    def fd(self) ->float:
        """Retorna a resistência de cálculo
        """
        if(self.p_fisica == "fc0k"):
            return(self.kmod()*self.bambu.p_fisicas.fco/self.ym())
        elif(self.p_fisica == "ft0k"):
            return(self.kmod()*self.bambu.p_fisicas.ft0()/self.ym())
        elif(self.p_fisica == "fv0k"):
            return(self.kmod()*self.bambu.p_fisicas.fv0k()/self.ym())
        elif(self.p_fisica == "ft90k"):
            return(self.kmod()*self.bambu.p_fisicas.fc90()/self.ym())
        elif(self.p_fisica == "fmk"):
            return(self.kmod()*self.bambu.p_fisicas.fm0()/self.ym())
    
    def ForcaEuler(self):
        fe =  (pi**2*self.bambu.p_fisicas.eb()*self.bambu.MomentoDeInercia())/self.bambu.L**2
        return(fe)

    def un_resistencia(self)->str:
        """Retorna a unidade em que a resistencia foi escrita 
        """
        return(self.bambu.p_fisicas.un)