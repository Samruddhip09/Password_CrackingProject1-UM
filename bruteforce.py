import itertools
import string

def brute_force(password):
    chars = string.ascii__lowercase + string.digits

    for i in range(1, 5):
        for guess in itertools.product(chars, repeat=i):
            guess = ''.join(guess)
            if guess == password:
                print("password found:", guess)
                return
            
brute_force("ab1")