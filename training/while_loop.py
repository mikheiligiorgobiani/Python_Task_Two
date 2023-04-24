is_raining = True
i = 0
while is_raining:
    i += 2
    print(f'I\'m sad {i}')
    if i >= 50:
        is_raining = False
