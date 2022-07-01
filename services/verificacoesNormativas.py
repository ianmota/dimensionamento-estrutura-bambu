class VerificacoesGeometricas():
    def __init__(self,id:int) -> None:
        self.id = id
    
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    def BarraPrismatica(self,D:float,L:float)->bool:
        """Verifica se o colmo com as dimensões D e L pode ser considerado como prismático

        Args:
        D (float): diâmetro
        L (float): comprimento

        Returns:
        bool: pode ser / não pode ser
        """
        if(L <= 65*D):
            return(f"A barra pode ser tratada como prismática: {L} < {65*D} ")
        
        else:
            return(f"A barra não pode ser tratada como prismática: {65*D} > {L}")

    def Conicidade(self,conicidade:float):
        if(conicidade<=1):
            return(f"A barra pode ser usada como elemento estrutural, conicidade:{conicidade} < 1 ")
        else:
            return(f"A barra não pode ser usada como elemento estrutural, conicidade:{conicidade} > 1 ")
    
    def EsbeltezMaxima(self,esbeltez:float):
        if(esbeltez<= 150):
            return(f"A esbeltez está dentro do limite permitido: {esbeltez}<=150")
        else:
            return(f"A esbeltez está fora do limite permitido: {esbeltez}>150")

    def DefinicaoPilarEsbeltez(self, esbeltez):
        if(esbeltez<=30):
            return({"Pilar curto":1})
        elif(30<=esbeltez<=70):
            return({"Pilar médio":2})
        elif(70<=esbeltez<=150):
            return({"Pilar esbelto":3})
    