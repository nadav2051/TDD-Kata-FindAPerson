import unittest
from CrowdMap import CrowdMap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = CrowdMap()
        
    def test_getAllPostsForName(self):
        posts = self.crowdmap.getAllPostsFor("Or")
        self.assertIn("Or", posts)
        
    def test_getAllPostsForMissingName(self):
        posts=self.crowdmap.getAllPostsFor("Or2")
        self.assertNotIn("Or2",posts)

if __name__ == '__main__':
    unittest.main()