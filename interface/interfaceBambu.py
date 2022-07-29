import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from adapters.dimensionamentoPilar import *
from services.verificacoesGeometricas import VerificacoesGeometricas
from services.verificacoesSeguranca import VerificacoesSeguranca

class Application(Dimensionamento,VerificacoesGeometricas,VerificacoesSeguranca):
    def __init__(self) -> None:
        self.root = tk.Tk()
        
        self.root.title('Dimensionamento de Pilar de Bambu')
        self.root.configure(background='light blue')
        self.root.geometry('700x570')
        self.root.resizable(False, False)
        self.LabelsJanela01()
        self.ButonsJanela01()
        
        self.root.mainloop()
        
    def LabelsJanela01(self):
        
        # Títulos da página
        Titulo01 = tk.Label(self.root, fg="#05677F", bg="light blue", text='BambuCalc', width=15, height=2, padx=2, font=('Ivy 40 bold'), justify='center')
        Titulo01.place(relx=0.150, rely=0.200)

        Titulo2 = tk.Label(self.root, fg="black", bg="light blue", text='Por:', width=10, height=2, padx=2, font=('Ivy 15 bold'), justify='center')
        Titulo2.place(relx=0.420, rely=0.370)

        # Descrição da página
        labelKarla = tk.Label(self.root, bg="light blue", font=('Ivy 12 bold'), fg="black", text="Antônia Karla")
        labelKarla.place(relx=0.430, rely=0.440)

        labelKarla_curriculo = tk.Label(self.root, bg="light blue", width=30, font=('Ivy 9 bold'), fg="black", text="Graduanda em Engenheira Civil - IFS ")
        labelKarla_curriculo.place(relx=0.350, rely=0.480)

        labelAdysson = tk.Label(self.root, bg="light blue", font=('Ivy 12 bold'), fg="black", text="Adysson André")
        labelAdysson.place(relx=0.420, rely=0.520)

        labelAdysson_curriculo = tk.Label(self.root, bg="light blue", width=30, font=('Ivy 9 bold'), fg="black", text="Mestre em Engenharia Civil ")
        labelAdysson_curriculo.place(relx=0.350, rely=0.565)

        labelIan = tk.Label(self.root, bg="light blue", font=('Ivy 12 bold'), fg="black", text="Ian Mota")
        labelIan.place(relx=0.460, rely=0.605)

        labelIan_curriculo = tk.Label(self.root, bg="light blue", width=30, font=('Ivy 9 bold'), fg="black", text="Graduando em Engenheira Civil - IFS ")
        labelIan_curriculo.place(relx=0.350, rely=0.645)

    def ButonsJanela01(self):
        botao_IniciarCalculo = tk.Button(self.root,command=lambda:[self.HideRoot(),self.OpenRoot2() ], bg="#05677F", font=('Ivy 12 bold'), fg="black", text="INICIAR O CÁLCULO")
        botao_IniciarCalculo.place(relx=0.350, rely=0.850, relwidth=0.30, relheight=0.085)
    
    def ReopenRoot(self):
        self.root.destroy()
        self.root2.destroy()
    
    def ReopenRoot2(self):
        self.root2.deiconify()
        self.root3.destroy()
        
    def OpenRoot2(self):
        self.root2 = tk.Toplevel()
        self.root2.title('Dimensionamento de Pilar de Bambu')
        self.root2.configure(background='light blue')
        self.root2.geometry('700x570')
        self.root2.resizable(False, False)
        self.root2.protocol('WM_DELETE_WINDOW', self.ReopenRoot)
        
        self.LabelsJanela02()
        self.EntrysJanela02()
        self.ButtonsJanela02()
        
        self.root2.mainloop()
        
    def LabelsJanela02(self):
        
        label_Titulo01 = tk.Label(self.root2, bg='light blue', fg='black', text='DIMENSIONAMENTO E SEGURANÇA DE PILAR DE BAMBU', width=52, height=2, padx=25, font=('Ivy 11 bold'), justify='center')
        label_Titulo01.place(relx=0.120, rely=0.020)
        
        label_DMAIOR = tk.Label(self.root2, bg='light blue', fg='black', text='Diâmetro externo maior (cm) :', width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_DMAIOR.place(relx=0.050, rely=0.15)

        label_DMENOR = tk.Label(self.root2, bg='light blue', fg='black', text='Diâmetro externo menor (cm) :', width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_DMENOR.place(relx=0.053, rely=0.22)
        
        label_L = tk.Label(self.root2, bg='light blue', fg='black', text=' Comprimento do bambu (cm) :',
                            width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_L.place(relx=0.050, rely=0.28)

        label_EMAIOR = tk.Label(self.root2, bg='light blue', fg='black', text=' Espessura maior (cm) :',
    width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_EMAIOR.place(relx=0.042, rely=0.34)

        label_EMENOR = tk.Label(self.root2, bg='light blue', fg='black', text=' Espessura menor (cm) :',
    width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_EMENOR.place(relx=0.042, rely=0.40)
        
        label_CARREGAMENTO_PROJETO= tk.Label(self.root2, bg='light blue', fg='black', text='Carga de projeto (kN) :',
                          width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_CARREGAMENTO_PROJETO.place(relx=0.042, rely=0.46)
        
        label_CARREGAMENTO_PERMANENTE= tk.Label(self.root2, bg='light blue', fg='black', text='Carga permanente (kN) :',
                          width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_CARREGAMENTO_PERMANENTE.place(relx=0.042, rely=0.58)

        label_CARREGAMENTO_ACIDENTAL= tk.Label(self.root2, bg='light blue', fg='black', text='Carga acidental (kN) :',
                          width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_CARREGAMENTO_ACIDENTAL.place(relx=0.042, rely=0.64)
        
        label_tipodecarregamento = tk.Label(self.root2, bg='light blue', fg='black', text='Selecione o tipo de carregamento ',
                        width=30, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_tipodecarregamento.place(relx=0.042, rely=0.75)
        
        label_fc0k = tk.Label(self.root2, bg='light blue', fg='black', text='fc0,k(kN/cm²) :',width=25, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_fc0k.place(relx=0.042, rely=0.52)
        
        label_umidaderelativa = tk.Label(self.root2, bg='light blue', fg='black', text='Selecione a umidade relativa do ambiente',width=35, height=2, padx=2, font=('Ivy 10 bold'), justify='center')
        label_umidaderelativa.place(relx=0.042, rely=0.83)
        
    def EntrysJanela02(self):
        
        self.DMAIOR = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.DMAIOR.place(relx=0.40, rely=0.17)
        
        self.DMAIOR2 = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.DMAIOR2.place(relx=0.55, rely=0.17)

        self.DMENOR = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.DMENOR.place(relx=0.40, rely=0.24)
        
        self.DMENOR2 = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.DMENOR2.place(relx=0.55, rely=0.24)

        self.L = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.L.place(relx=0.40, rely=0.30)

        self.EMAIOR = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.EMAIOR.place(relx=0.40, rely=0.36)

        self.EMAIOR2 = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.EMAIOR2.place(relx=0.55, rely=0.36)
        
        self.EMENOR = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.EMENOR.place(relx=0.40, rely=0.42)

        self.EMENOR2 = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.EMENOR2.place(relx=0.55, rely=0.42)
    
        self.CARREGAMENTO_PROJETO = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.CARREGAMENTO_PROJETO.place(relx=0.40, rely=0.48)

        self.CARREGAMENTO_PERMANENTE = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.CARREGAMENTO_PERMANENTE.place(relx=0.40, rely=0.6)

        self.CARREGAMENTO_ACIDENTAL = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.CARREGAMENTO_ACIDENTAL.place(relx=0.40, rely=0.65)
        
        self.fc0k = tk.Entry(self.root2, width=15, bg='white', justify='center')
        self.fc0k.place(relx=0.40, rely=0.54)
        
        self.TIPO_CARGA = tk.StringVar()
        self.TIPO_CARGA_BOX= Combobox(self.root2,width=40,textvariable=self.TIPO_CARGA)
        self.TIPO_CARGA_BOX ["values"]= ("Permanente","Longa duração (mais de seis meses)","Média duração (uma semana a seis meses)","Curta duração (até uma semana)","Instantânea")
        self.TIPO_CARGA_BOX.place(relx=0.05, rely=0.8)

        self.UMIDADE_VALUE = tk.StringVar()
        self.UMIDADE = Combobox(self.root2, width=40,textvariable=self.UMIDADE_VALUE)
        self.UMIDADE["values"] = ("ur<75","75<ur<85","saturado")
        self.UMIDADE.place(relx=0.05, rely=0.880)
    
    def ButtonsJanela02(self):
        
        self.LIMPAR = tk.Button(self.root2,command=self.CleanEntrys, fg="white", bg="#05677F",text='LIMPAR CAMPO ', width=15, height=1)
        self.LIMPAR.place(relx=0.738, rely=0.099)

        self.CALCULAR = tk.Button(self.root2, bg='#05677F', fg='white', font=('Ivy 10 bold'),justify='center', command=lambda:[self.HideRoot02(), self.OpenRoot03()], text='CALCULAR',width=12, height=1, padx=2)
        self.CALCULAR.place(relx=0.05, rely=0.925)

    def HideRoot(self):
        self.root.withdraw()
        
    def HideRoot02(self):
        self.root2.withdraw()
        
    def OpenRoot03(self):
        self.root3 = tk.Toplevel()
        self.root3.title('Resultados')
        self.root3.configure(background='light blue')
        self.root3.geometry('600x570')
        self.root3.resizable(False, False)
        self.root3.protocol('WM_DELETE_WINDOW', self.ReopenRoot2)
        self.Calcular()
        self.VerificarCarregamentos()
        self.LabelsJanela03()
        
    def CleanEntrys(self):
        self.DMAIOR.delete(0, tk.END)
        self.DMAIOR2.delete(0,tk.END)
        self.DMENOR.delete(0, tk.END)
        self.DMENOR2.delete(0,tk.END)
        self.L.delete(0, tk.END)
        self.EMAIOR.delete(0, tk.END)
        self.EMAIOR2.delete(0,tk.END)
        self.EMENOR.delete(0, tk.END)
        self.EMENOR2.delete(0,tk.END)
        self.CARREGAMENTO_PROJETO.delete(0, tk.END)
        self.CARREGAMENTO_PERMANENTE.delete(0,tk.END)
        self.CARREGAMENTO_ACIDENTAL.delete(0,tk.END)
        self.fc0k.delete(0, tk.END)
        
    def Calcular(self):
        
        g1 = Geometria(0,float(self.DMAIOR.get()),float(self.DMENOR.get()),float(self.EMAIOR.get()),float(self.EMENOR.get()),"cm")
        g2 = Geometria(1,float(self.DMAIOR2.get()),float(self.DMENOR2.get()),float(self.EMAIOR2.get()),float(self.EMENOR2.get()),"cm")
        p1 = PropriedadesFisicas(0,float(self.fc0k.get()),"kN/m²")
        self.c1 = colmoDeBambu(0,g1,g2,float(self.L.get()),p1)
        self.r1 = Resistencia(0,self.c1,"fc0k",self.UMIDADE_VALUE.get())
        self.ca1 = Carregamento(0,float(self.CARREGAMENTO_PROJETO.get()),"kN",ng=float(self.CARREGAMENTO_PERMANENTE.get()),nq=float(self.CARREGAMENTO_ACIDENTAL.get()))
        self.t1 = Tensoes(self.ca1,self.r1)
        self.d1 = Dimensionamento(self.t1)
        self.vg = VerificacoesGeometricas(self.c1)
        self.vs = VerificacoesSeguranca(self.d1)
    
    def LabelsJanela03(self):
        self.LabelConicidade()
        self.LabelPrismatico()
        self.LabelEsbeltez()
        self.LabelSegurança()
        self.LabelTensao()
        
    def LabelConicidade(self):
        
        label_conicidade_titulo = tk.Label(self.root3, bg='light blue', fg='black', text='Conicidade (%): ',width=35, height=2, padx=2, font=('Ivy 10 bold'), justify='left')
        label_conicidade_titulo.place(relx=0.01, rely=0.01)
        
        label_conicidade_value = tk.Label(self.root3, bg='light blue', fg='black', text= self.ResultadoConicidade() ,width=15, height=2, padx=2, font=('Ivy 10'), justify='left')
        label_conicidade_value.place(relx=0.4, rely=0.01)

    def LabelPrismatico(self):
        label_prismatico_titulo = tk.Label(self.root3, bg='light blue', fg='black', text='Prismatico (65*D > L): ',width=35, height=2, padx=2, font=('Ivy 10 bold'), justify='left')
        label_prismatico_titulo.place(relx=0.01, rely=0.06)

        label_prismatico_value = tk.Label(self.root3, bg='light blue', fg='black', text=self.ResultadoPrismatico(),width=15, height=2, padx=2, font=('Ivy 10'), justify='left')
        label_prismatico_value.place(relx=0.4, rely=0.06)
        
    def LabelEsbeltez(self):
        label_esbeltez_titulo = tk.Label(self.root3, bg='light blue', fg='black', text='Esbeltez: ',width=35, height=2, padx=2, font=('Ivy 10 bold'), justify='left')
        label_esbeltez_titulo.place(relx=0.01, rely=0.11)

        label_prismatico_value = tk.Label(self.root3, bg='light blue', fg='black', text=self.ResultadoEsbeltez(),width=15, height=2, padx=2, font=('Ivy 10'), justify='left')
        label_prismatico_value.place(relx=0.4, rely=0.11)
        
    def LabelSegurança(self):
        label_seguranca_titulo = tk.Label(self.root3, bg='light blue', fg='black', text='Segurança: ',width=35, height=2, padx=2, font=('Ivy 10 bold'), justify='left')
        label_seguranca_titulo.place(relx=0.01, rely=0.16)

        label_prismatico_value = tk.Label(self.root3, bg='light blue', fg='black', text=self.ResultadoSeguranca(),width=25, height=2, padx=2, font=('Ivy 10'), justify='left')
        label_prismatico_value.place(relx=0.32, rely=0.16)  
  
    def LabelTensao(self):
        label_tensao_resultado = tk.Label(self.root3, bg='light blue', fg='blue', text=self.TensaoNoColmo(),width=55, height=4, padx=2, font=('Ivy 14 bold'), justify='left')
        label_tensao_resultado.place(relx=0.05, rely=0.4)
        
    def ResultadoConicidade(self):
        if(self.vg.ConicidadeMax()['conicidade']):
            conicidade = float("{:.2f}".format(self.c1.Conicidade()))
            return(f"OK! {conicidade}% < 1%")
        else:
            return(f"ERRO! {conicidade}% > 1%")
        
    def ResultadoPrismatico(self):

        if(self.vg.ComprimentoMax()['prismatica']):
            return("OK! Colmo L < 65D")
        else:
            return("ERRO! Colmo L > 65D")
        
    def ResultadoEsbeltez(self):
        if(self.c1.Esbeltez()<=30):
            return("Pilar Curto")
        elif(30<self.c1.Esbeltez()<=70):
            return("Pilar Medio")
        elif(70<self.c1.Esbeltez()<=150):
            return("Pilar Esbelto")
        else:
            return("ERRO! Esbeltez > 150")
    
    def ResultadoSeguranca(self):
        fcd = float("{:.2f}".format(self.vs.fcd()))
        if(self.vs.Seguranca()['segurança']):
            return(f"OK! {fcd} > Esforço solicitante")
        else:
            return(f"ERRO! Colapso estrutural")
        
    def TensaoNoColmo(self):
        tensao = float("{:.2f}".format(self.d1.classificacaoPilar()))
        fcd = float("{:.2f}".format(self.vs.fcd()))
        
        if(self.vs.Seguranca()['segurança'] and self.vg.ComprimentoMax()['prismatica'] and self.vg.ConicidadeMax()['conicidade'] and self.vg.EsbeltezMax()['esbeltez']):
            
            return(f"O colmo PODE ser usado para suportar os esforços \
                   \n Tensão admissível: {fcd} > Tensão solicitante: {tensao}")
        else:
            if not self.vs.Seguranca()['segurança']:
                return(f"O colmo NÃO PODE ser usado para suportar os esforços \
                       \n Tensão admissível: {fcd} < Tensão solicitante: {tensao}")
            if not self.vg.ComprimentoMax()['prismatica']:
                return(f"O colmo NÃO PODE ser usado para suportar os esforços \
                       \n Comprimento: {self.L} > Comprimento máximo: {65*self.c1.DiametroExterno()}")

    def VerificarCarregamentos(self):
        if(self.c1.Esbeltez() > 70):
            ng = self.CARREGAMENTO_PERMANENTE.get()
            nq = self.CARREGAMENTO_ACIDENTAL.get()
            if( not ng or not nq):
                messagebox.askquestion("Omissão de carregamentos","Seu colmo é esbelto, é necessário inserir a carga permanente e acidental (por fora)","OK")
            