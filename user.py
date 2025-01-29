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
    

# Inicializa o sistema de estoque    
inventory_system = Inventory()
inventory_system.load_inventory_csv()

# Inicializa a janela
win = graphics.GraphWin("World Tech Center", 1200, 800)
background = graphics.Image(graphics.Point(600, 400), "graphic elements/user.ppm")
background.draw(win)

# Definições de layout da tabela de estoque
table_start_x, table_start_y = 43, 73
row_height, col_width = 30, 300
max_rows = 23  # Número máximo de linhas possíveis na tabela

# Função para desenhar a tabela e os itens do estoque
drawn_elements = []

def draw_table():
    global drawn_elements
    
    for element in drawn_elements: # Apagar elementos existentes
        element.undraw()
    drawn_elements = []  # Reseta a lista de elementos

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
            value_text = graphics.Text(graphics.Point(table_start_x + 535, y + row_height / 2), f"R${item_data[3]}")
            value_text.setSize(14)
            value_text.setStyle("bold")
            value_text.setTextColor("white")
            value_text.draw(win)
            drawn_elements.append(value_text)

# Função para compra
def buy_product(product_id, quantity):
    if inventory_system.buy_product(product_id, quantity):
        draw_table()
    else:
        alert = graphics.Text(graphics.Point(918, 505), "ID ou Quantidade inválidos.")
        alert.setSize(15)
        alert.setStyle("bold")
        alert.setTextColor("red")
        alert.draw(win)
        time.sleep(2)
        alert.undraw()

# Inputs para a compra
id_input = graphics.Entry(graphics.Point(875, 465), 7)
id_input.draw(win)

quantity_input = graphics.Entry(graphics.Point(961, 465), 7)
quantity_input.draw(win)

# Função para limpar os inputs
def clear_inputs():
    id_input.setText("")
    quantity_input.setText("")

# Desenha a tabela de estoque ao inicializar o programa
draw_table()

# Loop principal para capturar cliques
while True:
    click = win.getMouse()

    # Verificar se clicou no botão "Comprar"
    if (824 <= click.x <= 1026) and (538 <= click.y <= 596):  # Coordenadas do botão de compra
        product_id = id_input.getText()
        quantity = quantity_input.getText()
        if product_id and quantity.isdigit():
            buy_product(int(product_id), int(quantity))
            clear_inputs()

    # Sair do programa
    if (1138 <= click.x <= 1188) and (5 <= click.y <= 30):
        win.close()