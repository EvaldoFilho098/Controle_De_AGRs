from Telas import *

class JanelaInicio(Tela):
    def __init__(self, master):
        super().__init__(master)
        self.root.mainloop()
        

root = Tk()
JanelaInicio(root)