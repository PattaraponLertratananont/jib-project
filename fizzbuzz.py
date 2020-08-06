# fizzbuzz 
# if income value can divide 3 return Fizz
# if income value can divide 5 return Bizz
# if income value can divide 3 and 5 return FizzBizz
# if income value can't divide 3 and 5 return income value

import unittest

def fizzbuzz(number):
    if number == 1:
        return 1
    elif number == 3:
        return 'Fizz'

# Test
class TestFizzBuzz(unittest.TestCase):
    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        # self.assertEqual(result, aspect)
        self.assertEqual(result, 1)

    def test_input_3_should_get_Fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')

if __name__ == '__main__':
    unittest.main()