def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class Foo(object):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)