class emp:
   #class method and static method 
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
   
   @classmethod
   def change_raise(cls, amount):
       cls.raise_amount = amount

   @staticmethod
   def is_holiday(day):
       if day.upper() in ["SATURDAY", "SUNDAY"]:
           return True
       return False
 
       

if __name__ == "__main__":
    emp1 = emp("tanigai", 5000)
    emp2 = emp("tanigai1", 6000)

    print emp1.get_emp()
    print emp2.get_emp()

    print emp1.give_raise()
    print emp2.give_raise()

    emp.change_raise(0.60)

    print "****************After raise ****************"
    print emp1.give_raise()
    print emp2.give_raise()

    print "************Holiday**********"
    print emp.is_holiday("monday")
    print emp.is_holiday("sunday")
