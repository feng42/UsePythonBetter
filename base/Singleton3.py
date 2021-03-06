class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(object):
    __metaclass__ = Singleton

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)