def metade(n=0, format=False):
    m = n / 2
    return m if format is False else formatado(n)

def dobro(n=0, format=False):
    d = n * 2
    return d if format is False else formatado(n)

def aumento(n=0, format=False):
    au = n + (n * 10/100)
    return au if format is False else formatado(n)

def disconto(n=0, format=False):
    dis = n - (n * 13/100)
    return dis if format is False else formatado(n)

def formatado(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')
