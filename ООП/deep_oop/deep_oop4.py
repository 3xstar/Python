class Write:
    def do(self):
        print("Мы что-то написали!")

class Read:
    def do(self):
        print("Мы что то прочитали!")

def pc_do(self):
    self.do()

computer_do = [Write(), Read()]
for pc in computer_do:
    pc_do(pc)