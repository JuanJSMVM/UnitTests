"""
Your module description
"""
def sumar(x,y):
    return x+y
def es_primo(x):
    numbers=[x for x in range(2,2000)]
    for i in numbers:
        if(x%i==0 and x!=i):
            return False
    return True        