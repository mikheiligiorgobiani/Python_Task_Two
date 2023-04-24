# 1
#  როგორ შევქმნნათ ლისტი (მასივი)?
a = []

# 2
# საიდან იწყება მასივის ინდექსების ათვლა
0

#3
# ლისტზე (მასივზე) ელემენტზე წვდომა როგორ ხდება? 
# (დაწერეთ მაგალითი, ჩავთვალოთ გვაქვს ცვლადი arr რომელიც ლისტის ტიპისაა)
arr = ["tom", "jane", "josh","jack"]
print(arr[0])

# 4
# რა არის Index Error?
# index error_ი არის შეცდომა რომელიც მაშინ ამოვარდება როდესაც ჩვენ ვცდილობთ მივწვდეთ ლისტიდან ან სხვა მონაცემთა სტრუქტურიდან იმ ინდექს რომელიც არ არის სიაში

# 5
# როგორ ხდება ლისტში (მასივში), ელემენტების ჩამატება?
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# 6 
# როგორ გავიგოთ ლისტის ზომა?
fruits = ['apple', 'banana', 'cherry']
print(len(fruits))

# 7
# დაბეჭდეთ თითოეული მასივის ელემენტი ტერმინალში (გამოიყენეთ for ან while ციკლი)
fruits = ['apple', 'banana', 'cherry', 'orange']
for i in fruits:
    print(i)

# 8
# დაბეჭდეთ კენტ ინდექსზე მდგომი  მასივის ელემენტები ტერმინალში
number = [ 1, 2, 3, 5, 43, 32, 21, 9]
for i in range(1, len(number), 2):
    print(number[i])

# 9 
# დათვალეთ ტერმინალიდან შემოტანილი ათი რიცხვის ჯამი (hint: არ შექმნათ 10 ცვლადი)
input_int_array = [int(i) for i in input('please write ten number').split()]
result = sum(input_int_array)
print("total:",  result)

# 10
# შექმენით 10 ელემენტიანი ლისტი და შეავსეთ კლავიატურიდან შეტანილი მთელი რიცხვებით. შემდეგ თითოეული ელემენტი ლისტში აიყვანეთ მომდევნო ინდექსზე მდგომი ელემენტის ხარისხში (ბოლო ინდექსზე მდგომი ელემენტი აიყვანეთ პირველი ელემენტის ხარისხში)
inp_numbers = []
for i in range(10):
    number = int(input('enter number'))
    inp_numbers.append(number)
print(inp_numbers)

# 11
# რას აკეთებს for else?
for i in range(6):
  print()
else:
  print("finished!")
# else შესრულდება მაშინ როდესაც ციკლი დასრულდება

# 12
#გაარკვიეთ ლისტში არსებობს თუ არა 1 მარტივი რიცხვი მაინც, შეეცადეთ კოდი იყოს ოპტიმიზირებული, ანუ რაც შეიძლება ნაკლები იტერაცია იყოს!. (hint: for else, break)
numbers_list = [2, 12, 9, 27, 13, 25, 45]
for num in numbers_list:
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)