import re
import unittest


def is_valid_password(passwd):
    return re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$', passwd) is not None


class Test02(unittest.TestCase):

    tests = (
        ('a', False),
        ('1', False),
        ('-', False),
        ('--------', False),
        ('----a---', False),
        ('----1---', False),
        ('----A---', False),
        ('1------a', False),
        ('a--A---1', True),
        ('-1--A-a-', True),
        ('-1----a------------A', True),
        ('----a----------------', False)
    )

    def test(self):
        for test, expected in self.__class__.tests:
            result = is_valid_password(test)
            self.assertEqual(result, expected)
