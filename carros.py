import os
from Veiculos import organizacao
from datetime import datetime

def main ():
    
    org = organizacao()
    dia = 0
    entrada = 0
    comando = "date +%x --date \"0 days\""
    now = datetime.now()

    diahjsist = now.day
    mes = now.month
    ano = now.year
    
    os.system("clear")
    
    print("\t\tBEM VIDO A CENTRAL DE VEÍCULOS GG!!!\n\n")

    while entrada != 7:
        
        if diahjsist > 30:
        
            diahjsist -= 30
            mes += 1
        
            if mes > 12:
                mes -= 12
                ano += 1
    
        print("Data atual:")
        os.system(comando)
        #print ("%d/%d/%d"%(now.day,now.month,now.year))

        print("Quantidade de veículos cadastrados: %d"%(org.getVeiculos()))
        print("Quantidade de veículos alugados/reservado: %d"%(org.getIndisponiveis()))
        print("Quantidade de atrasos: ")
        
        print("\n\tOPERAÇÕES:")
        print("\n(1) Consultar veículos")
        print("(2) Adicionar veículos")
        print("(3) Alugar/reservar veículos")
        print("(4) Devolver/liberar veículos")
        print("(5) Excluir veículos")
        print("(6) Avançar data atual")
        print("(7) Sair")

        try:
            entrada = int(input("\nOperação desejada: "))
            
        except ValueError as e:
            print("Digite um valor inteiro")
            input()

        if entrada == 1:#consultar veiculo
            org.consultar()
            input()
        
        elif entrada == 2:# adicionar veiculo
            
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            
            try:
                ano = int(input("ano: "))
            except ValueError as e:
                ano = int(input("Digite um valor inteiro "))
                
            
            try:
                valor = float(input("valor do aluguel: "))
            except ValueError as e:
                valor = float(input("Digite um valor inteiro"))
                

            org.adicionar(marca, modelo, ano, valor)
        
        elif entrada == 3:#alugar\reservar
            escolha = int(input("O senhor deseja (1)Alugar ou (2)Reservar um veiculo: "))

            if escolha == 1:
                org.alugar()
            
            elif escolha == 2:
                org.reservar()

        elif entrada == 4:#devolver\liberar veiculo
            escolha = int(input("O senhor deseja (1)Devolver ou (2)liberar o veiculo: "))
            
            if escolha == 1:
                org.devolver(diahjsist, mes, ano)
            
            elif escolha == 2:
                org.liberar()
        
        elif entrada == 5:#escluir veiculo
            org.excluir()
        
        elif entrada == 6:# avancar data
            dia += 1
            comando = comando.replace(comando[17], str(dia))
            diahjsist += 1
                    
        os.system("clear")
main()