import json
import unittest

from smartcity_product.decorators import required_keys


@required_keys(['phone', 'token'])
def foo1(data):
    return json.dumps(data)


@required_keys([])
def foo2(data):
    return json.dumps(data)


class RequiredKeysTest(unittest.TestCase):

    tests = (
        (foo1, {'phone': 1, 'token': 2}, False),
        (foo1, {'phone': 1, 'test': 2, 'token': 3}, False),
        (foo1, {'test': 2, 'token': 3}, True),
        (foo1, {'phone': 1, 'test': 2}, True),
    )

    def test(self):
        for fn, arg, is_none in self.__class__.tests:
            result = fn(arg)
            self.assertEqual(result is None, is_none)
