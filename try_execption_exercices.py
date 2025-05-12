import os

def try_error_now(num,deno):
    print("Here")
    try:
        result = num/deno

    except NameError:
        print("Velue not define")
    except TypeError:
        print("num or deno not integer or digit")
    except ZeroDivisionError:
        print("You can not divide by zero")
    except type_the_excpetion_as as return_exception:
        print("The error :",return_exception)

    else:
        print(result)


if __name__ == "__main__":

    try_error_now()
