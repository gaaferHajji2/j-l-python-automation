from unittest import TestCase

from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        b2 = Blog('My Day', 'Jafar-Loka')

        self.assertEqual(b.__repr__(), 'Test By Test Author (0 posts)')

        self.assertEqual(b2.__repr__(), 'My Day By Jafar-Loka (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')

        b.posts = ['Test']

        b2 = Blog('My Day', 'Jafar-Loka')

        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test By Test Author (1 post)')

        self.assertEqual(b2.__repr__(), 'My Day By Jafar-Loka (2 posts)')