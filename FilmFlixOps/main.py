import printRecords, AddRecord, AmendRecord, DeleteRecord, searchReportRecords

def read_file():
    try:
        with open("FilmFlixOps/mainOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")

# create the menu function 
def members_menu():
    option = 0 # initialise theoption variable with an integere value
    optionsList = ["1","2","3","4","5","6"]

    # assign the  read_file() function to the menuChoices variable 
    menuChoices =  read_file()

    # create a while loop to repeat the code within the bod of while condition
    while option not in optionsList:
        print(menuChoices) # call/invoke read_file() function to the menuChoices variable 

        # re-assign the valeu of the option variable with the input function 
        option = input("Enter an option from the Menu choice above: ")

        # check if the input from the option variable match any of the options 
        # in the optionsList(["1","2","3","4","5","6"]) 
        if option not in optionsList:
            # if the condition above is true execute the code below
            print(f"{option} is not a valid choice! ")
    return option


mainProgram = True # Boolean variabe to toggle True/False

while mainProgram: #While True
    # assign the members_menu() function to the mainMenu variable 
    mainMenu = members_menu()
    
    # use match case 
    match mainMenu:
        case "1": # if case value equals/matches the string value 1 then 
            printRecords.print_records() # call the read_members()  from the readMembers.py file imported at the top
        case "2":
            AddRecord.insert_records()
        case "3":
            AmendRecord.update_records()
        case "4":
            DeleteRecord.delete_records()
        case "5":
            searchReportRecords.search()
        case _:
            #reassign the value of mainprogram to False
            mainProgram = False
input("Press Enter key to exit the program: ")