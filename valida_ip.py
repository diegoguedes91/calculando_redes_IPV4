from ipv4 import IPV4

def validanumero(valor):
    valor = valor.replace('/','.')
    valor = valor.split('.')
    for i in valor:
        if len(i) > 3:
            return
    return valor

def numero_ip(funcao):
    try:
        grupo1 = int(funcao[0])
        grupo2 = int(funcao[1])
        grupo3 = int(funcao[2])
        grupo4 = int(funcao[3])
        masc = int(funcao[4])

        if not masc <=32 or not masc >= 24:
            return print('Prefixo de máscara inválido')

        ipv4 = IPV4(grupo1, grupo2, grupo3, grupo4, masc)
        ipv4.lista_de_ip()
    except:
        print('Número de ip invalido')