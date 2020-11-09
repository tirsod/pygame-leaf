class Scene():
    name = "default"
    objects = []
    def add(self, obj, x, y):
        newobj = obj()
        obj.x = x
        obj.y = y
        self.objects.append(newobj)
        return newobj
    def update(self):
        for gameobj in self.objects:
            gameobj.update()
    def __init__(self, name = "newscene"):
        self.name = name

class SceneManager():
    scene = None
    
    def load(self, scenename, scenes):
        for s in scenes:
            if s.name == scenename:
                self.scene = s
                break
    