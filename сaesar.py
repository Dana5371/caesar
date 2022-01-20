class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        encoded_text = ''
        ord_first_letter_lower = ord('a')
        for i in plainText:
            if i in self._alphabet:
                encoded_text += chr(((ord(i) - ord_first_letter_lower + self._shift) % 26) + ord_first_letter_lower)
            else:
                encoded_text += i
        return encoded_text

alphabet = CesarCipher()
alphabet.set_alphabet('abcdefghijklmnopqrstuvwxyz')
alphabet.set_shift(3)
print(alphabet.encode('The quick brown fox jumps over the lazy dog'))