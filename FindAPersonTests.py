import unittest
from CrowdMap import CrowdMap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        postList = ["Or", 
                    "Or A.",
                    "Misisng Cowboy"]
        self.crowdmap = CrowdMap(postList)
        
    def test_getAllPostsForName(self):
        posts = self.crowdmap.getAllPostsFor("Or")
        self.assertEquals( ["Or", "Or A."], posts)
    
    def test_getAllPostsForNonExistantName(self):
        posts = self.crowdmap.getAllPostsFor("Joe")
        self.assertEquals([], posts)
    
    def test_existingLocatinInformationReturnsTrue(self):
        locationExist = self.crowdmap.isLocationForName("Or")
        self.assertTrue(locationExist)

if __name__ == '__main__':
    unittest.main()