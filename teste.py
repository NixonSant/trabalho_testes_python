from unittest import TestCase
from app import conversao

class TestConversao(TestCase):
    def test_deve_retornar_0_quando_receber_32(self):
        self .assertEqual(conversao(32), 0)

    def test_deve_retornar_37_77_quando_receber_100(self):
        self .assertAlmostEqual(conversao(100), 37.77, places=1)
