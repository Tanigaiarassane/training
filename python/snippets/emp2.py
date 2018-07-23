class emp:
   def __init__(self,name, salary):
         self.name = name
         self.salary = salary

   def __str__(self):
        return self.name

   def get_emp(self):
      return "Name: {} - Salary {}".format(self.name, self.salary)

if __name__ == "__main__":
    emp1 = emp("tanigai", 5000)
    emp2 = emp("tanigai1", 6000)

    print emp1
    print emp1.get_emp()
    print emp2.get_emp()

