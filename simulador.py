temposProcessos = []
temposTurnaround = []
temposEspera = []
somaBurst = 0

QuantProcesso = int(input("\nQuantos processos deseja simular?\n"))

for i in range(1, QuantProcesso +1):
    tempos = float(input(f"Tempo do Processo {i}: "))
    temposProcessos.append(tempos)

while(True):
    
    algoritimo = input("\nEscolha o algoritmo que deseja usar (Fifo/SJF), F para Fifo e S para SJF:\n")
    
    if algoritimo == 'f':
        for i in range(QuantProcesso):
            if i == 0:
                somaBurst
                temposEspera.append(somaBurst)
            
            else:
                somaBurst += temposProcessos[i -1]
                temposEspera.append(somaBurst)
            
        
        for i in range(QuantProcesso):
            if i == 0:
                temposTurnaround.append(temposProcessos[i])
            else:
                temposTurnaround.append(temposEspera[i] + temposProcessos[i])

        print("\nEscalonamento em Fifo\n")
    
        for i in range(QuantProcesso):
            print(f"\nProcesso {i +1}:")
            print(f"Tempo Turnaround: {temposTurnaround[i]}")
            print(f"Tempo de Espera: {temposEspera[i]}\n ")
            
        break
    
    elif algoritimo == 's':
        
    
    
    
        print 
        break
    else:
        print("\nPor fovaor, digite somente F(FiFo) ou S(SFJ)")
        