contador = 0
while contador < 5:
    print (contador)
    contador += 1
    
    #condição de parada
    if contador == 3:
        break

#três parâmetros: start, stop, step
for i in range(2, 20, 3):
    print(i)