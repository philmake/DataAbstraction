import unittest
import codeTesting


class MySetTest(unittest.TestCase):

    def setUp(self):
        self.mySet = codeTesting.MySet()
        pass

    def test_InsertNotThere(self):
        self.check_empty_do_not_contain(num=3)
        self.mySet.insert(3)
        self.check_set_contains_once(num=3)
        pass

    def test_InsertAlreadyThere(self):
        self.check_empty_do_not_contain(num=3)
        self.mySet.insert(3)
        self.check_set_contains_once(num=3)
        self.mySet.insert(3)
        self.check_set_contains_once(num=3)
        pass

    def check_empty_do_not_contain(self, num=0):
        self.assertEqual(self.mySet.get_size(), 0)
        self.assertFalse(self.mySet.contains(num=num))
        pass

    def check_set_contains_once(self, num=0):
        self.assertEqual(self.mySet.get_size(), 1)
        self.assertTrue(self.mySet.contains(num=num))
        pass

    pass


if __name__ == '__main__':
    unittest.main()
