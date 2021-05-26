from time import sleep
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class EmployeeAndSalary:
    def __init__(self):
        self.employee_number = 0
        self.employee_salary_per_hour = 0.0
        self.work_time = 0
        self.monthly_salary = 0.0
        self.questions()

    def questions(self):
        self.info("Informe o Numero do Funcionário")
        self.employee_number = int(input())
        self.info("Informe a quantidade de Horas Trabalhadas")
        self.work_time = int(input())
        self.info("Informe o valor por hora trabalhada:")
        self.employee_salary_per_hour = float(input().replace(".", "").replace(",", "."))

    def calculate(self):
        self.info("Calculando o salário mensal...", slp=True)
        self.calculate_monthly_salary()

    def calculate_monthly_salary(self):
        self.monthly_salary = self.employee_salary_per_hour * self.work_time

    def info(self, msg=None, slp=False):
        if slp:
            sleep(2)
        if not msg:
            print("Preparando as informações ...")
            sleep(2)
            msg = f"""
                Número do Funcionário: {self.employee_number}
                Horário trabalho: {self.work_time}
                Salário: {locale.currency(self.monthly_salary, grouping=True)}
            """
        print(msg)


if __name__ == '__main__':
    employee = EmployeeAndSalary()
    employee.calculate()
    employee.info()

