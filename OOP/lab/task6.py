class Task:
    def __init__(self, title, priority, status):
        self.title = title
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self, list_of_tasks):
        self.list_of_tasks = list_of_tasks

    def __getitem__(self, index):
        for i in self.list_of_tasks:
            return i[index]

    def __setitem__(self, key, value):
        for i in self.list_of_tasks:
            i[key] = value

    def __iter__(self):
        for i in self.list_of_tasks:
            return iter(i)

    def add_with_sort(self, task):
        if task.priority == "high":
            self.list_of_tasks.insert(0, task)
            print(f"Задача {task.title} добавлена в начало списка")
        if task.priority == "middle":
            self.list_of_tasks.insert(len(self.list_of_tasks)//2, task)
            print(f"Задача {task.title} добавлена в середину списка")

        if task.priority == "low":
            self.list_of_tasks.append(task)
            print(f"Задача {task.title} добавлена в конец списка")

    def complete(self, task, complete_tasks):
        complete_tasks.append(task)
        print(f"Задача: {task.title} добавлена в выполненные")

# ЗА ЛОР ТАСКОВ СПРАШИВАТЬ У НИКИТЫ ГРИГОРЬЕВА
kesha = Task("Любить клетку", "low", "Пока не станет радужкой")
kesha_transformation = Task("Трансформироваться в радужку", "middle", "Медленно но верно")
raduzhka = Task("Страпонить попугаев", "high", "Всегда в силе")
l_o_t = []
manager = TaskManager(l_o_t)

manager.add_with_sort(kesha)
manager.add_with_sort(kesha_transformation)
manager.add_with_sort(raduzhka)
