# Curso de Python 3 do Básico ao Avançado 
#### Desafio: Calculando redes IPV4

Criar um programa que obtem um numero de IP com o prefixo da mascara de rede. 

### O sistema irá calcular: 

* O IP da mascara de Rede
* Primeiro IP 
* Ultimo IP 
* Total de hosts
* IP e Mascara de rede convertidos em Binários

## Solução: 

Abaixo as funções vão receber a entrada de informção, a função _validanumero_ tira os "." e '/" tornando uma lista com 5 itens, verificando se cada item não passa de 3 caracteres.

A função _numero_ip_ converte cada membro da lista gerada em numero inteiro e verifica se o prefixo da mascara é valido.

```python
from valida_ip import validanumero, numero_ip

print('Digite um endereço IP e o prefixo da mascara de rede:')
ip = input()
numero_ip(validanumero(ip))
```

```python
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
```

Após a validação do numero IP é passado pelas funções _converter_para_binario_ e _binario_mascara_de_rede_ para a conversão do IP e mascara de rede em binário. </br>
A função _ip_mascara_de_rede_ gera uma nova mascara de rede e _numerodehost_ gera o numero de Host que pode setar IP. 

```python
CALCULAR = [128, 64, 32, 16, 8, 4, 2, 1]

class IPV4:
    def __init__(self, grupo1, grupo2, grupo3, grupo4, mascarasubrede):
        self.grupo1 = grupo1
        self.grupo2 = grupo2
        self.grupo3 = grupo3
        self.grupo4 = grupo4
        self.mascarasubrede = mascarasubrede

    def converter_para_binario(self,valor):
        valor = bin(valor).zfill(8)
        valor = valor.replace('b','0')
        return valor

    def binario_mascara_de_rede(self):
        novamascara = ''
        valor = 8 - (32 - self.mascarasubrede)
        for i in range(valor):
            novamascara += '1'
        novamascara = '{:0<8}'.format(novamascara)
        return novamascara

    def ip_mascara_de_rede(self):
        ipmasc = 0
        for i in range(8):
            if self.binario_mascara_de_rede()[i] == '1':
                ipmasc += CALCULAR[i]
        return ipmasc

    def numerodehost(self):
        hosts = (2**(32 - self.mascarasubrede)) - 2
        return hosts

    def lista_de_ip(self):
        if not self.grupo4 > self.numerodehost():
            ip1 = self.converter_para_binario(self.grupo1)
            ip2 = self.converter_para_binario(self.grupo2)
            ip3 = self.converter_para_binario(self.grupo3)
            ip4 = self.converter_para_binario(self.grupo4)
            masc = self.binario_mascara_de_rede()
            print('#' * 56)
            print(f'# IP: {self.grupo1}.{self.grupo2}.{self.grupo3}.{self.grupo4}/{self.mascarasubrede}\n'
                f'# REDE: {self.grupo1}.{self.grupo2}.{self.grupo3}.0/{self.mascarasubrede}\n'
                f'# MÁSCARA: 255.255.255.{self.ip_mascara_de_rede()}\n'
                f'# PRIMEIRO IP: {self.grupo1}.{self.grupo2}.{self.grupo3}.1/{self.mascarasubrede}\n'
                f'# ÚLTIMO IP: {self.grupo1}.{self.grupo2}.{self.grupo3}.{self.numerodehost()}/{self.mascarasubrede}\n'
                f'# Nº DE IPs: {self.numerodehost()}')
            print('#' * 56)
            print(f'# Números em binários: \n'
                  f'# IP: {ip1}.{ip2}.{ip3}.{ip4}\n'
                  f'# Mascara de rede: 11111111.11111111.11111111.{masc}')
        else:
            print('Número de ip invalido')
```

## Terminal:

![imagem do terminal](https://github.com/diegoguedes91/caculando_redes_IPV4/blob/main/output.png)
