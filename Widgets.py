"""
ESTILO DOS WIDGETS
"""
from Cores import *
from Fontes import *
from tkinter import *
from tkinter import ttk, END, INSERT
from PIL import Image, ImageTk
from Imagem import redimensionar
from Mensagens import Mensagem_Erro


class Botao(Button):
    def __init__(self,master,texto,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Mediana_14
        
        self.configure(
            text = texto,
            bg = bg,
            fg = fg,
            font = font,
            relief= FLAT
        )
            
class Texto(Label):
    def __init__(self,master,texto,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Mediana_14    
        
        self.configure(
            text = texto,
            bg = bg,
            fg = fg,
            font = font
        )
        
class Entrada(Entry):
    def __init__(self,master,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        width = args.get('width')
        
        if not bg:
            bg = cor_entradas
        
        if not fg:
            fg = cor_fontes_escuras
            
        if not font:
            font = fonte_Textos_12 
        
        if not width:
            width = 15
            
        self.configure(
            font = font,
            bg = bg,
            fg = fg,
            insertbackground = cor_fontes_escuras,
            width = width
        )
        
    def formato_de_telefone(self,event = None):
        texto = self.get().replace("(", "").replace(")","").replace("-", "")[:11]
        novo_texto = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(texto)):
            
            if not texto[index] in "0123456789": continue

            if index == 0: novo_texto += "(" + texto[index] 
            elif index == 1: novo_texto += texto[index] + ")"
            elif index == 6: novo_texto += texto[index] + "-"
            else: novo_texto += texto[index]

        self.delete(0, "end")
        self.insert(0, novo_texto)

    def formato_de_data(self,event = None):
        
        texto = self.get().replace("/", "")[:8]
        novo_texto = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(texto)):
            
            if not texto[index] in "0123456789": continue

            if index == 1: novo_texto +=  texto[index] + "/" 
            elif index == 3: novo_texto += texto[index] + "/"
            else: novo_texto += texto[index]

        self.delete(0, "end")
        self.insert(0, novo_texto)

class Entrada_Texto:
    def __init__(self,master,texto,**args):
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        width = args.get('width')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Mediana_14
            
        if not width:
            width = 15
        
        self.Frame = Frame(master)
        self.Frame.configure(
            bg=bg
        )
        
        self.texto = Texto(self.Frame,texto,bg=bg,fg=fg,font=font)
        self.entrada = Entrada(self.Frame,width=width)
        
        self.texto.pack(side=LEFT,padx=5,anchor='e')
        self.entrada.pack(side=RIGHT,anchor='w')

class Botao_Check(Checkbutton):
    def __init__(self,master,texto,variavel,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        selectcolor = args.get('selectcolor')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Textos_12 
        
        if not selectcolor:
            selectcolor = cor_fundo
        
        self.configure(
            text= texto,
            bg=bg,
            fg=fg,
            font=font,
            selectcolor=selectcolor,
            var = variavel
        )

class Botao_Imagem(Button):
    def __init__(self,master,txt,dir_img,**args):
        super().__init__(master=master)
        
        dir_img = 'Icones\\' + dir_img
        self.img = redimensionar(dir_img,20,20)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        width = args.get('width')
        height = args.get('height')
        
        if not bg:
            bg = cor_frames
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Mediana_14 
        
        if not width:
            width = 150
        
        if not height:
            height = 25

        
        self.configure(
            text=txt,
            image=self.img,
            width=width,
            height=height,
            bg=bg,
            fg=fg,
            font=font,
            compound=LEFT,
            padx=30,            
        )
        
class Botao_Radio(Radiobutton):
    def __init__(self,master,texto,variavel,valor,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        selectcolor = args.get('selectcolor')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
            
        if not font:
            font = fonte_Textos_12 
        
        if not selectcolor:
            selectcolor = cor_fundo
        
        self.configure(
            text= texto,
            bg=bg,
            fg=fg,
            font=font,
            selectcolor=selectcolor,
            var = variavel,
            value=valor
        )

class Texto_Imagem:
    def __init__(self,master,texto,dir_img,**args):
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        x = args.get('x')
        y = args.get('y')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_claras
        
        if not font:
            font = fonte_Mediana_14
            
        if not x:
            x = 30
            
        if not y:
            y = 30
            
        
        self.Frame = Frame(master)
        self.Frame.configure(
            bg=bg
        )
        
        dir_img = 'Icones\\' + dir_img
        self.img = redimensionar(dir_img,x,y)
        self.imagem = Label(self.Frame)
        self.imagem.configure(
            image=self.img,
            bg=bg,
        )
        
        self.txt = Texto(self.Frame,texto,bg=bg,fg=fg,font=font)
        
        self.imagem.pack(side=LEFT,padx=5)
        self.txt.pack(side=LEFT)
                
class Texto_Infos:
    def __init__(self,master,texto_principal,texto_secundario,dir_img,**args):
        
        bg = args.get('bg')
        fg_1 = args.get('fg_1')
        fg_2 = args.get('fg_2')
        font_1 = args.get('font_1')
        font_2 = args.get('font_2')
        x = args.get('x')
        y = args.get('y')
        
        if not bg:
            bg = cor_fundo
        
        if not fg_1:
            fg_1 = cor_fontes_claras
        
        if not fg_2:
            fg_2 = cor_cabecalhos
        
        if not font_1:
            font_1 = fonte_Mediana_16
        
        if not font_2:
            font_2 = fonte_Textos_9
            
        if not x:
            x = 35
            
        if not y:
            y = 35
            
        self.Frame = Frame(master)
        self.Frame.configure(
            bg=bg
        )
        
        dir_img = 'Icones\\' + dir_img
        self.Imagem = redimensionar(dir_img,x,y)
        self.Label_Imagem = Label(self.Frame)
        self.Label_Imagem.configure(
            image=self.Imagem,
            bg=bg,
        )
        
        self.Texto_Principal = Label(self.Frame)
        self.Texto_Principal.configure(
            text=texto_principal,
            bg=bg,
            fg=fg_1,
            font=font_1
        )
        self.Texto_Secundario = Label(self.Frame)   
        self.Texto_Secundario.configure(
            text=texto_secundario,
            bg=bg,
            fg=fg_2,
            font=font_2
        )     
        
        self.Label_Imagem.pack(side=LEFT,padx=5)
        self.Texto_Secundario.pack(side=TOP,anchor='w')
        self.Texto_Principal.pack(side=TOP,anchor='w')
    
class Lista_Selecao(ttk.Combobox):
    
    def __init__(self,master,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        fg = args.get('fg')
        font = args.get('font')
        width = args.get('width')
        
        if not bg:
            bg = cor_entradas
        
        if not fg:
            fg = cor_fontes_escuras
            
        if not font:
            font = fonte_Textos_12 
        
        if not width:
            width = 15
        
        self.configure(
            font = font,
            background = bg,
            foreground = fg,
            width=15 
        )
        
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", 
                        fieldbackground= bg,
                        foreground= fg,
                        relief="flat",
                        )
        
    def set_completion_list(self, completion_list):
        
        # Ordenar a Lista
        self._completion_list = sorted(completion_list, key=str.lower) 
        self._hits = []
        self._hit_index = 0
        self.position = 0
        
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list  

    def autocomplete(self, delta=0):
        
        #autocompleta o Combobox, delta pode ser 0/1/-1 para percorrer possíveis acertos

        if delta: # precisa excluir a seleção, caso contrário, fixaríamos a posição atual
            self.delete(self.position, END)
        else: # defina a posição para  que a seleção comece onde a entrada de texto terminou
            self.position = len(self.get())
                
        # coletar hits
        _hits = []
        
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()): # Corresponder maiúsculas e minúsculas
                _hits.append(element)
                        
        # se tivermos uma nova lista de ocorrências
        if _hits != self._hits:
            self._hit_index = 0
            self._hits=_hits
                
        # só permitir ciclismo se estivermos em uma lista de acertos conhecida
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
                
        # agora, finalmente, execute a completaçao automática
        if self._hits:
            self.delete(0,END)
            self.insert(0,self._hits[self._hit_index])
            self.select_range(self.position,END)


    def handle_keyrelease(self, event):
        
        #manipulador de eventos para o evento keyrelease neste widge
        if event.keysym == "BackSpace":
            self.delete(self.index(INSERT), END)
            self.position = self.index(END)
                
        if event.keysym == "Left":
            if self.position < self.index(END): # deleta a selecao
                self.delete(self.position, END)
            else:
                self.position = self.position-1 # deleta um caracter
                self.delete(self.position, END)
                    
        if event.keysym == "Right":
            self.position = self.index(END) # vai para o final (sem selecao)
                
        # lista na posição do autocompletar
        if len(event.keysym) == 1:
            self.autocomplete()

class Texto_Seleciona:
    def __init__(self,master,texto,lista,**args):
        
        bg = args.get('bg')
        bg_lista = args.get('bg_lista')
        fg = args.get('fg')
        fg_lista = args.get('fg_lista')
        font = args.get('font')
        font_lista = args.get('font_lista')
        width = args.get('width')
        
        if not bg:
            bg = cor_fundo
        
        if not bg_lista:
            bg_lista = cor_entradas
        
        if not fg:
            fg = cor_fontes_claras
        
        if not fg_lista:
            fg_lista = cor_fontes_escuras
            
        if not font:
            font = fonte_Mediana_14 
        
        if not font_lista:
            font_lista = fonte_Textos_12 
        
        if not width:
            width = 15
            
        self.Frame = Frame(master)
        self.Frame.configure(
            bg=cor_fundo
        )
        
        self.txt = Texto(self.Frame,texto,bg=bg,fg=fg,font=font)
        
        self.Lista = Lista_Selecao(self.Frame,bg=bg_lista,fg=fg_lista,font=font_lista,width=width)
        self.Lista.set_completion_list(lista)
        
        self.txt.pack(side=LEFT,padx=5)
        self.Lista.pack(side=RIGHT)

class Abas(ttk.Notebook):
    def __init__(self,master,**args):
        super().__init__(master=master)
        
        bg = args.get('bg')
        field = args.get('field')
        fg = args.get('fg')
        
        if not bg:
            bg = cor_fundo
        
        if not fg:
            fg = cor_fontes_escuras
            
        if not field:
            field = cor_cabecalhos 
            
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", 
                        fieldbackground= field,
                        foreground= fg,
                        background = bg,
                        relief="flat",
                        )
     
class Tabela:
    def __init__(self,master,colunas,qtd_linhas=15,largura=100,lar_min=100):
        
        self.estilizar()
        
        self.Colunas = colunas
        self.Largura = largura
        self.Altura = qtd_linhas
        self.UltimaLinha = 0
        
        self.Listagem = ttk.Treeview(master,columns = self.Colunas,show='headings', height = qtd_linhas, selectmode='browse',style="myStyle.Treeview")
        
        for new in self.Colunas:
            if new == 'ID':
                self.Listagem.column(str(new), width = 20, minwidth=20)
            else:
                self.Listagem.column(str(new), width = largura, minwidth=lar_min,anchor='center')
            
            self.Listagem.heading(str(new),text=str(new))
            
            
        #BARRAS DE ROLAGEM DA VISUALIZACAO
        self.Barra_Y= ttk.Scrollbar(master, orient=VERTICAL,command=self.Listagem.yview)
        self.Barra_X = ttk.Scrollbar(master, orient=HORIZONTAL,command=self.Listagem.xview)

        self.Listagem.configure(yscroll = self.Barra_Y.set)
        self.Listagem.configure(xscroll = self.Barra_X.set)

        # TEXTOS DOS CABEÇALHO
        for c in self.Colunas:
            self.Listagem.heading(str(c), text=str(c))
        
        self.Infos = []

    def Inserir(self,lista):
        
        # INSRINDO OS ITENS
        try:
            for i in lista:
                item = tuple(i)
                if self.UltimaLinha%2 == 0:
                    self.Listagem.insert('','end', values=item,tags = ('par',))
                else:
                    self.Listagem.insert('','end', values=item,tags = ('impar',))
                self.UltimaLinha += 1
                
            self.Listagem.tag_configure('par', background='#D9D9D9')
            self.Listagem.tag_configure('impar', background='#A5A5A5')
            
        except:
            Mensagem_Erro('Houve algum problema ao inserir itens na tabela!')
    
    def estilizar(self):
        
        #CONFIGURAR ESTILO
        self.style = ttk.Style()
        self.style.theme_use('alt')
        """
        self.style.configure("myStyle.Treeview",
                fieldbackground=preto_fosco,
                foreground=cor_fontes_claras,
                background=cor_frames,
                bordercolor=verde_suave,
                font=fonte_Textos_12,
                rowheight=25,
                relief="flat",
                highlightthickness=2, 
                bd=2,
                )
        """
        self.style.configure("myStyle.Treeview.Heading",
                        foreground=cor_fontes_claras,
                        background=cor_frames,
                        )

        
        self.style.layout("myStyle.Treeview", [
                    ('myStyle.Treeview.treearea', {'sticky': 'nswe'})])
      
        
