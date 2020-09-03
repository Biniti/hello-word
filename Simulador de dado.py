dado= input("Deseja jogar o dado ?" "\n")
dado.upper()
while dado != "não":
    if dado == "sim":
        from random import randint//Essa parte serve para receber números aleatórios
        print("O valor do dado é:",randint(1,6))//''randit(1,6)'' estou definindo valores aleatórios entre 1 a 6
        dado = input("Deseja jogar o dado ?" "\n")
        dado.upper()
    else:
        print("Por favor digite apenas sim ou não")
        dado = input("Deseja jogar o dado ?" "\n")
        dado.upper()


