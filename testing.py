class Company: pass
class Developer(Company): pass
class Entity(Developer): 
    def set(self, key,val):
        return setattr(self, key, val)

c = Company()
d = Developer()
e = Entity()

print(c) #<__main__.Company object at 0x1043a72b0>
print(d) #<__main__.Developer object at 0x1041d2b80>
print(e) #<__main__.Entity object at 0x1041d2730>

#e.__class__.__qualname__ = 'Polluted_Entity'

#print(e) #<__main__.Polluted_Entity object at 0x1041d2730>

#e.__class__.__base__.__qualname__ = 'Polluted_Developer'
#e.__class__.__base__.__base__.__qualname__ = 'Polluted_Company'
#setattr(e, '__getattribute__', lambda f,g: 'Bye!')
#e.set('__qualname__', 'Bye!')
#print(d) #<__main__.Polluted_Developer object at 0x1041d2b80>
#print(c) #<__main__.Polluted_Company object at 0x1043a72b0>

print(dir(e.__class__.__init__))
#print(dir(e.__class__.__base__.__base__))