class emp:
    # Inheritance and subclass
    raise_amount = .40
    num_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        emp.num_of_employees += 1

    def get_emp(self):
        return "Name: {} - Salary {}".format(self.name, self.salary)

    def give_raise(self):
        return self.salary * emp.raise_amount + self.salary

    def __repr__(self):
        return 'emp({} , {})'.format(self.name, self.salary)

    @classmethod
    def change_raise(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_holiday(day):
        if day.upper() in ["SATURDAY", "SUNDAY"]:
            return True
        return False

class Developer(object, emp):

    def __init__(self, name, salary, skill):
        emp.__init__(self,name, salary)
        self.skill = skill

    def __repr__(self):
        return 'Developer({}, {}, {})'.format(self.name, self.salary, self.skill)

class Manager(emp):
    def __init__(self, name, salary, engineers = None):
        emp.__init__(self, name,salary)
        if engineers:
            self.team = engineers
        else:
            self.team = []

    def get_team(self):
        print "****************Printing team***********************"
        for engineer in self.team:
            print engineer
        print "****************Printing team***********************"


if __name__ == "__main__":
    emp1 = emp("tanigai", 5000)
    emp2 = Developer("tanigai1", 6000, 'Python')
    mgr = Manager("tani,", 7000, [emp2])
    print emp1
    print emp2
    print mgr.get_team()

    print help(Developer)

