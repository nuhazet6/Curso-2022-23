class Red:
    def __init__(self,*ips: str):
        self.ips = []
        for ip in ips:
            if Red.is_valid_ip(ip):
                self.ips.append(ip)
            else:
                raise TypeError(f'Ip inválida: {ip}')


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

    @property
    def ips(self) -> list:
        return self.__ips

    @ips.setter
    def ips(self,ips):
        self.__ips = ips
        self.__binary_ips = []
    
    @property
    def binary_ips(self):
        if not self.__binary_ips:
            print('Calculando binario...')
            for ip in self.ips:
                self.__binary_ips.append('.'.join(f'{int(oct):08b}'for oct in ip))
        return self.__binary_ips
    

    
    def __str__(self):
        return '.'.join(self.ip)
    



ip1 = Red('192.12.233.243','192.168.5.13')
print(ip1.binary_ips)