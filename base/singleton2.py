class Singleton(object):
    def __nem__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__nem__(cls)
        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)