from LocationService import LocationService
class CrowdMap():
    def __init__(self, initPostList):
        self.postList = initPostList
        
    def getAllPostsFor(self, name):            
        return [post for post in self.postList if name in post]
    
    def isLocationForName(self, name):
        locations = LocationService().getLocations()
        posts = self.getAllPostsFor(name)
        for post in posts:
            for location in locations:
                if location in post:
                    return True
        return False
            
        