class Tester:

    def __init__(self, name):    # Добавил self
        self.name = name         # Исправил self.name
        self.deadline = True     # Исправил: self.deadline

    def work_hard(self, deadline=True):
        if deadline:             # Исправил: используем параметр
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')