import unittest;
from numeroromano import converte;

class conversaoTest(unittest.TestCase):
  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');

  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 

  def testUm(self):
    self.assertEqual(1, converte('I'), "Erro ao converter o I")

  def testCinco(self):
    self.assertEqual(5, converte('V'), "Erro ao converter o V")

  def testDois(self):
    self.assertEqual(2, converte('II'), "Erro ao converter o II")

  def testVinteDois(self):
    self.assertEqual(22, converte('XXII'), "Erro ao coverter o XX")

  def testNove(self):
    self.assertEqual(9, converte('IX'), "Erro ao converter o IX")

  def testVinteQuatro(self):
    self.assertEqual(24, converte('XXIV'), "Erro ao converter o XXIV")

  def testMille(self):
    self.assertEqual(1000, converte('M'), "Erro ao converter o C")

if __name__ == "__main__":
  unittest.main()
