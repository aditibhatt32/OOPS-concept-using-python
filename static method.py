class Player:
    teamName='Liverpool'
    def __init__(self,name):
        self.name=name
    @staticmethod
    def demo():
        print("I am static method")
p1=Player('lol')
p1.demo()
