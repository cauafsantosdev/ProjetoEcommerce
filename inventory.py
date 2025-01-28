import csv
import pandas as pd

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
        inventory = pd.read_csv("inventory.csv", sep=";", skiprows=1, header=None)
        print(inventory.head())
        for _, row in inventory.iterrows():
            self.inventory.append(Product(int(row[0]), row[1], int(row[2]), float(row[3])))

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
    def remove_product(self, product_id):
        self.inventory = [product for product in self.inventory if product.product_id != product_id]
        # Reorganizar IDs
        for idx, product in enumerate(self.inventory):
            product.product_id = idx + 1
        self.save_inventory_csv()

    # Altera o produto
    def change_product(self, product_id: int, quantity: int, price: float):
        for product in self.inventory:
            if product.product_id == product_id:
                product.quantity = quantity
                product.price = price

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

    # Processar compra
    def buy_product(self, product_id: int, quantity: int):
        for product in self.inventory:
            if product.product_id == product_id:
                if product.quantity < quantity:
                    return False
                else:
                    product.quantity -= quantity
                    self.save_inventory_csv()
                    return True
    

if __name__ == "__main__":
    inventory = Inventory()
    inventory.load_inventory_csv()
    print(inventory.search_product(3))