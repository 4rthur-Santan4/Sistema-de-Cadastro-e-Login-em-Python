usuarios = {}#Dicionário onde as informações de cadastro são armazenadas

def cadastro(usuarios):

    print('---INÍCIO Menu Cadastro de Usuário---')

    usuario = input('Digite o usuário: ').strip()

    while not usuario or usuario in usuarios : #verifica se a variavel usuário está vazia e se o user já está cadastrado
                                               
        if not usuario:                       
            print('É preciso digitar o usuário!')
            usuario = input('Digite o usuário: ').strip() 

        else:
            print('Usuário já cadastrado!')
            print('1 - Digitar usuário novamente ')
            print('2 - Voltar para MENU ')

            escolha = input('Digite a opção escolhida: ').strip()

            while escolha not in ('1', '2'):
                print('Escolha somente entre as opções!')
                escolha = input('Digite a opção escolhida: ').strip()

            if escolha == '1':
                usuario = input('Digite outro usuário: ').strip()

            elif escolha == '2':
                print('Escolheu voltar para MENU!')
                return
            

    #Cadastro senha
    senha = input('Digite a senha: ')
    while len(senha) < 8: #Valida se a senha tem 8 caracteres

        print('A senha deve conter no mínimo 8 caracteres!')
        senha = input('Digite a senha: ')
    
    #Confirmação senha
    confirma_senha = input('Digite a senha novamente: ')

    while senha != confirma_senha:
        print('As senhas não coincidem!')
        confirma_senha = input('Digite a senha novamente: ')

    print(f'Cadastro realizado com sucesso! Bem vindo, {usuario}!')

    usuarios[usuario] = {'senha': senha}

    print('---FIM Menu Cadastro de Usuário---')


def login(usuarios):

    print('---INÍCIO Menu Login de Usuário---')

    usuario = input('Digite o usuário: ').strip()

    while not usuario or usuario not in usuarios:

        if not usuario:
            print('É preciso digitar o usuário!')
            usuario = input('Digite o usuário: ').strip() 

        else:
            print('Usuário não encontrado!')
            print('1 - Digitar usuário novamente ')
            print('2 - Voltar para MENU ')

            escolha = input('Digite a opção escolhida: ').strip()

            while escolha not in ('1', '2'):
                print('Escolha somente entre as opções!')
                escolha = input('Digite a opção escolhida: ').strip()

            if escolha == '1':
                usuario = input('Digite outro usuário: ').strip()

            elif escolha == '2':
                print('Escolheu voltar para MENU!')
                return


    tentativa = 0 

    while tentativa < 3:

        senha = input('Digite a senha: ')

        if senha == usuarios[usuario]['senha']:
            print(f'Login realizado com sucesso! Bem-vindo, {usuario}!')
            return #sai do while se a senha estiver correta

        else:
            tentativa += 1
            print(f'Senha incorreta! Tentativas restantes: {3 - tentativa}')
            
    print('Tentativas demais! Acesso bloqueado.')

    print('---FIM Menu Login de Usuário---')


def menu(usuarios):
    while True:
        print('---Menu de opções---')
        print('Escolha uma das opções a seguir:')
        print('1 - Cadastrar usuário')
        print('2 - Login com usuário') 
        print('9 - Sair')
        escolha = input('Opção Escolhida: ').strip()
        
        if escolha == '1':
            cadastro(usuarios)
            
        elif escolha == '2':
            login(usuarios)
            
        elif escolha == '9':
            print('Escolheu sair!')
            break
            
        else:
            print('Escolha somente entre as opções!')

menu(usuarios)
