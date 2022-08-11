# valorlogico = bool(int(input("você está se sentindo bem?")))
# if valorlogico == 'sim' or valorlogico == 'não':
#     print("sim")
# else:
#     print("não")
# print("qual o problema")

# print("fim, do programa") 
# barraDireita = int(input("Botao apertado?")) 
# barraEsquerda = int(input("Botao apertado?"))
# if barraEsquerda and not barraDireita:
#     print("10mg de suco")
# if not barraEsquerda and barraDireita:
#     print("20mg de suco")
# if not barraEsquerda and not barraDireita:
#     print("sem suco suco")
# if barraEsquerda and barraDireita:
#     print("erro")
 
#print("Fim do programa!")
valorLogico = input("você está se sentindo bem?")
if valorLogico == 'sim' or valorLogico == 'não':
        if valorLogico == 'não':
            print("Qual é o problema?")
        else:
            print('Você não respondeu corretamente')

else:
    if valorLogico == 'sim':
        print('Bom para você')
    elif valorLogico == 'não':
        print("Qual o problema?")
    else:
        print('Você não respondeu corretamente')
print ("Fim do programa!")

