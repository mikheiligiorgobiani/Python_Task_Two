numbers_list = [2, 12, 9, 27, 13, 25, 45]
for num in numbers_list:
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)