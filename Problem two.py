class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
        
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
a = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4,"user": person_b}}}

def print_depth(data,n=1):

    for i in data:
        print(i,":",n)
        if isinstance(data[i],dict):
            print_depth(data[i],n=n+1)
        elif isinstance(data[i],Person):
            print_depth(data[i].__dict__,n=n+1)

print_depth(a)
    
