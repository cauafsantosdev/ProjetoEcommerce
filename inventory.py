import csv

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = []

    # Carregar estoque a partir de um arquivo CSV
    def load_inventory_csv(self):
        try:
            with open('inventory.csv', mode='r') as file:
                reader = csv.DictReader(file, delimiter=';')
                if 'ID' not in reader.fieldnames or 'Product' not in reader.fieldnames or 'Quantity' not in reader.fieldnames or 'Price' not in reader.fieldnames:
                    raise ValueError("CSV deve conter as colunas 'ID', 'Product', 'Quantity' e 'Price'.")
                for row in reader:
                    self.inventory.append(Product(int(row['ID']), row['Product'], int(row['Quantity']), float(row['Price'])))
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. Criando um novo estoque vazio.")
        except ValueError as e:
            print(f"Erro no arquivo CSV: {e}")

    # Salvar estoque no arquivo CSV
    def save_inventory_csv(self):
        with open('inventory.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['ID', 'Product', 'Quantity', 'Price'])
            for product in self.inventory:
                writer.writerow([product.product_id, product.name, product.quantity, product.price])

    # Adicionar um novo produto ou atualizar a quantidade de um existente
    def add_product(self, name, quantity, price):
        for product in self.inventory:
            if product.name == name:
                product.quantity += quantity
                self.save_inventory_csv()
                return
        new_id = max([product.product_id for product in self.inventory], default=0) + 1
        new_product = Product(new_id, name, quantity, price)
        self.inventory.append(new_product)
        self.save_inventory_csv()

    # Remover produto do estoque
    def remove_product(self, name):
        self.inventory = [product for product in self.inventory if product.name != name]
        # Reorganizar IDs
        for idx, product in enumerate(self.inventory):
            product.product_id = idx + 1
        self.save_inventory_csv()

    # Gerar lista de estoque formatada
    def list_inventory(self):
        products = []
        for product in self.inventory:
            linha = f"{product.product_id};{product.name};{product.quantity};{product.price:.2f}"
            products.append(linha)
        return products

    # Obter o tamanho do estoque
    def get_inventory_size(self):
        return len(self.inventory)

if __name__ == "__main__":
    inventory = Inventory()
    inventory.load_inventory_csv()
    inventory.add_product("Produto1", 10, 5.50)
    inventory.add_product("Produto2", 20, 10.00)
    print(inventory.list_inventory())