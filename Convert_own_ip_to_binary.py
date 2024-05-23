import socket

def get_ip():
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.connect(("8.8.8.8", 80))
     return s.getsockname()[0] 
     s.close()

def convert_to_ip(binary_array):    
     binary_string = ''.join(binary_array)
     octets = [binary_string[i:i+8] for i in range(0, 32, 8)]
     binary_ip = "{}.{}.{}.{}".format(octets[0],octets[1],octets[2],octets[3])
     return binary_ip



splittet_str_ip = list(map(int, get_ip().split(".")))


Bit = [128,64,32,16,8,4,2,1]


Binary_array = []
for oktet in splittet_str_ip:
     for Bit_i in Bit:
          if oktet >= Bit_i:
               Binary_array.append("1")
               oktet = oktet - Bit_i
          else:
               Binary_array.append("0")

print(convert_to_ip(Binary_array))
