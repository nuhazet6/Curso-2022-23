class IP:
    def __init__(self, ip: str, cidr: str):
        self.ip = ip
        self.cidr = cidr.strip('/')

    @property
    def binary_ip(self):
        return ".".join([f'{int(octeto):08b}' for octeto in self.ip.split(".")])

    @property
    def mask(self):
        cidr = int(self.cidr)
        mask = []
        for octeto in self.binary_ip.split("."):
            if cidr >= len(octeto) :
                mask.append('1'*8)
                cidr -= 8
            else: 
                mask.append(f'{"1"*cidr}{"0"*(8-cidr)}')
        return ".".join(mask)

    @property
    def broadcasting(self):
        host_part = self.binary_ip[self.mask.find('0'):]
        return self.binary_ip[:self.mask.find("0")] + host_part.replace('0','1')

    @property
    def red(self):
        host_part = self.binary_ip[self.mask.find('0'):]
        return self.binary_ip[:self.mask.find("0")] + host_part.replace('1','0')

    @staticmethod
    def binary2dec(binary):
        return ".".join([str(int(octeto,2)) for octeto in binary.split(".")])

    def __eq__(self,other):
        return self.binary_ip == other.binary_ip

    # def lt(self,other):


    def __repr__(self):
        return f'Binary: {self.binary_ip}\nRealIP: {self.ip}\nBD {self.broadcasting} {IP.binary2dec(self.broadcasting)}\nIDRED {self.red} {IP.binary2dec(self.red)}'

    def __iter__(self):
        return IPIterator(self)

class IPIterator:
    def __init__(self, ip):
        self.ip = ip.ip.split(".")
        self.pointer = 0

    def __next__(self):
        if self.pointer >= len(self.ip):
            raise StopIteration
        current_oct = self.ip[self.pointer]
        self.pointer += 1
        return current_oct

ip1 = IP('192.80.5.125','/20')
print(ip1.mask)
for oct in ip1:
    print(oct)