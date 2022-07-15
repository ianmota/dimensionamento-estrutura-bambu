from adapters.dimensionamentoPilar import *
from services.verificacoesGeometricas import VerificacoesGeometricas
from services.verificacoesSeguranca import VerificacoesSeguranca


extremidade1 = Geometria(0,12,15,2,3,"cm")
extremidade2 = Geometria(1,11,14,3,4,"cm")

p_fisica = PropriedadesFisicas(0,50,"MPa")

colmo = colmoDeBambu(0,extremidade1,extremidade2,150,p_fisica)

resistencia = Resistencia(0,colmo,"fc0k","ur<75")

carregamento = Carregamento(0,100,"KN")

tensao = Tensoes(carregamento,resistencia)

dimensionamento = Dimensionamento(tensao)

print(dimensionamento)
print(f"{resistencia.fd()} {resistencia.un_resistencia()}")

vg = VerificacoesGeometricas(dimensionamento.tensao.resistencia_bambu.bambu) 
vs = VerificacoesSeguranca(tensao)
print(vg)
print(vs.fcd())

