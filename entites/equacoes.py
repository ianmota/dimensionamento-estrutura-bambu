import math as m

def esbeltezMaxima(lo:float,I:float,A:float)->float:
    i = (I/A)**(1/2)
    esbeltez = lo/i
    
    return(esbeltez)

def esforcoCalculo(nk):
    pass

def tensaoCompressao(nd,A):
    tensao = nd/A
    return(tensao)
    
def tensaoCalculo(kmod,fcok):
    ym = 1
    tensao = kmod*fcok/ym
    return(tensao)
    
def resistenciaTracao(fcok):
    rt = 1.3*fcok
    return(rt)

def resistenciaCortante(fcok):
    rc = 0.15*fcok
    return(rc)

def coeficienteResistencia(kmod1,kmod2,kmod3,kmod4):
    kmod = kmod1*kmod2*kmod3*kmod4
    return(kmod)
    
def kmod1(carga:str):
    pass

def diametroMedio(d1,d2):
    dm = (d1+d2)/2
    return(dm)

def espessuraMedia(t1,t2):
    tm = (t1+t2)/2
    return(tm)
    
def Media(*args):
    media=sum(args)/len(args)
    return(media)

def inerciaUnitaria(D,d):
    inercia = m.pi*(D**4-d**4)/64
    return(inercia)
    
def Area(D,d):
    area = m.pi(D**2-d**2)/4
    return(area)

def Conicidade(Dmax, Dmin, L):
    conicidade = 100*(Dmax-Dmin)/L
    return(conicidade)