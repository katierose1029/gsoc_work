class Example(object):
    class_name = 'first_class'
    def name(self):
        return class_name
    print('first_class type(name): ', type(name))

print('first_class type(Example.name): ', type(Example.name))
