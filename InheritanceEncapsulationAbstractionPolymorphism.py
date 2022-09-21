class Horse:
    def __init__(self, name, style):
        self.name = name
        self.style = style

    def print_name(self):
        print(self.name, self.style)


class Thoroughbred(Horse):
    pass


class Arabian(Horse):
    def __int__(self, name, style):
        super.__init__(self, name, style)

    def print_name(self):
        print('Arabian sub class: ', self.name)


p = Arabian('Godolphin', '1724')
p.print_name()
