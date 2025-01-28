senha = '1234'

print('''Login
1 - Comprar
2 - ADMIN'''
)

if input() == '1':
    with open('user.py', 'r') as file:
        codigo = file.readlines()
        exec(''.join(codigo))
else:
    if input('Senha: ') == senha:
        with open('admin.py', 'r') as file:
            codigo = file.readlines()
            exec(''.join(codigo))
    else:
        print('Senha incorreta')
