class Carregamento():
    def __init__(self,id:int,nd:float,unidade:str,m1d:float=0,ng:float=0,nq:float=0) -> None:
        """insere os dados de um determinado carregamento
        Args:
            id (int)
            nd (float)
            unidade (str)
            m1d (float, optional)
            ng (float, optional)
            nq (float, optional)
        """
        self.id = id
        self.nd = nd
        self.carga_permanente = ng
        self.carga_acidental = nq
        self.unidade = unidade
        self.m1d = m1d

        
    def __str__(self) -> str:
        return(f"C{self.id}({self.nd} {self.unidade},{self.carga_permanente} {self.unidade},{self.carga_acidental} {self.unidade},{self.m1d} {self.unidade}(medida)) ")
    
    def __repr__(self) -> str:
        return(f"C{self.id}({self.nd} {self.unidade},{self.carga_permanente} {self.unidade},{self.carga_acidental} {self.unidade},{self.m1d} {self.unidade}(medida)) ")


    

    
    
        