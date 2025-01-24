import inventory, display


def main():
    # Carregar o sistema de inventário
    inventory_system = inventory.Inventory()
    inventory_system.load_inventory_csv()
    app = inventory.Application(inventory_system)
    
    # Criar janela
    win = display.gerar_janela()
    
    
    # Página inicial
    display.pagina_inicial(win)
    
    # tem que mudar os botoes no figma
    botao_comprar = display.Botao(win, 100, 110, "graphic elements/botao_comprar.ppm")
    botao_remover = display.Botao(win, 100, 213, "graphic elements/botao_remover.ppm")
    botao_estoque = display.Botao(win, 100, 315, "graphic elements/botao_estoque.ppm")
    botao_adicionar = display.Botao(win, 300, 110, "graphic elements/botao_adicionar.ppm")
    botao_editar = display.Botao(win, 300, 210, "graphic elements/botao_editar.ppm")
    botao_sair = display.Botao(win, 300, 325, "graphic elements/botao_sair.ppm")
    win.getMouse()

if __name__ == "__main__":
    main()