with open('awshucks.jpg', 'rb') as file:
    img_data = file.read()

with open('awshucks_copy.jpg', 'wb') as file:
    file.write(img_data)