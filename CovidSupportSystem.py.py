totalSA = 27403
totalUSA = 1700000
totalChina = 82995

while True:
    print("Welcome to the COVID 19 support service. Please select an option below:")
    print("1.Statistics") 
    print("2.Prevention")
    print("3.Symptoms")
    print("4.Treatment")
    print("5.Report Case")
    print("6.Exit")
    enter_choice = int(input("Enter choice(1/2/3/4/5/6): ")) 


    if enter_choice == 1:
        print()
        print("Currently in SA there are " + str(totalSA) + " Confirmed cases.")   # make the numbers changeable obvs and also looped 
        print("Currently in USA there are " + str(totalUSA) + " Confirmed cases.")
        print("Currently in China there are " + str(totalChina) + " Confirmed cases.")
        print()                                                     
        RandomCountryInput = str(input("Would you like to see the Confirmed cases of a random country? y/n "))
        if RandomCountryInput == "y":
            RandomCountry = {0 : "India has 2348787 Confirmed cases",
                 1 : "Singapore has 21 000 Confirmed cases",
                 2 : "New Zealand has 3140 Confirmed cases",
                 3 : "Taiwan has 8100 Confirmed cases",
                 4 : "South Korea has 47770 Confirmed cases",
                 5 : "Brazil has 255500 Confirmed cases", 
                 6 : "Russia has 1000000 Confirmed cases",
                 7 : "Australia has 7155 Confirmed cases",
                 8 : "France has 4738744 Confirmed cases",
                 9 : "UK has 79774 Confirmed cases"}
            chosen_input = int(input("To select a random country, type a number from 0 to 9: "))
            print(RandomCountry[chosen_input])
        if RandomCountryInput == "n":
            print()


    if enter_choice == 2: 
        print("""
        To prevent the spread of COVID-19: 
        Clean your hands often. Use soap and water or an alcohol-based hand rub.
        Maintain a safe distance from anyone who is coughing and sneezing.
        Don't touch your eyes, nose and mouth.
        Cover your nose and mouth with your bent elbow or a tissue when you cough and sneeze.
        Stay home if you feel unwell.
        If you have a fever, cough and difficulty breathing, seek medical attention. Call in adavnce.
        Follow the directions of your local health authority.
        """)

    if enter_choice == 3: 
        print("""    
    Most common symptoms:
    fever
    dry cough
    tiredness
    
    Less common symptoms:
    aches and pains
    sore throat
    diarrhoea
    conjunctivitis
    headache
    loss of taste and smell
    a rash on skin, or discolouration of fingers or toes
    
    Serious symptoms:
    difficulty breathing or shortness of breath
    chest pain or pressure
    loss of speech or movement
    """)

    if enter_choice == 4: 
        print("""
    If you feel sick, drink plenty of fluid, and eat nutritious food. Stay in a separate room
    from other family members, and use a dedicated bathroom if possible. Clean and disinfect
    frequently touched areas
    """)

    if enter_choice == 5:
        symptoms = str(input("Do you have any of symptoms? y/n: "))
        if symptoms == "n":
            print("No COVID")
        if symptoms == "y":
            temperature = str(input("Is your temperature above 38.5°C? y/n: "))
            if temperature == "n":
                print("No COVID")
            if temperature == "y":
                country_census = int(input("""In which country are you select an option below
            1.SA
            2.USA
            3.China
            Enter option(1/2/3): """))
                if country_census == 1:
                    totalSA += 1
                if country_census == 2:
                    totalUSA += 1
                if country_census == 3:
                    totalChina += 1
                print("You have COVID 19 please see Treatment")
    
    if enter_choice == 6:
        break