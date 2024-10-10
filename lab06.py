def print_from_index(s, i):
    n = len(s)
    result = ' '
    print('| ', end='')
    for _ in range(n):
        result += s[i % n]
        print(s[i % n] + ' |', end = ' ')
        i += 1
    return result

def vigenere_sq(alphabet):
    for i in range (0, 26):
        print_from_index(alphabet, i)
        """
        from j in range(0, 26):
            print(f'{alphabet[j%26]', end=' ')
        """
        print ()
def letter_to_in(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i
    return -1

def in_to_letter(alphabet, index):
    if 0 < index < len(alphabet):
        return alphabet[index]
    return -1

def vigenere_in(key, plaintext, alphabet):
    plain_in = letter_to_in(plaintext, alphabet)
    key_in = letter_to_in(key, alphabet)
    c_index = (key_in + plain_in) % len(alphabet)
    return in_to_letter(alphabet, c_index)

def encrypt_vigenere(key, plaintext, alphabet):
    cipheretext = ''
    k_len = len(key)
    for i, l in enumerate(plaintext):
        #print(f'{i}: {key[i%k_len]}: {l}')
        cipheretext += vigenere_in(key[i%k_len], l, alphabet)
    return cipheretext


alphabet = "abcdefghijklmnopqrstuvwxyz "
key = input("Enter a key:")
plaintext = input("enter your plaintext: ")
print(encrypt_vigenere(key, plaintext, alphabet))
#key = 'davinci'
#plain_t = 'the eagle has landed'
#print(vigenere_in(key[0], plain_t[0], alphabet))
#key = 'silver'
#plain_let = 'the eagle has started its journey'

#vigenere_sq(alphabet)