import inspect

print(type)
print(dir(type))

for a in inspect.getmembers(type):
    print(a)

print("INIT SIGNATURE")
print(inspect.signature(type.__init__))
print("NEW SIGNATURE")
print(inspect.signature(type.__new__))

