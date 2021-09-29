class TestClass(object):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def test_class_method(cls):
        print ('this is a class method')
        print ('instance is: ', cls)

    @staticmethod
    def test_static_method():
        print ('this is a static method')
        print ('static methods have no instances')

    def test_regular_method(self):
        print ('this is a regular method')
        print ('instance is: ', self)

TestClass.test_static_method()
TestClass.test_class_method()

try:
    TestClass.test_regular_method()
except TypeError:
    print ('Failed executing regular method, regular methods need an instance to be executed')

t = TestClass()
t.test_regular_method()
