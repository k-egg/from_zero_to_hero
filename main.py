
def function(x):
    print("Hello!")
    return(x)

def make_file():
    f = open("test.txt","w")
    f.write("Hello World!")
    f.close()

make_file()
