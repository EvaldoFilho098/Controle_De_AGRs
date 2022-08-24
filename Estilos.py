"""
Estilos
"""

from tkinter import ttk
from Cores import *
from Fontes import *

style = ttk.Style()
style.theme_use('clam')
style.configure("Preto_Maior.Treeview",
                fieldbackground=preto_fosco,
                foreground=branco,
                background=preto,
                bordercolor=laranja_meta,
                font=fonte_Mediana_14,
                rowheight=40,
                relief="flat",
                )
style.configure("Preto_Maior.Treeview.Heading",
                font=fonte_Destaques_24,
                foreground=preto,
                background=cinza_claro_suave,
                )

style.layout("Preto_Maior.Treeview", [
             ('Preto_Maior.Treeview.treearea', {'sticky': 'nswe'})])
