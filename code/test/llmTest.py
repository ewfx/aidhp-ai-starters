import unittest
from src.llm import generate_response

class TestLLM(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("What is the capital of France?", "Paris is the capital.")
        self.assertIn("Paris", response)

if __name__ == '__main__':
    unittest.main()
