class Base1: 
    def __init__(self) -> None: 
        print ('This is base1 init') 
    def which_one_executes(self): 
        print ('Base1 execution') 

class Base2: 
    def __init__(self) -> None: 
        print ('This is base2 init') 
        def which_one_executes(self):
            print ('Base2 execution') 

class Main(Base1, Base2): 
    def __init__(self) -> None: 
        super().__init__() 
        print ('This is main') 
        self.which_one_executes() 

main_obj = Main()
