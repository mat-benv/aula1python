#não funciona

while True:
    senha = input("Crie uma senha: ")
    list(senha)
    if not any(senha.isupper()):
        print("A senha deve conter uma letra maiúscula.")
        continue
    elif not any(senha.isdigit()):
        print("A senha deve conter um número.")
        continue
    elif not any(senha.isalnum()):
        print("A senha deve conter um caractere especial.")
        continue
    else:
        print("Senha aceita.")
        break
print('Até logo!')
