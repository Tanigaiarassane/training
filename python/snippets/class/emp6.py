class emp:
    # Special/Dundar functions
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