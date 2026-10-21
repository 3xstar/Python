class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    #Срабатывает при вызове принт для пользователя
    def __str__(self):
        return f"Название книги: {self.name}\nАвтор книги: {self.author}"
    
    #Срабатывает при вызове для отладки
    def __repr__(self):
        return f'({self.name}) ({self.author})'

book1 = Book('Метро', 'Дмитрий глуховский')
print(book1) #Срабатывает __str__()
print([book1]) #Срабатывает __repr__()