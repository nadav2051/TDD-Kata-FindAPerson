from LocationService import LocationService
class CrowdMap():
    def __init__(self, initPostList):
        self.postList = initPostList
        
    def getAllPostsFor(self, name):            
        return [post for post in self.postList if name in post]
    
    def isLocationForName(self, name):
        locationList = LocationService().getLocations()
        postList = self.getAllPostsFor(name)
        for post in postList:
            for location in location:
                if location in post:
                    return True
        return False
    
    def mapInconsistenciesExist(self, name):
        locations = []
        appearnces = 0
        if appearnces > 1:
            return True
        else:
            return False
            
        