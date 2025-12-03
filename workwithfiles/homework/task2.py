def create_duplicate(source, duplicate):
    with open(source, 'rb') as inner_file:
        with open(duplicate, 'wb') as outer_file:
            outer_file.write(inner_file.read()[::-1])

create_duplicate('task2.txt', 'task2_duplicate.txt')
