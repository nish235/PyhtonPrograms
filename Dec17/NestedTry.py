try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10 / 0)
    except ZeroDivisionError:
        print("Inner Except Block")
    finally:
        print("InnerFinally Block")
    print(2/0)
except ZeroDivisionError:
    print("Outer Except Block")
finally:
    print("Outer Finally Block")
