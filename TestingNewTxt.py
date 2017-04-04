#test_newtext.py

from c2c import *
import unittest


class TestNewText(unittest.TestCase):
	def test_c2c(self):
		self.assertNotEqual(old_txt, new_txt)

if __name__ == '__main__':
	unittest.main()