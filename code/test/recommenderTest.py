import unittest
from src.recommender import get_recommendation

class TestRecommender(unittest.TestCase):
    def test_get_recommendation(self):
        recommendation = get_recommendation("What is the best way to learn Python?")
        self.assertIsNotNone(recommendation)

if __name__ == '__main__':
    unittest.main()
