def outer():
    
    print('print outerFunction')

    def inner():

       print('print innerFunction')        
    inner()


outer()
