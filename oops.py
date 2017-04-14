class test:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print self.name


if __name__ == "__main__":
   a = test("tanigai")
   print a.get_name() 

