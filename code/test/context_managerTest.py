import unittest
from src.context_manager import retrieve_relevant_context

class TestContextManager(unittest.TestCase):
    def test_retrieve_relevant_context(self):
        context = retrieve_relevant_context("What is AI?")
        self.assertTrue(len(context) > 0)

if __name__ == '__main__':
    unittest.main()
