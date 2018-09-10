class emp:
   #class variable
   raise_amount = .40
   num_of_employees = 0

   def __init__(self,name, salary):
         self.name = name
         self.salary = salary
         emp.num_of_employees += 1 

   def get_emp(self):
      return "Name: {} - Salary {}".format(self.name, self.salary)

   def give_raise(self):
       return self.salary* emp.raise_amount + self.salary

if __name__ == "__main__":
    emp1 = emp("tanigai", 5000)
    emp2 = emp("tanigai1", 6000)

    print emp1.get_emp()
    print emp2.get_emp()

    print emp1.give_raise()
    print emp2.give_raise()


    print emp1.raise_amount
    print emp2.raise_amount
    print emp.raise_amount

    print emp.__dict__
    print emp1.__dict__
    print emp2.__dict__

    print "*"*30

    emp1.raise_amount = 0.5
   
    print emp1.raise_amount
    print emp2.raise_amount
    print emp.raise_amount

    print emp1.__dict__
    print emp.__dict__
    print emp2.__dict__


    print emp.num_of_employees
