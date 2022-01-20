
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






