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

# Inicializa a janela
win = graphics.GraphWin("World Tech Center", 1200, 800)
background = graphics.Image(graphics.Point(600, 400), "graphic elements/admin.ppm")
background.draw(win)

# Definições da tabela de estoque
table_start_x, table_start_y = 527, 79
row_height, col_width = 30, 300
max_rows = 23  # Número máximo de linhas possíveis na tabela

# Função para desenhar a tabela e os itens do estoque
drawn_elements = []

def draw_table():
    global drawn_elements
    
    for element in drawn_elements: # Apagar elementos existentes
        element.undraw()
    drawn_elements = []  # Limpar a lista de elementos

    # Redesenhar os itens
    items = inventory_system.list_inventory()
    for row_idx in range(max_rows):
        y = table_start_y + row_idx * row_height
        if row_idx < len(items):
            item_data = items[row_idx].split(";")

            # Desenhar ID
            id_text = graphics.Text(graphics.Point(table_start_x + 50, y + row_height / 2), item_data[0])
            id_text.setSize(14)
            id_text.setStyle("bold")
            id_text.setTextColor("white")
            id_text.draw(win)
            drawn_elements.append(id_text)

            # Desenhar Nome
            name_text = graphics.Text(graphics.Point(table_start_x + 260, y + row_height / 2), item_data[1])
            name_text.setSize(14)
            name_text.setStyle("bold")
            name_text.setTextColor("white")
            name_text.draw(win)
            drawn_elements.append(name_text)

            # Desenhar Quantidade
            quantity_text = graphics.Text(graphics.Point(table_start_x + 454, y + row_height / 2), item_data[2])
            quantity_text.setSize(14)
            quantity_text.setStyle("bold")
            quantity_text.setTextColor("white")
            quantity_text.draw(win)
            drawn_elements.append(quantity_text)

            # Desenhar Valor
            value_text = graphics.Text(graphics.Point(table_start_x + 534, y + row_height / 2), f"R${item_data[3]}")
            value_text.setSize(14)
            value_text.setStyle("bold")
            value_text.setTextColor("white")
            value_text.draw(win)
            drawn_elements.append(value_text)

# Função para adicionar produto ao estoque
def add_product(name: str, quantity: int, price: float):
    inventory_system.add_product(name, quantity, price)
    draw_table()

# Função para remover produto do estoque
def remove_product(product_id: int):
    inventory_system.remove_product(product_id)
    draw_table()

# Função para alterar produto
def change_product(product_id: int, quantity: int, price: float):
    inventory_system.change_product(product_id, quantity, price)
    draw_table()

# Inputs para adicionar produto
name_add_input = graphics.Entry(graphics.Point(101, 325), 20)
name_add_input.draw(win)

quantity_add_input = graphics.Entry(graphics.Point(255, 325), 10)
quantity_add_input.draw(win)

price_add_input = graphics.Entry(graphics.Point(386, 325), 10)
price_add_input.draw(win)

# Inputs para alterar produto
id_change_input = graphics.Entry(graphics.Point(101, 505), 10)
id_change_input.draw(win)

quantity_change_input = graphics.Entry(graphics.Point(255, 505), 10)
quantity_change_input.draw(win)

price_change_input = graphics.Entry(graphics.Point(386, 505), 10)
price_change_input.draw(win)

# Input para remover produto
id_remove_input = graphics.Entry(graphics.Point(255, 677), 10)
id_remove_input.draw(win)

# Função para limpar os inputs
def clear_inputs():
    name_add_input.setText("")
    quantity_add_input.setText("")
    price_add_input.setText("")
    id_change_input.setText("")
    quantity_change_input.setText("")
    price_change_input.setText("")
    id_remove_input.setText("")

# Desenha a tabela de estoque ao inicializar o programa
draw_table()

# Loop principal para capturar cliques
while True:
    click = win.getMouse()

    # Verificar se clicou no botão "Adicionar"
    if (132 <= click.x <= 375) and (368 <= click.y <= 414):  # Coordenadas do botão de adicionar produto
        name = name_add_input.getText()
        quantity = quantity_add_input.getText()
        price = price_add_input.getText()
        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            add_product(name, int(quantity), float(price))
            clear_inputs()

    # Verificar se clicou no botão "Alterar"
    if (132 <= click.x <= 375) and (550 <= click.y <= 595):  # Coordenadas do botão de alterar produto
        product_id = id_change_input.getText()
        quantity = quantity_change_input.getText()
        price = price_change_input.getText()
        if product_id and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            change_product(int(product_id), int(quantity), float(price))
            clear_inputs()

    # Verificar se clicou no botão "Remover"
    if (132 <= click.x <= 375) and (710 <= click.y <= 755):  # Coordenadas do botão de remover produto
        product_id = id_remove_input.getText()
        if product_id:
            remove_product(int(product_id))
            clear_inputs()

    # Sair do programa
    if (1138 <= click.x <= 1188) and (5 <= click.y <= 30):
        win.close()