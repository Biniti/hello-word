#Nomes:Vinicius Santos,Thales Hipólito,Arthur Vilar,João Gabriel
menu =""
lista_nomes = []
lista_debito = []
lista_apt = []
lista_cpf = []
devedor=[]
quitado=[]
while True :
    menu = int(input("""
1: Inserir um novo condômino (cpf, nome, apartamento e débito).
2: Consultar condôminos pelo cpf.
3: Atualizar o débito do condôminos pelo cpf (Devedor ou Pagador)
4: Exibir os condôminos devedores
5: Exibir os condôminos quites
6: Remover os condôminos
0: Sair do programa;"""))
    if menu == 1:
        novo_nome = (input("Digite o seu nome:"))
        lista_nomes.append(novo_nome)

        novo_cpf = (int(input("Digite o cpf:")))
        lista_cpf.append(novo_cpf)

        novo_apt = (int(input("Digite o número do novo apt:")))
        lista_apt.append(novo_apt)

        novo_debito = (int(input("Digite o novo débito:")))
        lista_debito.append(novo_debito)

    if menu == 2:
        consulta = int(input("Digite o cpf:"))

        if consulta in lista_cpf:
            ln = lista_cpf.index(consulta)
            print("O morador do condomino é:", lista_nomes[ln], "e o apartamento é:", lista_apt[ln])

        else:
            print("O cpf não esta cadastrado")

    if menu == 3:
        atualizar=int(input("Digite o cpf:"))
        atualizado=int(input("Digite 1 caso o cliente esteja devendo ou 2 caso o cliente tenha quitado:"))

        if atualizar in lista_cpf:
            la=lista_cpf.index(atualizar)

            if atualizado==1:
                devedor.append("Devedores:")
                devedor.append(lista_nomes[la])

                print("O cliente esta devendo")

            elif atualizado==2:
                quitado.append("Quitados:")
                quitado.append(lista_nomes[la])

                print("O cliente esta quitado")

    if menu == 4:
        if "Devedores:" in devedor and "Quitados:" in quitado:
            devedor.remove("Devedores:")
            devedor.remove(lista_nomes[la])
            quitado.remove("Quitados:")
            quitado.remove(lista_nomes[la])

            print("Por favor atualize novamente o débito do cliente")

        elif "Devedores:" in devedor:
            print("Os condominos devedores são:",devedor)

        else:
            print("No momento nenhum condomino esta devendo")

    if menu == 5:
        if "Devedores:" in devedor and "Quitados:" in quitado:
            devedor.remove("Devedores:")
            devedor.remove(lista_nomes[la])
            quitado.remove("Quitados:")
            quitado.remove(lista_nomes[la])

            print("Por favor atualize novamente o débito do cliente")
        elif "Quitados:" in quitado:

            print("Os condominos quitados são:",quitado)

        else:

            print("No momento nenhum condomino esta quitado")

    if menu == 6 :
        remover=int(input("Digite o cpf do cliente que deseja remover:"))

        if remover in lista_cpf:
            lr=lista_cpf.index(remover)
            lista_nomes.pop(lr)
            lista_cpf.pop(lr)
            lista_debito.pop(lr)
            lista_apt.pop(lr)

            print("O cliente foi removido")

    if menu == 0 :
        print("Programa encerrado")
        exit()




