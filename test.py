import unittest
import testing
class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param=10
        result=testing.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'assisnation'
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = testing.do_stuff(test_param)
        self.assertEqual(result,'please enter a number')
#unittest.testing()
