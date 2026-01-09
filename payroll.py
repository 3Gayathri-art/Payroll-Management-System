def calculate_payroll(basic):
    hra = 0.40 * basic
    da = 0.10 * basic
    gross = basic + hra + da
    pf = 0.12 * basic
    tax = 0.10 * gross
    net = gross - (pf + tax)
    return gross, net

employees = [
    {"id": 101, "name": "Ravi", "basic": 30000},
    {"id": 102, "name": "Sita", "basic": 25000}
]

for emp in employees:
    gross, net = calculate_payroll(emp["basic"])
    print(emp["name"], "Net Salary:", net)
