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
    
    
def def_window():
    win = graphics.GraphWin("Prisco Shop", 800, 400)
    return win


def intial_page(win):
    background = graphics.Image(graphics.Point(400, 200), "graphic elements/background.ppm")
    background.draw(win)
    shadows = graphics.Image(graphics.Point(200, 220), "graphic elements/sombras_botoes.ppm")
    shadows.draw(win)
    welcome = graphics.Image(graphics.Point(600, 200), "graphic elements/boas-vindas.ppm")
    welcome.draw(win)   

    
def def_btn(win, x, y, imagem):
    botao = graphics.Image(graphics.Point(x, y), imagem)
    botao.draw(win)
    return botao


def move_btn(botao):
    botao.move(0, 3)
    time.sleep(0.1)
    botao.move(0, -3)
    

#animação da troca de abas
def backgroud_animation(win, background_ativo):
    if background_ativo:
        for i in range(600, 1000, 15):
            background_2 = graphics.Image(graphics.Point(i, 200), "graphic elements/limpa_background_2_.ppm")
            background_2.draw(win)
            graphics.update(120)

    for i in range(1000, 600, -15):
        background_2 = graphics.Image(graphics.Point(i, 200), "graphic elements/background_2.ppm")
        background_2.draw(win)
        graphics.update(120)


#comprar produto
def buy_product(win, app):
    i = 0
    for i in range(app.inventory_system.get_inventory_size()):    
        product_name = graphics.Entry(graphics.Point(600, 200 + i), 10)
        product_name.draw(win)
        quantity = graphics.Entry(graphics.Point(650, 200 + i), 1)
        quantity.draw(win)
        i += 20
        graphics.update(1)
    
# carregar estoque
def plot_inventory(win, app):
    inventory = app.show_inventory()
    i = 0
    
    if not inventory:
        graphics.Text(graphics.Point(600, 200), "Nenhum produto no estoque.").draw(win)
        graphics.update(60)
        return
    
    for line in inventory:
        graphics.Text(graphics.Point(600, 30 + i), line).draw(win)
        graphics.update(60)
        i += 20
    