def get_input():
    number = int(input('Enter a number: '))
    if number < 0:
        print("Negative number entered,ending the program.")
        return
    print(f"You entered:{number}")
    get_input()
get_input()