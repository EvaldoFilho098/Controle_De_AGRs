"""
MENSAGENS
"""

from tkinter import messagebox

def Mensagem_Sim_Nao(txt):
    """Caixa de mensagem na tela, fazendo uma pergunta de sim ou não

    Args:
        txt (str): Texto a ser exibido na caixa de mensagem

    Returns:
        boolean: retorna True caso a resposta seja "Sim", e retorna False caso a resposta sejã "Não"
    """
    return messagebox.askyesno(title="Aviso!", message=txt )

def Mensagem_Concluida(txt=''):
    """Caixa de mensagem na tela avisando que algo foi concluído com sucesso

    Args:
        txt (str, optional): Mensagem específica a ser exibida. Defaults to '', nesse caso a mensagem é padrão.
    """
    if txt == '':
        txt = 'Operação Concluída com Sucesso!'  

    messagebox.showinfo(title="Sucesso!", message=txt)

def Mensagem_Erro(txt=''):
    """Caixa de mensagem na tela avisando que algo deu errado.  

    Args:
        txt (str, optional): Mensagem específica a ser Exibida. Defaults to '', nesse caso a mensagem é padrão.
    """
    if txt == '':
        txt = 'Essa Operação não pôde ser Concluída!'  
    
    messagebox.showerror(title="Erro!", message=txt)

def Sobre():
    """Caixa de mensagem para exibir informações sobre o Software
    """
    messagebox.showinfo(
        title="SOBRE",
        message="""
        Software para Controle de AGRs\n
        2022\n
        Meta Certificado Digital\n
        """)
