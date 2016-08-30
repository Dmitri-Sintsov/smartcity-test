import re
import unittest


def missing_bracket_replace_regex(s):
    regex = re.compile(r'\([^)]*(?!\(.*?\))$')
    return regex.sub('', s)


def missing_bracket_replace(s):
    regex = re.compile(r"([\(\)])")
    matches = list(filter(None, regex.split(s)))
    level = 0
    tokens = []
    for key, match in enumerate(matches):
        token = {'val': match}
        if match == '(':
            token['level'] = level
            level += 1
        elif match == ')':
            level -= 1
            token['level'] = level
        tokens.append(token)
    last_non_closed_index = None
    for key, token in reversed(list(enumerate(tokens))):
        if token['val'] == ')' and token['level'] == 0:
            break
        elif token['val'] == '(':
            last_non_closed_index = key
        elif token['val'] == ')':
            break
    result = matches[:last_non_closed_index]
    return ''.join(result)


class Test01(unittest.TestCase):

    tests = (
        ('qlqksq((ewwe)(pll', 'qlqksq((ewwe)'),
        ('qlqksq((ewwe)(pll)', 'qlqksq((ewwe)(pll)'),
        ('qlqksq((ewwe)(pll))', 'qlqksq((ewwe)(pll))')
    )

    def test(self):
        for test, expected in self.__class__.tests:
            result = missing_bracket_replace(test)
            self.assertEqual(result, expected)
            result = missing_bracket_replace_regex(test)
            self.assertEqual(result, expected)
