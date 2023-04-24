odd_numbers = [number for number in range(0,1000,2)]
even_numbers = [numbers for numbers in range(1,1000,2)]

res_list = []
for i in range(0, len(odd_numbers)):
    res_list.append(even_numbers[i] ** odd_numbers[i])


print("resultant list is : " + str(res_list))

res_list_two = [i / j for i, j in zip(odd_numbers, even_numbers)]
print("two resultant list is : " + str(res_list_two))





