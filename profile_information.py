# Open a text file
with open(".\\user_information.txt", "a") as profile_information:
    # Ask user for informations
    while True:
        try:
            name = input('What is your full name? : ')
            while True:
               try:
                  age = int(input('How old are you?: '))
                  break
               except ValueError:
                  print("Invalid, Please try again")
            while True:  
                 gender = input('Type xy if you are a man, xx if a woman : ')
                 if gender == 'xy':
                   gender = 'Man'
                   break
                 elif gender == 'xx':
                   gender = 'Woman'
                   break
                 else:
                    print('Invalid, input again')     

            address = input('Where do you live? : ')
            hobbies = input('What are your hobbies? : ')

            while True: 
                 personality = input('Type shy if you are introvert, loud if extrovert : ')
                 if personality == 'shy':
                   personality = 'Introvert'
                   break
                 elif personality == 'loud':
                   personality = 'Extrovert'
                   break
                 else:
                    print('Invalid, input again')   
               
            religion = input('What is your religious belief? : ')
            nationality = input('What is your nationality? : ')
            while True:
               try:
                  favorite_number = int(input('What is your favorite number? : '))
                  break
               except ValueError:
                  print("Invalid, Please try again")     
            dream_career = input('What is your dream job? : ')
            
        # Writing informations in text file
            profile_information.write(f'Name: {name}\n')
            profile_information.write(f'Age: {age}\n')
            profile_information.write(f'Gender: {gender}\n')
            profile_information.write(f'Address: {address}\n')
            profile_information.write(f'Hobbies: {hobbies}\n')
            profile_information.write(f'Personality: {personality}\n')
            profile_information.write(f'Religion: {religion}\n')
            profile_information.write(f'Favorite number: {favorite_number}\n')
            profile_information.write(f'Dream career: {dream_career}\n')
            profile_information.write("\n \n")
        
        except ValueError:
         print('Invalid') 

# Ask user if want to input info again, exit if not
        another_entry = input('Do you want to input another one? yes or no : ')
        if another_entry != 'yes':
            break
     