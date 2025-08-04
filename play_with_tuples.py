# display (3.99999999999)

def display_floating(value):
    """Display a floating point number with 2 decimal places."""
    # Check if float number
    # Check if float number
    print(type(value))
    if type(value)  is not float:
        raise TypeError("Value must be a float")
    
    value = str(value)
    entire_part, decimal_part = value.split('.')
    new_value =  ','.join([entire_part,decimal_part[:2]])
    print(f"({new_value})")
    return new_value

value = 3.99999999999
display_floating(value)  # Should display (3.99)

liste_des_parametres=[1,2,4,9,16,25,36,49,64,81,100]
print(*liste_des_parametres)