import unittest
from triangle_classifier import classify_triangle, is_valid_triangle, is_right_triangle

class TestTriangleClassifier(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")
    
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 6), "Isosceles")
    
    def test_scalene_triangle(self):    
        self.assertEqual(classify_triangle(2, 4, 5), "Scalene")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle")
    
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "NotATriangle")
    
    def test_valid_triangle(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertFalse(is_valid_triangle(1, 1, 3))
    
    def test_right_triangle_check(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(5, 5, 5))

if __name__ == '__main__':
    unittest.main()
