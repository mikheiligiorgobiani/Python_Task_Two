# დაწერეთ კოდი, რომელიც შემნის 1000 ელემენტიან ლისტს, სადაც იქნება მხოლოდ მარტივი რიცხვები 
# (Prime Numbers, რიცხვები, რომლებიც იყოფა მხოლოდ 1-ზე და თავის თავზე)
prime_numbers = [
       number 
       for number in range(1000)
]
for num in prime_numbers:
    if all(num%i!=0 for i in range(2,num)):
       print (num)


# კოდის აღწერა

# პირველ რიგში შექმნილია ორ განზომილებიანი ლისტი რადგან ლისტში გვაქვს ლისტი
# ლისტის ელემენტი არის ლისტი რომელიც ინახავს სტრინგის და ინტის ტიპის მონაცემებს
#  შემდეგ for ციკლით ხდება იტერაცია ვიყნებთ enumerate ფუნქციას რომელიც ჩაშენებულია პითონში და გვეხმარება
# გადანომროს თითეული იტერაციის შედეგად მიღებული შედეგი
# შემდეგ გამოგვაქვს output_ში პროდუქტი რომელ ინდექსზეა დასახელება და ფასი, მინიჭებულ ხაზზე
# შემდეგ input()_ის საშუალებით ტერმინალიდან მომხმარებელი ირჩევს პროდუქტს , product to purchase არის თავდაპირველად none ანუ არაფერი
# შემდეგ ვიყენებთ isdigit() მეთოდს რომელიც აბრუნებს ბულიანს ანუ თუ ყველას სიმბოლო არის ციფრი true_ს სხვა შემთხევაში false_ს
# შემდეგ მოწმდება მომხმარებლის მიერ შეყვანილი მნიშნველობა თუ მისი შეყვანილი მნიშვნელობა ნაკლებია ან ტოლი პროდუქტების length_ზე
# მაშინ output_ში გამოჩნდება არჩეული პროდუქტი, წინააღმდეგ შემთხევაში Selected Product Does Not Exist


# წინა დავალებაში მოცემული ლისტის გამოყენებით,
# იპოვნეთ პროდუქტი სახელის მიხედვით

products = [
    ["google", 1000],
    ["Macbook", 3455],
    ["Chevy", 15000],
    ["Microsoft", 3422]
]

product_to_purchase = None
chosen_product = input("Chosen Product :")
for i, product in enumerate(products):
    if chosen_product in product:
        product_to_purchase = product
    
if product_to_purchase is None:
    print('selected product does not exist')
else:
    print(f"you have chosen {product_to_purchase[0]}, price: {product_to_purchase[1]} USD")


#დაწერეთ კოდი, რომელშიც გექნებათ მომხმარებლების სია:

import getpass
users = [
   ["misho", "123"],
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]
user_name = input('name entered please:')
password = getpass.getpass('password entered please:')
for i, user in enumerate(users):
    if user_name in user:
        if password in user:
            print("You have been successfully authorized")
    else:
        quit()

# წინა დავალებებში დაწერილი კოდი (პროდუქტის არჩევაზე და მომხმარებლის ავტორიზაციაზე) 
# გამოიყენეთ და მომხმარებელს პროდუქტი აარჩევინეთ 
# მხოლოდ იმ შემთხვევაში თუ ავტორიზაცია გავლილი აქვს.
import getpass
users = [
   ["misho", "123"],
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]
products = [
    ["google", 1000],
    ["Macbook", 3455],
    ["Chevy", 15000],
    ["Microsoft", 3422]
]
product_to_purchase = None
user_name = input('name entered please:')
password = getpass.getpass('password entered please:')
for i, user in enumerate(users):
    if user_name in user:
        if password in user:
            chosen_product = input("Chosen Product :")
            for i, product in enumerate(products):
               if chosen_product in product:
                product_to_purchase = product
                print("You have been successfully authorized")
            if product_to_purchase is None:
               print('selected product does not exist')
            else:
              print(f"you have chosen {product_to_purchase[0]}, price: {product_to_purchase[1]} USD")
    else:
        quit()


# ბალანსი ჩაამატეთ შესაბამის ინექსზე users ლისტში
# (მაგ. განახლებულ ლისტში მეორე ინდექსე მდგომ 
#   ელემენტს ასეთი სახე უნდა ჰქონდეს ["james123", "c5bt43f4", 12000])
users = [
["Legend27", "a1s2d3f4"],
["james123", "c5bt43f4"],
["DaveIsGreat", "wlervtb3r"]
]

balances = [
150000,
12000,
19000
] 
for i, user in enumerate(users):
    for j, bala in enumerate(balances):
        if j == i:
            user.append(bala)
            print(user)

# შეავსეთ ლისტი იმ ასოებით, რომლებიც აკლია პირველიდან ბოლო ელემენტამდე 
alphabet_part = ['c', 'h', 'e']