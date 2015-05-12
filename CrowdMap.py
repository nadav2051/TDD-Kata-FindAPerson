class CrowdMap():
    def __init__(self, initPostList):
        self.postList = initPostList
        
    def getAllPostsFor(self, name):            
        return [post for post in self.postList if name in post]
    
    def isLocationForName(self, name):
        return True