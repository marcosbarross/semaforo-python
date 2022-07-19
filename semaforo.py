usuarios = []
menu = 3

controle = 0

while menu != 0:
    menu = int(input("Se deseja logar digite 1 se deseja cadastrar digite 2: "))
    
    if menu == 1 and controle == 0:
        login = input("Qual seu usuário: ")
        
        for i in range (0, len(usuarios)):
            if login == usuarios[i] and controle == 0:
                print(f"Bem-vindo, {login}!")
                controle += 1
            
            if login != usuarios[i]:
                print("Usuário não cadastrado")
    
    elif controle > 0:
        print("Há um usuário já logado")
        signUp = input("Deseja sair do usuário já logado? (S/N) ")
        
        if signUp == "S" or signUp == "s":
            controle -= 1
            print("Usuário deslogado")	


    if menu == 2:
        cadastro = input("Cadastre seu usuário: ")
        if len(cadastro) > 0:
                usuarios.append(cadastro)
        else:
            print("Insira um nome de usuário")