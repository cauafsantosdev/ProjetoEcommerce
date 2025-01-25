import inventory, display
from time import sleep


def main():
    background_ativo = False
    
    # Carregar o sistema de inventário
    inventory_system = inventory.Inventory()
    inventory_system.load_inventory_csv()
    app = inventory.Application(inventory_system)
    
    # Criar janela
    win = display.def_window()
    
    
    # Página inicial
    display.intial_page(win)
    
    # Define os botões principais
    botao_comprar = display.def_btn(win, 100, 109, "graphic elements/botao_comprar.ppm")
    botao_remover = display.def_btn(win, 100, 211, "graphic elements/botao_remover.ppm")
    botao_estoque = display.def_btn(win, 100, 323, "graphic elements/botao_estoque.ppm")
    botao_adicionar = display.def_btn(win, 300, 109, "graphic elements/botao_adicionar.ppm")
    botao_editar = display.def_btn(win, 300, 211, "graphic elements/botao_editar.ppm")
    botao_sair =  display.def_btn(win, 300, 323, "graphic elements/botao_sair.ppm")
    
    coords = {
        "botao_comprar": ((25, 71.5, 175, 146.5), botao_comprar),
        "botao_remover": ((25, 173.5, 175, 248.5), botao_remover),
        "botao_estoque": ((25, 285.5, 175, 360.5), botao_estoque),
        "botao_adicionar": ((200, 71.5, 350, 146.5), botao_adicionar),
        "botao_editar": ((200, 173.5, 350, 248.5), botao_editar),
        "botao_sair": ((200, 285.5, 350, 360.5), botao_sair)
    }
    
    while True:
        click = win.getMouse()
        
        for coord, botao in coords.values():
            if coord[0] < click.getX() < coord[2] and coord[1] < click.getY() < coord[3]:
                display.move_btn(botao)
                if botao != botao_sair:
                    display.backgroud_animation(win, background_ativo)
                    background_ativo = True
                
                
                if botao == coords["botao_comprar"][1]:
                    display.buy_product(win, app)
                    break
                elif botao == coords["botao_remover"][1]:
                    break
                elif botao == coords["botao_estoque"][1]:
                    display.plot_inventory(win, app)
                    break
                elif botao == coords["botao_adicionar"][1]:
                    break
                elif botao == coords["botao_editar"][1]:
                    break
                elif botao == coords["botao_sair"][1]:
                    win.close()
                    return
                    
        sleep(0.25)
if __name__ == "__main__":
    main()