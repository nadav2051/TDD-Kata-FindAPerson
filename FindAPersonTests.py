import unittest
from CrowdMap import CrowdMap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        postList = ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"]
        self.crowdmap = CrowdMap(postList)
        
    def test_getAllPostsForName(self):
        posts = self.crowdmap.getAllPostsFor("Or")
        self.assertEquals(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"], posts)
    
    def test_getAllPostsForNonExistantName(self):
        posts = self.crowdmap.getAllPostsFor("Joe")
        self.assertEquals([], posts)
    
    def test_existingLocatinInformationReturnsTrue(self):
        locationExist = self.crowdmap.isLocationForName("Or")
        self.assertTrue(locationExist)
        
    def test_nonExistingLocatinInformationReturnsFalse(self):
        locationExist = self.crowdmap.isLocationForName("Lassy")
        self.assertFalse(locationExist)
    
    def test_mapInconsistenciesReturnsTrue(self):
        mapIncosistent = self.crowdmap.mapInconsistenciesExist("Or")
        self.assertTrue(mapIncosistent)
        
    def test_mapIncosistenciesReturnsFalse(self):
        mapIncosistent = self.crowdmap.mapInconsistenciesExist("Lassy")
        self.assertFalse(mapIncosistent)
        
if __name__ == '__main__':
    unittest.main()