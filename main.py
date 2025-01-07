import csv


class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.inventory = []

    # Carregar estoque a partir de um arquivo CSV
    def load_inventory_csv(self):
        try:
            with open('inventory.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.inventory.append(Product(row["Name"], int(row["Quantity"])))
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. Criando um novo estoque vazio.")

    # Salvar estoque no arquivo CSV
    def save_inventory_csv(self):
        with open('inventory.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Quantity"])
            for product in self.inventory:
                writer.writerow([product.name, product.quantity])

    # Adicionar um novo produto ou atualizar a quantidade de um existente
    def add_product(self, name, quantity):
        for product in self.inventory:
            if product.name == name:
                product.quantity += quantity
                self.save_inventory_csv()
                return
        new_product = Product(name, quantity)
        self.inventory.append(new_product)
        self.save_inventory_csv()

    # Gerar lista de estoque
    def list_inventory(self):
        for product in self.inventory:
            print(f"Produto: {product.name}, Quantidade: {product.quantity}")

    # Verificar quantidade de um produto específico
    def check_product_quantity(self, name):
        for product in self.inventory:
            if product.name == name:
                print(f"Quantidade de {name}: {product.quantity}")
                return
        print(f"Produto {name} não encontrado no estoque.")

    # Reduzir a quantidade de um produto após uma compra
    def reduce_product_quantity(self, name, quantity):
        for product in self.inventory:
            if product.name == name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    self.save_inventory_csv()
                    print(f"Compra de {quantity} unidade(s) de {name} realizada com sucesso.")
                else:
                    print(f"Estoque insuficiente para {name}. Quantidade disponível: {product.quantity}")
                return
        print(f"Produto {name} não encontrado no estoque.")


class Application:
    def __init__(self, inventory_system):
        self.inventory_system = inventory_system

    # Simular compras realizadas por um usuário
    def purchase(self, product_name, quantity):
        print(f"Tentando comprar {quantity} unidade(s) de {product_name}...")
        self.inventory_system.reduce_product_quantity(product_name, quantity)

    # Mostrar o estoque para o usuário
    def show_inventory(self):
        print("\nEstoque atual:")
        self.inventory_system.list_inventory()


# Simulação do sistema
inventory_system = Inventory()

# Carregar estoque existente
inventory_system.load_inventory_csv()

# Adicionar produtos ao estoque
inventory_system.add_product("Camiseta", 50)
inventory_system.add_product("Calça Jeans", 30)

# Criar aplicação
app = Application(inventory_system)

# Mostrar estoque inicial
app.show_inventory()

# Realizar compras
app.purchase("Camiseta", 5)
app.purchase("Calça Jeans", 10)
app.purchase("Tênis", 2)

# Mostrar estoque atualizado
app.show_inventory()
