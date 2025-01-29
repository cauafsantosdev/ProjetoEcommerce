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
    elif choice == '2':
        for _ in range(3):
            input_senha = input('Senha: ')
            if input_senha == senha:
                with open('admin.py', 'r') as file:
                    codigo = file.readlines()
                    exec(''.join(codigo))
            else:
                print('Senha incorreta')
        else:
            print("Acesso negado!")
            quit()
    else:
        print("Opção inválida!")
