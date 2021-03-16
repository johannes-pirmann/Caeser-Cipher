class CaeserCipher:

    def encoder(self, key, message):
        self.key = key
        if self.key > 26: 
            print('Key is too big.')
            return
        elif self.key < 0:
            print('Key is too small.')
            return
        elif self.key % 1 != 0:
            print("Key not a number.")
            return
        self.message = message
        encodedMessage = ''

        for l in message:
            if l == ' ':
                encodedMessage += ' '
            elif ord(l) in range(65, 90):
                switchedLetter = ord(l) + self.key
                if switchedLetter > 90:
                    switchedLetter -= 26
                encodedMessage += chr(switchedLetter)
            elif ord(l) in range(97, 122):
                switchedLetter = ord(l) + self.key                 
                if switchedLetter > 122:
                    switchedLetter -= 26
                encodedMessage += chr(switchedLetter)
            else:
                encodedMessage += l
        return encodedMessage

    def decoder(self, key, message):
        self.key = key
        if self.key > 26: 
            print('Key either too big or too small or not a number')
            return

        elif self.key < 0:
            print('Key is too small.')
            return
        elif self.key % 1 != 0:
            print("Key not a number.")
            return
        self.message = message
        encodedMessage = ''

        for l in message:
            if l == ' ':
                encodedMessage += ' '
            elif ord(l) in range(65, 90):
                switchedLetter = ord(l) - self.key
                if switchedLetter < 65:
                    switchedLetter += 26
                encodedMessage += chr(switchedLetter)
            elif ord(l) in range(97, 122):
                switchedLetter = ord(l) - self.key                 
                if switchedLetter < 97:
                    switchedLetter += 26
                encodedMessage += chr(switchedLetter)
            else:
                encodedMessage += l

        return encodedMessage
