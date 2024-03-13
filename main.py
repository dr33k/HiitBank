from tools import register

while True:
    user_response = input("""
            Welcome user, what would you like to do today?
            1. Register
            2. Login
            3. Quit
    """)

    if user_response  == '1':
        print('You entered the Register option')
        register()
    elif user_response == '2':
        print('You entered 2')
    elif user_response == '3':
        print('Bye Bye!')
        break
    else:
        print('Invalid Input!')
