class IP:
    UPPER_LIMIT_CIDR = 32
    LOWER_LIMIT_CIDR = 8
    NETWORK_OCTET = ['1' * 8] * 4
    ALL_NETWORK = '.'.join(NETWORK_OCTET)
    ALL_HOST = ALL_NETWORK.replace('1','0')
    OCTET_LEN = 8
    
    def __init__(self,ip:str,cidr:int):
        self.ip = ip
        self.cidr = cidr
        

    @property
    def cidr_fixed_index(self):
        '''Propiedad para calcular el índice real del cidr sobre las ips en modo str y binario,
          al tener en cuenta los puntos entre cada octeto y sumarlo al cidr, arreglamos el índice'''
        period_amount = self.cidr // IP.OCTET_LEN 
        return self.cidr + period_amount
   
    @property#Cacheo del binary_ip, ir directamente a binary_ip
    def ip(self) -> list:
        return self.__ip

    @ip.setter
    def ip(self,ip):
        self.__ip = ip
        self.__binary_network = None
    
    @property
    def binary_network(self) -> str:
        if self.__binary_network is None:
            print('Calculando binario...')
            self.__binary_network = '.'.join(f'{int(octet):08b}'for octet in self.ip.split('.'))[:self.cidr_fixed_index]
        return self.__binary_network
    #Fin del cacheo
    
    @property
    def binary_mask(self) -> str:
        return IP.ALL_NETWORK[:self.cidr_fixed_index] + IP.ALL_HOST[self.cidr_fixed_index:]
    
    @property
    def network_id(self):
        return self.binary_network + IP.ALL_NETWORK[self.cidr_fixed_index:]
    
    @property
    def ip_broadcast(self) -> str:
        return self.binary_network + IP.ALL_NETWORK[self.cidr_fixed_index:]
    
    @property
    def ip_router(self) -> str:   
        binary_ip = self.binary_network + IP.ALL_HOST[self.cidr_fixed_index:-1] + '1'     
        return self.binary_ip_2_dec(binary_ip)
    
    @staticmethod
    def binary_ip_2_dec(binary_ip:str) -> str:
        return '.'.join(str(int(octet,2)) for octet in binary_ip.split('.'))

    @staticmethod
    def is_valid_ip(ip):
        if isinstance(ip,str):
            valid_octets = []
            for octet in ip.split('.'):
                if 0 <= int(octet) <= 255:
                    valid_octets.append(True)
                else:
                    return False
            return all(valid_octets) and len(valid_octets) == 4
        else:
            False
    
    def __str__(self):
        return self.ip +"\n"+self.binary_ip
    
    def __len__(self):
        return len(self.ip)


print(IP.ALL_NETWORK,IP.ALL_HOST)
ip1 = IP('192.168.5.12',23)
print(ip1.binary_ip,ip1.binary_ip)
ip1.ip = '192.168.5.14'
print(ip1.binary_ip,ip1.binary_ip)
ip2 = IP('192.168.11.40',20)
print(ip2.cidr)
print(ip2)
print(ip2.binary_mask)
print(ip2.ip_broadcast)
print(ip2.binary_ip_2_dec(ip2.binary_mask))

class Red(IP):
    def __init__(self,*ips: str):
        self.ips = []
        for ip in ips:
            if IP.is_valid_ip(ip):
                self.ips.append(ip)
            else:
                raise TypeError(f'Ip inválida: {ip}')
    