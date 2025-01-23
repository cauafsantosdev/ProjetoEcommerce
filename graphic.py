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

def criar_janela():
    win = graphics.GraphWin("Prisco Shop", 800, 400, autoflush=False)
    return win

def tela_inicial(win):
    background = graphics.Image(graphics.Point(400, 200), "graphic elements/background.ppm")
    background.draw(win)

    for i in range(1000, 610, -10):
        background_2 = graphics.Image(graphics.Point(i, 200), "graphic elements/background_2.ppm")
        background_2.draw(win)
        graphics.update(60)

    win.getMouse()
