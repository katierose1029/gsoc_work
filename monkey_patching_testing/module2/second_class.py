# from module1.first_class import Example
import module1.first_class as Example1

class Example(object):
    class_name = 'second_class'
    def name(self):
        return class_name
    print('second_class type(name): ', type(name))

print('second_class type(Example.name): ', type(Example.name))

print('Example1.Example before patching: ', Example1.Example)
Example1.Example = Example
print('Example1.Example after patching: ', Example1.Example)
