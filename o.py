with open('sequential_numbers.txt', 'w') as file:
    for i in range(100000000):
        file.write(f'{i:08d}\n')
