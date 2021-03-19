class Circle:
    def __init__(self, ban):
        self.ban = ban
    def getTo(self):
        return self.ban * self.ban * 3.14
    
c = Circle(2)
print("원의 면적: {0}".format(c.getTo()))
