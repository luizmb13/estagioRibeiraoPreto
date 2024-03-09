def pertence(numero):
    a = 0
    b = 1
    while a < numero:
        a, b = b, a + b
    return a == numero

numero = 6 

if pertence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
