def hello(fx):
    def mfx():
        print("Hello, World!")
        fx()
        print("Thank for using these functions!")
    return mfx
    
@hello
def greet():
    print("Good morning!")

greet()