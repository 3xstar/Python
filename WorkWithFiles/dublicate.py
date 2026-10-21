def create_duplicate(source, duplicate):
    with open(source, 'rb') as inner_file:
        with open(duplicate, 'wb') as outer_file:
            outer_file.write(inner_file.read())

create_duplicate('awshucks.jpg', 'awshucks_duplicate.jpg')
