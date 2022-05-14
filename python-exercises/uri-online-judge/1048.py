salary = input()

salary = float(salary)

if salary > 0 and salary <= 400.00:
    rate = 0.15
elif salary > 400.00 and salary <= 800.00:
    rate = 0.12
elif salary > 800.00 and salary <= 1200.00:
    rate = 0.1
elif salary > 1200.00 and salary <= 2000.00:
    rate = 0.07
elif salary > 2000.00:
    rate = 0.04

salary_raise = salary * rate
new_salary = salary_raise + salary
perc = rate * 100

print("Novo salario: {:.2f}".format(new_salary))
print("Reajuste ganho: {:.2f}".format(salary_raise))
print("Em percentual: {:.0f} %".format(perc))