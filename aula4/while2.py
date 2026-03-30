#estrutura de repetição: while

#executara o while até acertar a senha
while True: 
    usuario = input("digite seu login: ")
    senha = input('digite sua senha: ')

    if(usuario =='admin' and senha =="123"):
        break
    else:
        print('falha ao realizar login')

print('bem vindo ao sistema')