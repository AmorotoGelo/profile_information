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
            
                                    
        
        # Writing informations in text file
            profile_information.write(f'Name: {name}\n')
            profile_information.write(f'Age: {age}\n')
            profile_information.write(f'Gender: {gender}\n')
            profile_information.write(f'Address: {address}\n')
            profile_information.write(f'Email: {email}\n')
            profile_information.write(f'Hobbies: {hobbies}\n')
            profile_information.write(f'Personality: {personality}\n')
            profile_information.write(f'Religion: {religion}\n')
            profile_information.write(f'Language: {language}\n')
            profile_information.write(f'Favorite number: {favorite_number}\n')
            profile_information.write(f'Dream career: {dream_career}\n')
            profile_information.write(f'Dream destination: {dream_destination}\n')
            profile_information.write(f'Biggest_fear: {biggest_fear}\n')
            profile_information.write(f'Life motto: {life_motto}\n')
        

        except ValueError:
         print('Invalid') 

# Ask user if want to input info again, exit if not
        another_entry = input('Do you want to input another one? : ')
        if another_entry != 'yes':
            break
     