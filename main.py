import classes
import graphic


def main():
    # Carregar o sistema de inventário
    inventory_system = classes.Inventory()
    inventory_system.load_inventory_csv()
    app = classes.Application(inventory_system)
    
    # Criar janela gráfica
    win = graphic.criar_janela()
    
    # Carregar elementos gráficos
    graphic.tela_inicial(win)


if __name__ == "__main__":
    main()