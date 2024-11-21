class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return self.name, self.id

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return "project managed"

    def get_info(self):
        return super().get_info(), self.department

class Technician(Employee):

    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return "maintenance performed"

    def get_info(self):
        return super().get_info(), self.specialization


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)

        self.employee_list = []

    def add_employee(self,spec):
        match spec:
            case "M":
                new_employee = Manager("Manager " + "Name" + str(len(self.employee_list)),"Id" + str(len(self.employee_list)),"Department" + str(len(self.employee_list)))
                self.employee_list.append(new_employee)
            case "T":
                new_employee = Technician("Technician " + "Name" + str(len(self.employee_list)),"Id" + str(len(self.employee_list)),"Specialization" + str(len(self.employee_list)))
                self.employee_list.append(new_employee)
            case "TM":
                new_employee = TechManager("TechManager " + "Name" + str(len(self.employee_list)),"Id" + str(len(self.employee_list)),"Department" + str(len(self.employee_list)),"Specialization" + str(len(self.employee_list)))
                self.employee_list.append(new_employee)
            case _:
                return "Unknown employee type"

    def get_team_info(self,num):
        if len(self.employee_list) > num:
            return self.employee_list[num].get_info()
        else:
            return "Employee not found"

tech_manager = TechManager("Name1",1, "Dep1", "IT")


def tech_manager_interface():
    command = input("Select Command: add,get,exit: ")

    match command:
        case "add":
            print(tech_manager.add_employee(input("Enter employee spec Manager - M, Technician - T, TechManager - TM: ")))
        case "get":
            print(tech_manager.get_team_info(int(input("Enter employee ID: "))))
        case "exit":
            return
        case _:
            print("Unknown command")

    tech_manager_interface()
    return

tech_manager_interface()