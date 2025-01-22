"abcdefghijklmnopqrstuvwxyz"
"aefjhlmqlpquswxbtxycaefjeijnlpqujT"

"abcdabcdabcd"
"aefjdhimdhim"

"aaaaaaaaa"
"addgdggjd"

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


As = "addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj"
Bs = "beehehhkehhkhkknehhkhkknhkknknnqehhkhkknhkknknnqhk"
Cs = "cffifiilfiilillofiililloilloloorfiililloillolooril"

def print_diffs():
    for (a, b, c) in zip(As, Bs, Cs):
        print(a, b, c)
        [a, b, c] = [ord(x) for x in [a,b,c]]
        print(a, b, c)
        print(a - b, b - c)
        print()

def diff(letter, base_letter):
    return ord(letter) - ord(base_letter)


def print_offsets():
    for (a, b, c) in zip(As, Bs, Cs):
        print(diff(a, "a"), diff(b, "b"), diff(c, "c"))

offsets = [diff(a, "a") for a in As]

def encrypt_letter(letter, index):
    return chr(ord(letter) + offsets[index])

def encrypt(msg: str) -> str:
    return "".join(encrypt_letter(ch, i) for (i, ch) in enumerate(msg))

# print(As)
# print(encrypt("a" * 50))


def decrypt_letter(letter: str, index: int) -> str:
    return chr(ord(letter) - offsets[index])

def decrypt(msg: str) -> str:
    return "".join(decrypt_letter(ch, i) for (i, ch) in enumerate(msg))

ENCRYPTED_PW = "lxpyrvmgduiprervmoqkvfqrblqpvqueeuzmpqgycirxthsjaw"

print(ENCRYPTED_PW)
print(decrypt(ENCRYPTED_PW))
print(encrypt(decrypt(ENCRYPTED_PW)))
