class Apple:

    def __init__(self, color):
        self._color_ = color
    
    @property
    def color(self):
        return self._color_
    
    @color.setter
    def color(self,_color):
        self._color_=_color
        return self._color_

    
a1 = Apple("red")
print(a1.color)
a1.color="blue"
print(a1.color)
        
