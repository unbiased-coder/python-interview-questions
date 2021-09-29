fib = lambda limit: limit if limit < 2 else fib(limit-1) + fib(limit-2) 
print ('Fib(20): ', fib(20))
print ('Fib(10): ', fib(10))
