def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

inner_function() # name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function() # Я в области видимости функции test_function

