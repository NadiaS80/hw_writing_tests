import unittest

def vote(votes):
    a = {}
    for vote in votes:
        if vote not in a:
            a[vote] = 1
        else: 
            a[vote] += 1
    max_value = max(i for i in a.values())
    for key, value in a.items():
        if value == max_value:
            return key



class TestVote(unittest.TestCase):


    def test_vote_max_quantity(self):
        params = (([0, 0, 0, 5, 6, 9], 0),
                  ([-5, 9897, 0, -5, 98], -5),
                  ([], ValueError)
        )
        for i, (the_list, expected) in enumerate(params):
            with self.subTest(i):
                if expected is ValueError:
                    with self.assertRaises(ValueError):
                        vote(the_list)
                else:
                    result = vote(the_list)
                    self.assertEqual(result, expected)