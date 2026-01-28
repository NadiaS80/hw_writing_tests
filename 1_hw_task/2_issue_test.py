import unittest


def check_triangle(side1: int, side2: int, side3: int):
    if (side1 + side2 <= side3 or side3 + side2 <= side1 or side1 + side3 <= side2) or (side1 <= 0 or side2 <= 0 or side3 <= 0):
        result = "Треугольник не существует"
    elif side1 == side2 == side3 : 
        result = "Равносторонний треугольник"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result


class TestCheck_triangle(unittest.TestCase):

    def test_with_params(self):
        """
        Verify that the triangle type is correctly determined for different combinations of sides.
        """
        params = (
            (30, 30, 30, "Равносторонний треугольник"),
            (130, 10, 80, "Треугольник не существует"),
            (34, 34, 66, "Равнобедренный треугольник"),
            (38, 54, 22, "Разносторонний треугольник")
        )
        for i, (side1, side2, side3, expected) in enumerate(params):
            with self.subTest(i):
                result = check_triangle(side1, side2, side3)
                self.assertEqual(expected, result)