def BarraPrismatica(D:float,L:float,parametro)->bool:
        """Verifica se o colmo com as dimensões D e L pode ser considerado como prismático

        Args:
        D (float): diâmetro
        L (float): comprimento

        Returns:
        bool: pode ser / não pode ser
        """
        if(65*D <= L):
            return(parametro)
        
        else:
            return("A barra não pode ser tratada como prismática, 65*D > L")
        
        