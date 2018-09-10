class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def function_add(val):
    if val % 2 != 0:
        raise MyError("Not a even number")
    return val

if __name__ == "__main__":
    try:
       va = function_add(2) 
    except MyError as e:
        print "Error {}".format(e)
    else:
        print "Square of {} is {}".format(va, va*va)

