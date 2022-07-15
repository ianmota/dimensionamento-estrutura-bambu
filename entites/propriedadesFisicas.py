from services.coeficientesRead import jsonRead 

coeficientes = "database/tabelaCoeficientes.json"
tabelaCoeficientes = jsonRead(coeficientes)
tabelaCoeficientesFisico = tabelaCoeficientes["rc"]

class PropriedadesFisicas():
    def __init__(self,id:int,fco:float,unidade:str) -> None:
        """Determina as propriedades físicas e do material do colmo de bambu
        """
        self.fco = fco
        self.id = id
        self.un = unidade
        
    def __repr__(self) -> dict:
        return(f"M{self.id}({self.fco},{self.eb()}) {self.un}")
    
    def __str__(self) -> str:
        return(f"M{self.id}({self.fco},{self.eb()}) {self.un}")
    
    def fv0k(self) -> float:
        """calcula a resistencia ao cisalhamento paralelo
        Returns:
            resistencia ao cisalhamento paralelo(float)
        """
        rc = tabelaCoeficientesFisico["fv0"]*self.fco
        return(rc)
    
    def ft0(self) -> float:
        """calcula a resistencia a tracao paralela
        Returns:
            resistencia a tração paralela(float)
        """
        rt = tabelaCoeficientesFisico["ft0"]*self.fco
        return(rt)
    
    def fc90(self) -> float:
        """calcula a resistencia a compressao perpendicular
        Returns:
            resistencia a compressão perpendicular(float)
        """
        rc = tabelaCoeficientesFisico["fc90"]*self.fco
        return(rc)
    
    def fm0(self) -> float:
        """calcula a resistencia a flexao
        Returns:
            resistencia a flexao(float)
        """
        rm = tabelaCoeficientesFisico["fmo"]*self.fco
        return(rm)
    
    def eb(self) -> float:
        """calcula a resistencia a compressao paralela
        Returns:
            elasticidade a compressao paralela(float)
        """
        e = tabelaCoeficientesFisico["eb"]*self.fco
        return(e)

