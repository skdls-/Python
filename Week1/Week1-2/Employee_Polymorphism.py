class Employee(object):

    def __init__(self, name):
        self.name = name

    def weeklyPay(hours):
        raise NotImplementedError

    def getName(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, payment_per_hour):
        super().__init__(name)
        self.payment_per_hour = payment_per_hour

    def weeklyPay(self, hours):
        if hours < 40:
            return self.payment_per_hour * hours
        return 3 * self.payment_per_hour / 2 * hours  # 3/2 * hours


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weeklyPay(self, hours):
        return self.salary


class Manager(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary + self.bonus


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
