from datetime import datetime

class organizacao (object):

    def __init__(self):
        self.veiculo = []
        self.prazos = []
    
    def getVeiculos(self):#quantidade de veiculos cadastrados
        return len(self.veiculo)
    
    def getIndisponiveis(self):#quantidade de veiculos alugados ou rezervados
        return len(self.prazos)

    def adicionar(self,marca,modelo,ano,aluguel):
        veiculo = "Veiculo: " + str(len(self.veiculo) + 1) + " Modelo: " + modelo + " Marca: " + marca + " Ano: " + str(ano) + " Aluguel: " + str(aluguel) +   " 1"
        
        self.veiculo.append(veiculo)
        input()

    def consultar(self):
        
        i = 0        
        while i < len(self.veiculo):
            
            aux = self.veiculo[i].find("Marca")
            print(self.veiculo[i][:aux-1])
            
            if self.veiculo[i][-1::] == '1':
                print("Veiculo disponível")
            
            else:
                print("Veiculo indisponível")
            i += 1
        
        detalhes = input("Para mais detalhes digite 1")

        if detalhes == '1':
            i = 0
            while i < len(self.veiculo):
            
                print(self.veiculo[i])
                
                if self.veiculo[i][-1::] == '1':
                    print("Veiculo disponível")
                
                else:
                    print("Veiculo indisponível")
                i += 1            

    
    def alugar(self):
        nomeLocatario = input("Nome do Locatario: ")
        prazo = int(input("Por quanto tempo (dias) deseja alugar o veiculo: "))

        now = datetime.now()
        dia = now.day + prazo
        mes = now.month
        ano = now.year

        if dia > 30:
        
            dia -= 30
            mes = now.month + 1
        
            if mes > 12:
                mes -= 12
                ano = now.year + 1

        if len(self.veiculo) == 0:
            print("Não temos veiculos!!! sorry")
        
        elif prazo > 30:
            
            print("Aluguel e reservas somente poderão ser realizadas para no máximo 30 dias")
        
        else:
            
            escolha = int(input("Escolha o veiculo a ser alugado: "))
            escolha -= 1

            aux = int(self.veiculo[escolha][-1::])

            if aux != 1:
                print("Veiculo indisponível")
            
            else:
                self.veiculo[escolha] = self.veiculo[escolha].replace(self.veiculo[escolha][-1::], '0')
                
                dataVencimento = escolha, str(dia) + "/" + str(mes) + "/" + str(ano), nomeLocatario, prazo
                self.prazos.append(dataVencimento)

    def reservar(self):
        nomeLocatario = input("Nome do Locatario: ")
        prazo = int(input("Por quanto tempo (dias) deseja alugar o veiculo: "))

        if prazo > 30:     
            print("Aluguel e reservas somente poderão ser realizadas para no máximo 30 dias")

        else:
            escolha = int(input("Qual carro deseja rerservar: "))
            escolha -= 1
            
            dataReserva = input("Data para a reserva(d/m/aaaa): ")

            reserva = dataReserva.split('/')
            dia = int(reserva[0])
            mes = int(reserva[1])
            ano = int(reserva[2])
            i = 0
            
            while i < len(self.prazos):
                if self.prazos[i][0] == escolha:
                    
                    reservaVeiculo = self.prazos[i][1].split('/')#data que o veicul tah reservado
                    diaV = int(reservaVeiculo[0])
                    mesV = int(reservaVeiculo[1])
                    anoV = int(reservaVeiculo[2])

                    if ano == anoV:
                        if mes == mesV:
                            if dia >= diaV:
                                
                                dataVencimento = escolha, str(dia) + "/" + str(mes) + "/" + str(ano)
                                self.prazos.append(dataVencimento)
                                self.veiculo[escolha] = self.veiculo[escolha].replace(self.veiculo[escolha][-1::], '0')
                            else:
                                print("Veiculo indisponível")
                        else:
                            dataVencimento = escolha, str(dia) + "/" + str(mes) + "/" + str(ano)
                            self.prazos.append(dataVencimento)
                            self.veiculo[escolha] = self.veiculo[escolha].replace(self.veiculo[escolha][-1::], '0')
                    else:
                        dataVencimento = escolha, str(dia) + "/" + str(mes) + "/" + str(ano)
                        self.prazos.append(dataVencimento)
                        self.veiculo[escolha] = self.veiculo[escolha].replace(self.veiculo[escolha][-1::], '0')

                i +=1
            
            if i == len(self.prazos):
                dataVencimento = escolha, str(dia) + "/" + str(mes) + "/" + str(ano), nomeLocatario, prazo
                self.prazos.append(dataVencimento)
                self.veiculo[escolha] = self.veiculo[escolha].replace(self.veiculo[escolha][-1::], '0')

    def devolver(self, dia, mes, ano):

        veiculo = int(input("Veiculo a ser devolvido: "))
        veiculo -=1

        i = 0
        while i < len(self.prazos):
            print("Veiculo alugado: %d"%(self.prazos[i][0] + 1))
            input()

            if self.prazos[i][0] == veiculo:
                prazoVeiculo = self.prazos[i][1].split('/')#data que o veicul tah reservado
                
                diaV = int(prazoVeiculo[0])
                mesV = int(prazoVeiculo[1])
                anoV = int(prazoVeiculo[2])
                
                aux1 = self.veiculo[i].find("Aluguel")
                aux1 += 10

                valor = float(self.veiculo[i][aux1: -2])

                if mes == mesV:
                    if dia == diaV:
                        print("Nome do Locatario: %s"%(self.prazos[i][2]))
                        print("Pagar: %d"%(valor*self.prazos[i][3]))
                        self.prazos.remove(self.prazos[i])
                        self.veiculo[veiculo] = self.veiculo[veiculo].replace(self.veiculo[veiculo][-1::], '1')
                        
                    else:
                        print("Nome do Locatario: %s"%(self.prazos[i][2]))
                        print("Veiculo está atrasado, Pagar: %d"%(valor*self.prazos[i][3]+(valor*(dia - diaV))))
                        self.prazos.remove(self.prazos[i])
                        self.veiculo[veiculo] = self.veiculo[veiculo].replace(self.veiculo[veiculo][-1::], '1')

                else:
                    
                    mesA = mes - mesV
                    diasA = 30 - diaV + 30*(mesA-1) + dia
                    print("Nome do Locatario: %s"%(self.prazos[i][2]))
                    print("Veiculo está atrasado, Pagar: %d"%(valor*self.prazos[i][3]+(valor*(diasA))))
                    self.prazos.remove(self.prazos[i])
                    self.veiculo[veiculo] = self.veiculo[veiculo].replace(self.veiculo[veiculo][-1::], '1')
            i += 1
    
    def liberar(self):
        
        veiculo = int(input("Veiculo a ser devolvido: "))
        veiculo -= 1

        i = 0
        while i < len(self.prazos):
            
            print("Veiculo alugado: %d"%(self.prazos[i][0] + 1))
            input()
            
            if self.prazos[i][0] == veiculo:
                self.prazos.remove(self.prazos[veiculo])
                self.veiculo[veiculo] = self.veiculo[veiculo].replace(self.veiculo[veiculo][-1::], '1')
            i += 1    

    def excluir(self):
        
        remover = int(input("Veiculo a ser removido: "))
        remover -= 1

        if self.veiculo[remover][-1::] == '1':
            self.veiculo.remove(self.veiculo[remover])
        
        else:
            print("O veiculo têm rezervas")

