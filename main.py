from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,id, name):
        self.employee_id = id
        self.name = name
        
    def display_info(self):
        employee_type = self.__class__.__name__.replace("Employee", "")
        print(f"Mã nhân viên: {self.employee_id} | Tên nhân viên: {self.name:<15} | Loại: {employee_type}")
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate
    
    
class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
    
    def calculate_salary(self):
        return self.allowance
    

def display_employees(employees):
    for value in employees:
        value.display_info()
    
def display_salaries(employees):
    for value in employees:
        print(f"Mã NV: {value.employee_id} | Tên nhân viên: {value.name:<15} | Lương: {value.calculate_salary():,.0f} VND")


def main_menu():
    employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
    ]
    
    while True:
        print("=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        try:
            choice = int(input("Chọn chức năng (1-3):"))
        except ValueError:
            print("Nhập sai định dạng chức năng. Vui lòng nhập lại.")
            return
            
        if choice == 1:
            display_employees(employees)
        elif choice == 2:
            display_salaries(employees)
        elif choice == 3:
            print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
            break 
        else:
            print("Nhập sai chức năng. Vui lòng nhập lại chức năng (Từ 1-3)")
        
main_menu()