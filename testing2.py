class Employee: pass # Creating an empty class

def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)


emp_info = {
    "name":"Ahemd",
    "age": 23,
    "manager":{
            "name":"Sarah"
        },
    "__class__":{
            "__qualname__":"Polluted"
        }
    }


emp = Employee()
merge(emp_info, emp)

print()
print(vars(emp))

print(emp)
print(emp.__class__.__qualname__)

print()
print(Employee)
print(Employee.__qualname__)

#> {'name': 'Ahemd', 'age': 23, 'manager': {'name': 'Sarah'}}
#> <__main__.Polluted object at 0x000001F80B20F5D0>
#> Polluted

#> <class '__main__.Polluted'>
#> Polluted