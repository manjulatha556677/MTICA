def outer():
    
    message='outer Function'
    print(message)

    def inner():

       print(' inner Function')        
    inner()


outer()
