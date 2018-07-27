import unittest
import multifunc
from prime import is_prime
from prime import next_prime
class TestMultifunc(unittest.TestCase):
	def test_add_2positive_number(self):
		self.assertEqual(multifunc.add(10,5),15)
		
	def test_add_2negative_number(self):
		self.assertEqual(multifunc.add(-5,-5),-10)
	
	def test_add_positive_negative_number(self):
		self.assertEqual(multifunc.add(-5,5),0)
	

	def test_sub_2positive_number(self):
		self.assertEqual(multifunc.sub(10,5),5)
		
	def test_sub_2negative_number(self):
		self.assertEqual(multifunc.sub(-5,-5),0)
	
	def test_sub_positive_negative_number(self):
		self.assertEqual(multifunc.sub(-5,5),-10)
	
	def test_multi_2positive_number(self):
		self.assertEqual(multifunc.multi(10,5),50)
		
	def test_multi_2negative_number(self):
		self.assertEqual(multifunc.multi(-5,-5),25)
	
	def test_multi_positive_negative_number(self):
		self.assertEqual(multifunc.multi(-5,5),-25)
	def test_prime_negative_number(self):
		self.assertFalse(is_prime(-1), msg = 'it is a negative number')
 	def test_prime_for_0_number(self):
		self.assertFalse(is_prime(0))
	def test_prime_for_1_number(self):
		self.assertFalse(is_prime(1))
	def test_prime_for_4_number(self):
		self.assertFalse(is_prime(4))
	def test_prime_for_5_number(self):
		self.assertTrue(is_prime(5))
	def test_next_prime(self):
		self.assertEqual(next_prime(5),7)
if __name__ == '__main__':
	unittest.main()

