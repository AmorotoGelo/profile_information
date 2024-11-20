# Open a text file
with open(".\\user_information.txt", "a") as profile_information:
    # Ask user for informations
    while True:
        try:
            name = input('What is your full name? : ')
            age = int(input('How old are you?: '))
            gender = input('What is your gender identity? : ')
            address = input('Where do you live? : ')
            email = input('What is your email? : ')
            hobbies = input('What are your hobbies? : ')
            personality = input('Are you introvert or extrovert? : ')
            religion = input('What is your religious belief? : ')
            language = input('What languages do you speak? : ')
            nationality = input('What is your nationality? : ')
            favorite_number = int(input('What is your favorite number? : '))
            dream_career = input('What is your dream job? : ')
            dream_destination = input('Where do you want to travel? : ')
            biggest_fear = input('What are you scared the most? : ')
            life_motto = input('What is your life motto? : ')
            break
        except ValueError:
            print('Invalid')                             

# Ask user if want to input info again, exit if not
     