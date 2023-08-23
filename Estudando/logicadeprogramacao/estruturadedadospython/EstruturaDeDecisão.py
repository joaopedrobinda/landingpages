idade = 18
if idade < 18:
    print("maior de idade")
elif idade == 18:
    print("você em exatamente 18 anos")
else:
    print("menor de idade")
    
#Em uma única linha
a = 10
b = 20
if a < b: print("A é menor que B")

print("A") if a < b else print ("B")

#Com operadores lógicos
if a < b and b < idade:
    print("todas condições verdadeiras")
elif a < b and b > idade:
    print("segunda opção")
    
if a < b or b > idade: print("pelo menos uma condição verdadeira")

if not(a > b): print("negação de true")

print("passei aqui para testar o git")