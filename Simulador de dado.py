dado= input("Deseja jogar o dado ?" "\n")
dado.upper()
while dado != "não":
    if dado == "sim":
        from random import randint
        print("O valor do dado é:",randint(0,6))
        dado = input("Deseja jogar o dado ?" "\n")
        dado.upper()
    else:
        print("Por favor digite apenas sim ou não")
        dado = input("Deseja jogar o dado ?" "\n")
        dado.upper()


