from adapters.colmoBambu import *
from services.verificacoesGeometricas import * 
from adapters.consideracoesCalculo import * 
from services.verificacoesSeguranca import *

#definição das extremidades
unit = "cm"
extremidade1 = Geometria(0,12,15,2,3,unit)
extremidade2 = Geometria(1,11,14,3,4,unit)

#propriedade física
fisica1 = PropriedadesFisicas(1,50,"Mpa")

#definição do colmo
colmo1 = colmoDeBambu(1,extremidade1,extremidade2,150,fisica1)

#definição do carregamento
carregamento1 = Carregamento(0,150,"permanente","ur<75","N",50,"fc0k")

dimensionamento1 = ConsideracoesDeCalculo(carregamento1,colmo1)

#resultados do colmo
print(f"conicidade: {colmo1.Conicidade()}")
print(f"D: {colmo1.DiametroExterno()}")
print(f"d: {colmo1.DiametroInterno()}")
print(f"A: {colmo1.Area()}")
print(f"I: {colmo1.MomentoDeInercia()}")
print(f"e: {colmo1.Esbeltez()}")
print(f"t: {colmo1.Espessura()}")

#resultados do dimensionamento
print(f"Tensão normal: {dimensionamento1.FlexaoNormal()}")
print(f"kmod: {carregamento1.kmod()}")

verificacao1 = VerificacoesGeometricas(0,colmo1)
print(verificacao1.ComprimentoMax())
print(verificacao1.ConicidadeMax())
print(verificacao1.EsbeltezMax())