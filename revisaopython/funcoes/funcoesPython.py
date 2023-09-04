def minhafuncao(nome, sobrenome):
    print("seu nome é :" + nome, sobrenome)
    
minhafuncao("joao pedro", "binda da silva")

def funcao(x):
    return 5 * x
print("retorno de funcao", funcao(3))

#lambida = função anônima
x = lambda a: a + 10
print("lambida ", x(5))

def minhaFuncaoLambida (n):
    return lambda a: a * n
dobrarValor = minhaFuncaoLambida(2)
print("lambida dentro da funcao ",dobrarValor(10))

