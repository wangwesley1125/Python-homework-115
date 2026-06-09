def try_it(value):
    try:
        x = int(value)
    
    except ValueError:
        print(f'{value} could not be converted to an integer')
    
    else:
        print(f'int({value}) is {x}')

try_it(10.7)
try_it('Python')