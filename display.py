import importlib
import time

try:
    import graphics
except ImportError or ModuleNotFoundError:
    import subprocess
    print("Instalando biblioteca graphics...")
    subprocess.run(["pip", "install", "graphics.py"])
    time.sleep(5)
    importlib.reload(graphics)
    
class Botao:
    def __init__(self, win, x, y, path):
        self.x = x
        self.y = y
        self.pos = graphics.Point(x, y)
        self.botao = graphics.Image(self.pos, path)
        self.botao.draw(win)
    
    
def gerar_janela():
    win = graphics.GraphWin("Prisco Shop", 800, 400)
    return win

def pagina_inicial(win):
    background = graphics.Image(graphics.Point(400, 200), "graphic elements/background.ppm")
    background.draw(win)
    sombras = graphics.Image(graphics.Point(200, 220), "graphic elements/sombras_botoes.ppm")
    sombras.draw(win)
    
    