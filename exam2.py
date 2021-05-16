class Company:
  def __init__(self, employees):
    self.employees = employees

  def getSalaryForEach(self):
    print("\tIndividual salary for each employee:")
    for e in self.employees:
      print(f'{e.id} {e.name}: {e.getSalary()}')

  def getTotalSalary(self):
    sum = 0
    for e in self.employees:
      sum += e.getSalary()
    print(f'\tTotal salary to be paid for company employees: {sum}')

  def getEmployeeEfficiency(self):
    resultArray = []
    for e in self.employees:
      employeesEfficiency = (e.working_hours / 40) * 100
      resultArray.append([employeesEfficiency, e.name])
    self.sortedArray = sorted(resultArray, reverse=True)


  def getEmployeesEfficiencyTable(self):
    self.getEmployeeEfficiency()
    print("\tIndividual efficiency for each employee:")
    for el in self.sortedArray:
      print(f'{el[1]}: {el[0]}%')

  def getBestWorstEmployeeBasedOnEfficiency(self):
    self.getEmployeeEfficiency()
    print('\tEfficiency best/worst:')
    print(f'Best Efficiency: {self.sortedArray[0][1]} with {self.sortedArray[0][0]}% efficiency')
    print(f'Worst Efficiency: {self.sortedArray[-1][1]} with {self.sortedArray[-1][0]}% efficiency')

class Employee:
	def __init__(self, name, working_hours, idx):
		self.name = name
		self.working_hours = working_hours
		self.id = idx

class Manager(Employee):
	def __init__(self, name, salary, working_hours, idx):
		super().__init__(name, working_hours, idx)
		self.salary = salary

	def getSalary(self):
		return self.salary

class Secretary(Employee):
	def __init__(self, name, salary, working_hours, idx):
		super().__init__(name, working_hours, idx)
		self.salary = salary

	def getSalary(self):
		return self.salary

class SecretaryStandin(Employee):
	def __init__(self, name, working_hours, idx):
		super().__init__(name, working_hours, idx)

	def getSalary(self):
		return self.working_hours * 100

class Seller(Employee):
	def __init__(self, name, salary, sales, working_hours, idx):
		super().__init__(name, working_hours, idx)
		self.salary = salary
		self.sales = sales

	def getSalary(self):
		return self.salary + (50 * self.sales)

class Worker(Employee):
	def __init__(self, name, working_hours, idx):
		super().__init__(name, working_hours, idx)

	def getSalary(self):
		return self.working_hours * 100

# 0 manager, 1 secretary, 2 secretary standin, 3 seller, 4 worker
db = [
  {
    "id": 1,
    "firstname": "Barsbek",
    "lastname": "Kanatkulov",
    "salary": 45000,
    "post": "manager",
    "hours": 18,
    "sales": 0
  },
  {
    "id": 2,
    "firstname": "Alymkul",
    "lastname": "Tilekbaev",
    "salary": 20000,
    "post": "secretare",
    "hours": 38,
    "sales": 0
  },
  {
    "id": 3,
    "firstname": "Aiperi",
    "lastname": "Shalymbekova",
    "salary": 20000,
    "post": "sales",
    "hours": 38,
    "sales": 20
  },
  {
    "id": 4,
    "firstname": "Bakyt",
    "lastname": "Rustamov",
    "salary": 0,
    "post": "worker",
    "hours": 25,
    "sales": 0
  },
  {
    "id": 5,
    "firstname": "Altynai",
    "lastname": "Shirinbaeva",
    "salary": 0,
    "post": "worker",
    "hours": 40,
    "sales": 0
  },
  {
    "id": 6,
    "firstname": "Janar",
    "lastname": "Ryskulov",
    "salary": 0,
    "post": "stdn_secretare",
    "hours": 33,
    "sales": 0
  }
]

workers = []
for person in db:
  try:
    position = person["post"]
  except KeyError:
    print("KeyError occured, skipping to next...")
    continue

  if position == 'manager':
    manager = Manager((person['firstname'] + " " + person['lastname']), person['salary'], person['hours'], person['id'])
    workers.append(manager)
  elif position == 'secretare':
    secretary = Secretary((person['firstname'] + " " + person['lastname']), person['salary'], person['hours'], person['id'])
    workers.append(secretary)
  elif position == 'sales':
    seller = Seller((person['firstname'] + " " + person['lastname']), person['salary'], person['sales'], person['hours'], person['id'])
    workers.append(seller)
  elif position == 'worker':
    worker = Worker((person['firstname'] + " " + person['lastname']), person['hours'], person['id'])
    workers.append(worker)
  elif position == 'stdn_secretare':
    stdn_secretare = SecretaryStandin((person['firstname'] + " " + person['lastname']), person['hours'], person['id'])
    workers.append(stdn_secretare)

mycompany = Company(workers)

#Execution state
print("")
mycompany.getSalaryForEach()
print("")
mycompany.getTotalSalary()
print("")
mycompany.getEmployeesEfficiencyTable()
print("")
mycompany.getBestWorstEmployeeBasedOnEfficiency()
print("")

