from services.coeficientesRead import jsonRead 

coeficientes = "database/tabelaCoeficientes.json"
tabelaCoeficientes = jsonRead(coeficientes)
tabelaCoeficientesFisico = tabelaCoeficientes["rc"]

class PropriedadesFisicas():
    def __init__(self,id:int,resistencia_compressao:float,unidade:str) -> None:
        self.fco = resistencia_compressao
        self.id = id
        self.un = unidade
        
    def __repr__(self) -> dict:
        return({"Material":self.id,"fco":self.fco})
    
    def __str__(self) -> str:
        return(f"Material{self.id}-fco:{self.fco}")
    
    def resistenciaCisalhamentoParalela(self) -> float:
        """calcula a resistencia ao cisalhamento paralelo

        Returns:
            float: resistencia ao cisalhamento paralelo
        """
        rc = tabelaCoeficientesFisico["fv0"]*self.fco
        return(rc)
    
    def resistenciaTracaoParalela(self) -> float:
        """calcula a resistencia a tracao paralela

        Returns:
            float: resistencia a tração paralela
        """
        rt = tabelaCoeficientesFisico["ft0"]*self.fco
        return(rt)
    
    def resistenciaCompressaoPerpendicular(self) -> float:
        """calcula a resistencia a compressao perpendicular

        Returns:
            float: resistencia a compressão perpendicular
        """
        rc = tabelaCoeficientesFisico["fc90"]*self.fco
        return(rc)
    
    def resistenciaFlexao(self) -> float:
        """calcula a resistencia a flexao

        Returns:
            float: resistencia a flexao
        """
        rm = tabelaCoeficientesFisico["fmo"]*self.fco
        return(rm)
    
    def elasticidadeCompressaoParalela(self) -> float:
        """calcula a resistencia a compressao paralela

        Returns:
            float: elasticidade a compressao paralela
        """
        e = tabelaCoeficientesFisico["eb"]*self.fco
        return(e)