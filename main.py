senha = '1234'

print('''Login
1 - Comprar
2 - ADMIN'''
)

while True:
    choice = input()

    if choice == '1':
        with open('user.py', 'r') as file:
            codigo = file.readlines()
            exec(''.join(codigo))
    elif choice == 2:
        if input('Senha: ') == senha:
            with open('admin.py', 'r') as file:
                codigo = file.readlines()
                exec(''.join(codigo))
        else:
            print('Senha incorreta')
    else:
        print("Opção inválida!")
