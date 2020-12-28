import cs50

def print_name():
    answer = cs50.get_string("What is your name? \n");
    print(f"hello, {answer}")

print_name()