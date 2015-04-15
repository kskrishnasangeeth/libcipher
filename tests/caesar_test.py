"""Unit tests for caesar cipher module."""

import unittest
from libcipher.caesar import encrypt
from libcipher.caesar import decrypt


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_no_digits(self):
        encrypted = encrypt("Hello World")
        self.assertTrue(encrypted.replace(" ", "").isalpha())

    def test_encrypt_with_key(self):
        encrypted = encrypt("Hello World", 2)
        self.assertEquals(encrypted, "jgnnq yqtnf")

    def test_encrypt_empty(self):
        encrypted = encrypt("")
        self.assertEqual(encrypted, "")

    def test_decrypt_with_key(self):
        decrypted=decrypt("jgnnq yqtnf",2)
        self.assertEquals(decrypted,"hello world")
        
    
