from caesercipher import CaeserCipher
import unittest

cc = CaeserCipher()

class Testing(unittest.TestCase):
    def testEncoder(self):
        print('Test 1')
        encodedMessage = cc.encoder(1, "Hello World!")
        self.assertEqual(encodedMessage, "Ifmmp Xpsme!")

    def testDecoder(self):
        print('Test 2')
        decodedMessage = cc.decoder(1, "Ifmmp Xpsme!")
        self.assertEqual(decodedMessage, "Hello World!")

    def testNonNumericKey(self):
        print('Test 3')
        encodedMessage = cc.encoder(1.11, "Hello World!")
        self.assertFalse(encodedMessage)

    def testSmallKey(self):
        print('Test 4')
        encodedMessage = cc.encoder(-1, "Hello World!")
        self.assertFalse(encodedMessage)

    def testBigKey(self):
        print('Test 5')
        encodedMessage = cc.encoder(344667, "Hello World!")
        self.assertFalse(encodedMessage)


if __name__ == "__main__":
    unittest.main()
