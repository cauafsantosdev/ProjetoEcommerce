import importlib
import time
from inventory import Inventory

try:
    import graphics
except ImportError or ModuleNotFoundError:
    import subprocess
    print("Instalando biblioteca graphics...")
    subprocess.run(["pip", "install", "graphics.py"])
    time.sleep(5)
    importlib.reload(graphics)

# Inicializar o sistema de estoque
inventory_system = Inventory()
inventory_system.load_inventory_csv()

# Configuração inicial
win = graphics.GraphWin("World Tech Center", 1200, 800)
background = graphics.Image(graphics.Point(600, 400), "graphic elements/admin.ppm")
background.draw(win)

# Definições de layout
table_start_x, table_start_y = 150, 200
row_height, col_width = 30, 300
max_rows = 10  # Número máximo de linhas visíveis na tabela

# Função para desenhar a tabela e os itens do estoque

def draw_table():
    win.delete("all")
    background.draw(win)

    # Linhas da tabela
    items = inventory_system.list_inventory()
    for row_idx in range(max_rows):
        y = table_start_y + row_idx * row_height
        if row_idx < len(items):
            item_data = items[row_idx].split(";")

            # Desenhar ID
            id_text = graphics.Text(graphics.Point(table_start_x + 50, y + row_height / 2), item_data[0])
            id_text.setSize(12)
            id_text.draw(win)

            # Desenhar Nome
            name_text = graphics.Text(graphics.Point(table_start_x + 200, y + row_height / 2), item_data[1])
            name_text.setSize(12)
            name_text.draw(win)

            # Desenhar Quantidade
            quantity_text = graphics.Text(graphics.Point(table_start_x + 450, y + row_height / 2), item_data[2])
            quantity_text.setSize(12)
            quantity_text.draw(win)

            # Desenhar Valor
            value_text = graphics.Text(graphics.Point(table_start_x + 700, y + row_height / 2), item_data[3])
            value_text.setSize(12)
            value_text.draw(win)

# Funções para lidar com ações de adicionar, alterar e remover

def add_product(name, quantity, price):
    inventory_system.add_product(name, quantity, price)
    draw_table()


def remove_product(name):
    inventory_system.remove_product(name)
    draw_table()

# Inputs para os campos
name_add_input = graphics.Entry(graphics.Point(101, 325), 20)
name_add_input.draw(win)

quantity_add_input = graphics.Entry(graphics.Point(255, 325), 10)
quantity_add_input.draw(win)

price_add_input = graphics.Entry(graphics.Point(386, 325), 10)
price_add_input.draw(win)

id_change_input = graphics.Entry(graphics.Point(101, 505), 10)
id_change_input.draw(win)

quantity_change_input = graphics.Entry(graphics.Point(255, 505), 10)
quantity_change_input.draw(win)

price_change_input = graphics.Entry(graphics.Point(386, 505), 10)
price_change_input.draw(win)

id_remove_input = graphics.Entry(graphics.Point(255, 677), 10)
id_remove_input.draw(win)

# Função para limpar os inputs
def clear_inputs():
    name_add_input.setText("")
    quantity_add_input.setText("")
    price_add_input.setText("")

# Loop principal para capturar cliques
while True:
    click = win.getMouse()

    # Verificar se clicou no botão "Adicionar"
    if (700 <= click.x <= 800) and (500 <= click.y <= 550):  # Coordenadas do botão de adicionar na imagem
        name = name_add_input.getText()
        quantity = quantity_add_input.getText()
        price = price_add_input.getText()
        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            add_product(name, int(quantity), float(price))
            clear_inputs()

    # Verificar se clicou no botão "Remover"
    if (700 <= click.x <= 800) and (550 <= click.y <= 600):  # Coordenadas do botão de remover na imagem
        name = name_add_input.getText()
        if name:
            remove_product(name)
            clear_inputs()

    # Verificar se clicou no botão "Alterar"
    if (700 <= click.x <= 800) and (600 <= click.y <= 650):  # Coordenadas do botão de alterar na imagem
        name = name_add_input.getText()
        quantity = quantity_add_input.getText()
        price = price_add_input.getText()
        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            remove_product(name)  # Remover o produto antigo
            add_product(name, int(quantity), float(price))  # Adicionar com os novos valores
            clear_inputs()

# Desenhar a tabela inicial
draw_table()
