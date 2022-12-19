import random
import string
# fungsi key key random dengan kode string ascii dengan jumlah 6
def random_string(panjang:int)-> str:
    hasil_key_string = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return hasil_key_string