import unittest


def solve(phrases: list):
    result = []    
    for phrase in phrases:
        phrase_replace = phrase.replace(' ', '')
        if phrase_replace == phrase_replace[::-1]:
           result.append(phrase)
    return result



class TestSolve(unittest.TestCase):

    def test_solve_func(self):
        """
        Verify that the function correctly returns all palindromic phrases from the input list.
        """
        params = (
            (['шалаш', 'а роза упала на лапу азора', 'пальма'], ['шалаш', 'а роза упала на лапу азора']),
            (['солнце', 'альфа-центавра'], []),
            ([], [])
        )
        for i, (the_list, expected) in enumerate(params):
            with self.subTest(i):
                result = solve(the_list)
                self.assertListEqual(expected, result)