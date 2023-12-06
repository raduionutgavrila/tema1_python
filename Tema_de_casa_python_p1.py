class Employee:
    """Common base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.emp_count += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.emp_count -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"E03_{department}"  # Prefixăm "e03" la department
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Salary: {self.salary}")
        super().display_employee()#apelez in acelasi timp si metoda pentru
        #employee din baza

    def schimba_departament(self, department):
        #metoda care schimba department-ul si il afiseaza
        self.department=department
        print(f"noul departament este: {department}")

    def test_TeamX(self):
        if self.department=="TeamX":
            print("este in departamenul X!!!")
        else:
            print("nu este")
        



# Creați Y/3 obiecte ale clasei Manager
Y = 9  # Valoarea lui Y- Radu-Ionut
X = 7  # Valoarea lui X- Gavrila

managers = [] #creez o lista cu managers

manager1 = Manager("Manager1", 5000, "Team1")
managers.append(manager1)

manager2 = Manager("Manager2", 6000, "Team2")
managers.append(manager2)

manager3 = Manager("Manager3", 3000, "Team3")
managers.append(manager3)


# Apelați metoda 'display_employee' pentru obiectele din clasa Manager si Employee
for manager in managers:
    manager.display_employee()#afisez datele managerilor


# Afișați valoarea atributului emp_count pentru o instanță a clasei Employee și pentru una a clasei Manager
print(f"Employee Count: {managers[1].emp_count}")
print(f"Manager Count: {managers[0].mgr_count}")

manager1.schimba_departament("TeamX")#apelez metoda de schimabare a departamentului
manager1.test_TeamX



