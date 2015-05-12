class CrowdMap():
    def __init__(self, initPostList):
        self.postList = initPostList
        
    def getAllPostsFor(self, findName):            
        return [post for post in self.postList if findName in post]