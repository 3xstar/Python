with open ('log.txt', 'r', encoding = 'UTF-8') as file:
    for line in file:
        if 'ERROR' in line:
            print(line)