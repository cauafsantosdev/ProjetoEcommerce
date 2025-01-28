import importlib
import time
import inventory

try:
    import graphics
except ImportError or ModuleNotFoundError:
    import subprocess
    print("Instalando biblioteca graphics...")
    subprocess.run(["pip", "install", "graphics.py"])
    time.sleep(5)
    importlib.reload(graphics)
    
    
def def_window():
    win = graphics.GraphWin("World Tech Center", 1200, 800)
    bg = graphics.Image(graphics.Point(600, 400), "graphic elements/user.ppm")
    bg.draw(win)
    return win

def show_inventory(win, dados, colunas, linhas, x_inicial, y_inicial, largura_celula, altura_celula):
    # Preencher as células da tabela com os dados
    for i in range(linhas):
        for j in range(colunas):
            # Posição central das células
            x = x_inicial + j * largura_celula + largura_celula / 2
            y = y_inicial + i * altura_celula + altura_celula / 2
            texto = dados[i][j] if j < len(dados[i]) else ""
            texto_obj = graphics.Text(graphics.Point(x, y), texto)
            texto_obj.setSize(12)  # Ajuste o tamanho do texto se necessário
            texto_obj.draw(win)

def buy_product(win, app):
    i = 0
    for i in range(app.inventory_system.get_inventory_size()):    
        product_name = graphics.Entry(graphics.Point(600, 200 + i), 10)
        product_name.draw(win)
        quantity = graphics.Entry(graphics.Point(650, 200 + i), 1)
        quantity.draw(win)
        i += 20
        graphics.update(1)