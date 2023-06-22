def my_decorator(func): 
    def wrapper():
        print('Calling func : ' + func.__name__)
        func()
    return wrapper;


@my_decorator
def do_this(): 
    print('Doing this')
    
@my_decorator
def do_that(): 
    print('Doing that')


do_this()
do_that()