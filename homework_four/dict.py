# შექმენით dict -ი 2 ლისტისგან
keys: list = ['Ten', 'Twenty', 'Thirty']
values: list = [10, 20, 30]
res = {}
for key in keys:
    for value in values:
        res[key] = value
        break
print(res)

# შეაერთეთ ორი dict -ი
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2) 
print(dict1)

# ამოიღეთ dict -იდან 'history' -ს value
sampleDict = {
    "class":{
       "student":{
          "name":"Mike",
            "marks":{
              "physcs":70,
              "history":80
          }
       }
    }
}
clas = sampleDict.get("class")
student = clas.get("student")
marks = student.get("marks")
history = marks.get("history")
print(history)

#შექმენით dictionary, რომელშიც შეინახავთ იუზერის
#  მიერ შემოტანილ მონაცემებს მის შესახებ და შემდეგ დაბეჭდავთ კონსოლში. 
# (ველების ვალიდაცია: სიყვები უნდა იყოს კაპიტალიზირებულ ფორმატში, მაგ. 
# nick თუ შემოიტანა იუზერმა თქვენ უნდა გადააკეთოთ Nick - ად)
user = {}
for i in range(1):
    user_name = input("please enter name:")
    result = user_name[0].upper() + user_name[1:]
    age = input("please your age:")
    address = input("please your address:")
    result_two = address[0].upper() + address[1:]
    user["UserName"] = result
    user["age"] = age
    user["address"] =  result_two
print(user)


# შექმენით ლისტი, რომელშიც შეინახავთ ქალაქების მონაცემებს 
# (dict -ი გამოიყენეთ). იპოვეთ ამ ქალაქებს შორის, ყველაზე მცირე და 
# ყველაზე ბევრი მაცხოვრებელი რომელ ქალაქებს ყავს და დაწერეთ 
# მათი სახელები კონსოლში (თუ რამდენიმეა მაშინ ისინიც დაწერეთ)
city = {}
for i in range(2):
    city_name = input("please enter name:")
    population = input("please your age:")
    city["city_name"] = city_name
    city["population"] = population 
print(city)


#მოცემულია ლისტი, სადაც წერია თანამშრომლების სახელები, 
# ასევე მოცემულია default dict-ი სადაც წერია "default" მნიშვნელობები.
#  თქვენი დავალებაა შექმნათ ამ თანამშრომლებისთვის ახალი ლისტი, რომელშიც 
# შეინახავთ თანამშრომლის სახელს და + "მიადგამთ" default მნიშვნელობებს.
employees = ['Kelly','Emma','John']
defaults = {"designation": 'Application Developer', "salary": 8000}

user = {}
for i, use in enumerate(employees): 
    user["name"] = use
    for ind, defa in enumerate(defaults):
          user["designation"] = 'Application Developer'
          user["salary"] = 8000
          print(user)
          break
    
#მოცემულია ლისტი, სადაც წერია რა გასაღებები (key) უნდა 
# ამოიშალოს employee dict-იდან.
# ამოშალეთ და დაპრინტეთ დარჩენილი მნიშვნელობები და გასაღებები.
employee = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
}
employee.pop("name")
employee.pop("salary")
print(employee)
