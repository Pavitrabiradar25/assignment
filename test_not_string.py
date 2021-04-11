import unittest
import not_string

class Testnot_string(unittest.TestCase):

	def test_notstring(self):
		self.assertEqual(not_string.notstring('candy'),'notcandy')
		self.assertEqual(not_string.notstring('x'),'notx')
		self.assertEqual(not_string.notstring('notbad'),'notbad')

if __name__ == '__main__':
	unittest.main()