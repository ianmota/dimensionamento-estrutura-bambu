from adapters.colmoBambu import *
from services.verificacoesGeometricas import * 
from adapters.dimensionamentoBambu import * 
from services.verificacoesSeguranca import *

#definição da unidade
unit = "cm"

#definição das extremidades
extremidade1 = Geometria(1,12,15,2,3,unit)
extremidade2 = Geometria(2,11,14,3,4,unit)

#propriedade física
fisica1 = PropriedadesFisicas(1,50,"Mpa")
#definição do colmo

colmo1 = colmoDeBambu(1,extremidade1,extremidade2,150,fisica1)

carregamento1 = Carregamento(0,150,"permanente","ur<75","N")

dimensionamento1 = DimensionamentoSimples(carregamento1,colmo1)

v2 = VerificacoesSeguranca(carregamento1,colmo1,dimensionamento1)
#verificações
v1 = VerificacoesGeometricas(1)
print(v1.BarraPrismatica(colmo1.DiametroExterno(),colmo1.L))
print(v1.Conicidade(colmo1.Conicidade()))
print(v1.EsbeltezMaxima(colmo1.Esbeltez()))
print(v1.ClassificacaoPilar(colmo1.Esbeltez()))
print(v2.ResistenciaCompressao())
print(v2.PilarCurto())
#resultados do colmo
print(f"conicidade: {colmo1.Conicidade()}")
print(f"D: {colmo1.DiametroExterno()}")
print(f"d: {colmo1.DiametroInterno()}")
print(f"A: {colmo1.Area()}")
print(f"I: {colmo1.MomentoDeInercia()}")
print(f"e: {colmo1.Esbeltez()}")
print(f"t: {colmo1.Espessura()}")

#resultados do dimensionamento
print(f"Tensão normal: {dimensionamento1.PilarCurto()}")
print(f"kmod: {carregamento1.kmod()}")
