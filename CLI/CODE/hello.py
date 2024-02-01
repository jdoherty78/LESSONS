
def hello(name, count):
    for i in range(count):
        print(i, "Hey {}".format(name))
        
if __name__ == "__main__":
    hello("Elita", 4)
