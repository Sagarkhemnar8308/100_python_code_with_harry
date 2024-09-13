class Player:
    def __init__(self):
        self._name="sagar" # if have a _name it will acess directly but have __name then it get p1._Player__name
        

p1=Player()
print(p1._name)