from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *

class JanelaInicio(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.teste_texto = Texto(self.root,"Teste")
        self.teste_texto.pack(side=TOP)
        
        self._teste_texto_2 = Texto_Infos(self.root,'Teste','Fazendo um teste','treino.png')
        self._teste_texto_2.Frame.pack(side=TOP)
        
        
        lista = ['Arroz','Feijao','Salada']
        self.teste_2 = Texto_Seleciona(self.root,"Selecione:",lista,bg_lista=cor_fundo,fg_lista=cor_fontes_claras,font_lista=fonte_Textos_9,width=5)
        self.teste_2.Frame.pack(side=TOP)
        
        self.abas = Abas(self.root)
        
        self.aba_infos = Frame(self.abas)
        self.aba_infos.configure(
            background=preto_fosco, 
        )
        
        self.abas.add(self.aba_infos, text="Informações")
        
        self.teste_1 = Texto_Imagem(self.aba_infos,'Outro Teste','maquina.png')
        self.teste_1.Frame.pack(side=TOP)
        
        
        self.abas.place(relx=0,rely=0.5,relheight=0.3,relwidth=1)
        
        self.root.mainloop()
    
        
        
root = Tk()
JanelaInicio(root)