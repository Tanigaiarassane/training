class employee:
    raise1 = 0.15
    def __init__(self,name, salary):
        self.name = name 
        self.salary  = salary 

    def hike(self):
       return raise1*salary + salary
    
    def __str__(self):
        return self.name


if __name__ == "__main__":
    tan = employee("tanigai", 24000)
    print tan
    tan.hike()
