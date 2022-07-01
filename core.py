from adapters.colmoBambu import *
from services.verificacoesNormativas import * 

#definição da unidade
unit = "cm"

#definição das extremidades
extremidade1 = Geometria(1,12,15,2,3,unit)
extremidade2 = Geometria(2,11,14,3,4,unit)
#definição do colmo

colmo1 = colmoDeBambu(1,extremidade1,extremidade2,150)

#verificações
v1 = VerificacoesGeometricas(1)
print(v1.BarraPrismatica(colmo1.DiametroExterno(),colmo1.L))
print(v1.Conicidade(colmo1.Conicidade()))
print(v1.EsbeltezMaxima(colmo1.Esbeltez()))
print(v1.DefinicaoPilarEsbeltez(colmo1.Esbeltez()))

#resultados do colmo
print(f"conicidade: {colmo1.Conicidade()}")
print(f"D: {colmo1.DiametroExterno()}")
print(f"d: {colmo1.DiametroInterno()}")
print(f"A: {colmo1.Area()}")
print(f"I: {colmo1.MomentoDeInercia()}")
print(f"e: {colmo1.Esbeltez()}")
print(f"t: {colmo1.Espessura()}")