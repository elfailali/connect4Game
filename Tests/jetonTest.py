import unittest
from Classes.jeton import Jeton


class JetonTestCase(unittest.TestCase):
    # NOMMAGE des tests : test_create_article or
    # First lettre of file name of a class?
    def testShouldCreateNewJetonWithRedColorByDefault(self):
        jeton = Jeton()
        self.assertEqual(jeton.getColor(), "red")

    def testShouldCreateNewJetonWithChosenColor(self):
        jeton = Jeton("blue")
        self.assertEqual(jeton.getColor(), "blue")


if __name__ == '__main__':
    unittest.main()
