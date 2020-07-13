from pprint import pprint
from collections import namedtuple
import time
#import multiprocessing
Employees = namedtuple('Employees',['Name', 'Age', 'Type', 'Earnings'])
emp_list = []
inp = int(input("Enter the number of Employees in list"))
for emp in range(inp):
    print(f"{emp+1} Employee:")
    emp_list.append(Employees(Name=input("Enter the Name") , Age=int(input("Enter the Age")) , Type=input("Enter the Type") , Earnings=int(input("Enter the Earnings"))))

new_emp = tuple(emp_list)
pprint(new_emp)

start= time.time()
def transform(x):
    print(f'Processing {x.Name} record')
    return {'Name': x.Name, 'Age':2020-x.Age}
#pool = multiprocessing.Pool()
mapped_emp = tuple(map(transform, new_emp))
end = time.time()

pprint(mapped_emp)
pprint(end-start)
