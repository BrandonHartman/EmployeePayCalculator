# -----------------------------------------------------------------------------
# Programming Project Four
# Brandon Hartman
# December 2nd, 2016
# -----------------------------------------------------------------------------

# Write a program that has either a two dimensional list or four separate parallel
# lists for each type of information to store employee information.
# A main() function that first reads a file of employee data (name, hours, pay rate for
# each employee per line) into list(s). Close the file after reading the into lists. You
# may use the split string function to break a line into name, hours, pay rate. The
# program then enters a loop that ends when 4 is selected by a user and that processes a
# menu of the following items:

# 1. Input employees information
# 2. Compute pay for all employees
# 3. Display payroll report
# 4. Exit

# When the user enters 1 the inputData() function is called passing the list(s) as parameter(s),
# 2 computePay() function is called, and 3 displayPay() function is called. When the user enters
# 4, the program should write the list(s) data to the file by overwriting, and display a message:
# “Thank you for using our payroll application”

# A main() function that first reads a file of employee data (name, hours, pay rate for
# each employee per line) into list(s).


def main():
    # This states that a empty list is created within the main. The empty list will later on
    # store employee names throughout the program. Hence, the employeeNamesList variable name.
    employeeNamesList = []
    # This states that a empty list is created within the main. The empty list will later on
    # store the hours worked throughout the program. Hence, the hoursWorkedList variable name.
    hoursWorkedList = []
    # This states that a empty list is created within the main. The empty list will later on
    # store the employee's pay rate throughout the program. Hence, the payRateList variable name.
    payRatesList = []
    # # This states that a empty list is created within the main. The empty list will later on
    # store the gross pay amount throughout the program. Hence, the grossPayList variable name.
    grossPayList = []
    # The program will start to open the 'employeeFile.txt file inside the computer to read within
    # it. The program uses the open function to read the information from the file. The program
    # uses 'r' to do so.
    employeeFile = open('employeeFile.txt', 'r')
    # This states that it is reading the input that the user typed within the employeeFile and will be
    # finished once the line is read from the project file.
    readingLine = employeeFile.readline()
    # Next within the program states into a while loop breaking down the different indexes and
    # appending the information from the user to the file. The next line will state while
    # readingLine is not empty to do certain programs within the loop.
    while readingLine != "":
        # This line of code states that it will split the ':' away from the users input information
        # from the read line from the employeeFile.
        employeeInfo = readingLine.split(":")
        # This line of code states that it is appending the employeeInfo within the employee
        # namesList and indexing it to the beginning. Which is stated at zero.
        employeeNamesList.append(employeeInfo[0])
        # This line of code states that it is appending the employeeInfo within the hoursWorked
        # List and indexing. Which is stated at one.
        hoursWorkedList.append(employeeInfo[1])
        # This line of code states that it is appending the employeeInfo within the payRates
        # List and indexing. Which is stated at two.
        payRatesList.append(employeeInfo[2])
        # This line of code states that it is appending the employeeInfo within the grossPay
        # List and indexing it. Which is stated at three.
        grossPayList.append(employeeInfo[3])
        # This states that it is reading the input that the user typed within the employeeFile and will be
        # finished once the line is read from the project file.
        readingLine = employeeFile.readline()
    # Afterwards, the program will no longer need the project files. So the program will
    # need to use the .close() function to close the file until being called again by the
    # open() function.
    employeeFile.close()
    # This line of code states that the variable option is equaled to 0. This variable will be the key
    # to loop amongst the users choice through input.
    option = 0
    # Heading into a while loop stating that while option is not equal to four to go throughout
    # the lines of code inside the block of the while loop.
    while option != 4:
        # Displays the interface that the user will see. This will display the ----payroll menu-----.
        print("------------PAYROLL MENU-------")
        # Displays the interface that the user will see. This will display 1. Input employees information.
        print("1. Input employees information")
        # Displays the interface that the user will see. This will display 2. Compute pay for all employees.
        print("2. Compute pay for all employees")
        # Displays the interface that the user will see. This will display 3. Display payroll report.
        print("3. Display payroll report")
        # Displays the interface that the user will see. This will display 4. Exit.
        print("4. Exit")
        # Displays the interface that the user will see. This will display ----------Selection--------.
        print("-------------Selection---------", end="")
        # States that the user will input something and it will get assigned to the variable option.
        # The next sets of code states what happens after the user implies information.
        option = int(input())
        # States the program goes into a if statement saying if the user's information (option) is equal
        # one to head into the inputData function.
        if option == 1:
            # Goes into the inputData function. This also has three parameters as employeeNamesList, hoursWorkedList,
            # payRatesList.
            inputData(employeeNamesList, hoursWorkedList, payRatesList)
        # States the program goes into a elif statement saying if the user's information (option) is equal
        # two to head into the computePay function.
        elif option == 2:
            # Goes into the computePay function. This also has two parameters as hoursWorkedList and
            # payRatesList.
            computePay(hoursWorkedList, payRatesList)
        # States the program goes into a elif statement saying if the user's information (option) is equal
        # three to head into the displayPay function. This will pass four parameters. Known as
        # employeeNamesList, hoursWorkedList, payRatesList and grossPayList
        elif option == 3:
            # Before heading into the displayPay function, the program will go into a if
            # statement claiming if the length of the grossPayList is not equaled to 0 to head into
            # displayPay().
            if len(grossPayList) != 0:
                # Heading to the displayPay function that will pass four parameters. Known as
                # employeeNamesList, hoursWorkedList, payRatesList and grossPayList.
                displayPay(employeeNamesList, hoursWorkedList, payRatesList, grossPayList)
            # Else, if the list is empty. It will display a message stating you cannot display a empty list.
            else:
                # It will display a message stating you cannot display a empty list.
                print("You cannot display a empty list.")
        # Else, if the user response is equal to four. It is assigned to option and displays a exit message and closes.
        elif option == 4:
            # Displays "Thank you for using our payroll application." and exits out of the payroll application.
            print("Thank you for using our payroll application.")
        # This will state that all else fails..To display a Invalid input. Please try again later. Goodbye! message
        else:
            # This will state that all else fails..To display a Invalid input. Please try again later. Goodbye! message
            print("Invalid input. Please try again later. Goodbye!")
    # The program will start to open the 'employeeFile.txt file inside the computer to write within
    # it. The program uses the open function to write the information from the file. The program
    # uses 'w' to do so.
    employeeFile = open('employeeFile', 'w')
    # Heading into a for loop stating for employee in the range and length of employeeNamesList
    for employee in range(len(employeeNamesList)):
        # Writing onto the file as the variable employee and formats the variable inside the employeeNamesList,
        # hoursWorkedList, payRatesList and grossPayList and converts them into strings while being written.
        employeeFile.write("{0}:{1}:{2}\n".format(str(employeeNamesList[employee]), str(hoursWorkedList[employee]),
                                                  str(payRatesList[employee]), str(grossPayList[employee])))

# Heading into the inputData() once it is called within the option loop. The program will start with three
# parameter as well. Known as employeeNamesList, hoursWorkedList and payRatesList.


def inputData(employeeNamesList, hoursWorkedList, payRatesList):
    # First thing that the function will do is state a variable named userResponse and it will
    # get assigned from the input the user implies from "Do you have any employees to enter? (y/n): "
    userResponse = input("Do you have any employees to enter? (y/n): ")
    # Heading into a while statement: While userResponse is equaled to 'y'. Perform the actions below in the
    # block of code.
    while userResponse == "y":
        # Heading into the block of code inside of the while loop for employee information.
        # States the variable employeeNames will be assigned to the users response to the input
        # message containing "Enter employee name: "
        employeeNames = input("Enter employee name: ")
        # This line of code implies that the employeeNames entered will be appended to the
        # employeeNamesList.
        employeeNamesList.append(employeeNames)
        # This will state that the employeeNames will have a function that must declare that the
        # input must be alphabetic.
        while not employeeNames.isalpha():
            # while not alphabetic. It will display a invalid input.
            print("Invalid input. Input must be alphabetic.")
            # while not alphabetic. It will display a invalid input.
            # Goes into a line of code to re-input the employee name.
            employeeNames = input("Re-enter employee name: ")
            # appends the employees name that the user entered into the
            # employeeNamesList.
            employeeNamesList.append(employeeNames)
        # Heading into a variable named as hoursWorked. This assigns the user input as a float
        # and to the variable. The message displayed will be "Enter amount of hours worked: "
        hoursWorked = float(input("Enter amount of hours worked: "))
        # THe input for hoursWorked will append to the hoursWorkedList
        hoursWorkedList.append(hoursWorked)
        # Heading into a variable named as payRate. This assigns the user input as a float
        # and to the variable. The message displayed will be "What is the pay rate?"
        payRate = float(input("What is the pay rate? "))
        # THe input for payRate will append to the payRateList
        payRatesList.append(payRate)
        # The variable userResponse will be assigned as a input from the user displaying
        # a message such as "Do you have more employees to enter? (y/n): "
        userResponse = input("Do you have more employees to enter? (y/n): ")
    # It will continue into a if statement if the users response is "n"
    if userResponse == "n":
        # If userResponse is equal to 'n'. It will display a message saying
        # "Thank you for using our payroll application. Have a wonderful day!"
        # and will exit the program.
        print("Thank you for using our payroll application. Have a wonderful day!")
    # The else statement here states that if all else a invalid input message will appear.
    else:
        # Displays an invalid message displaying "Invalid input.
        # Please try again later. Goodbye!"
        print("Invalid input. Please try again later. Goodbye!")

# Heading into the computePay() once the it is called within the option loop. The
# program will start with two parameter as well. Known as hoursWorkedList and
# payRatesList.


def computePay(hoursWorkedList, payRateList):
    # Once inside the computePay(), it will go into a for stating
    # for employee in the range and length in the payRateList
    for employee in range(len(payRateList)):
        # Within the for loop processes different indexes and goes inside the if
        # statement. If the hoursWorkedList of the employee is greater than
        # forty.
        if hoursWorkedList[employee] > 40:
            # If greater than forty, assigns a variable named overTimePay.
            # That variable is equaled to the work of the hoursWorkedList minus
            # forty times the payRateList times one point five.
            overTimePay = hoursWorkedList[employee] - 40 * payRateList[employee] * 1.5
            # The grossPay of the employee is assigned when its equaled to forty times
            # the payRateList of the employee plus the overTimePay that was assigned
            # in the last line of code.
            grossPay[employee] = 40 * payRateList[employee] + overTimePay
            # The grossPay that was assigned will get appended to the grossPayList
            grossPayList.append(grossPay[employee])
        # Heading into the else statement if the hoursWorked is anything else.
        else:
            # Stating that the grossPay of the employee is assigned and equaled
            # to the hoursWorkedList of the employee plus the payRateList
            # of the employee.
            grossPay[employee] = hoursWorkedList[employee] + payRateList[employee]
            # The grossPay that was assigned will get appended to the grossPayList
            grossPayList.append(grossPay[employee])

# Heading into the displayPay() once the it is called within the option loop. The
# program will start with four parameter as well. Known as hoursWorkedList,
# employeeNamesList, payRatesList and grossPayList.


def displayPay(employeeNamesList, hoursWorkedList, payRatesList, grossPayList):
    # Displaying the Title of the payroll of the DooDad Manufacturing Company in
    # December.
    print("-----------------------DOODAD MANUFACTURING COMPANY DECEMBER PAYROLL------------------------------")
    # Displaying the different sections of the payroll
    # Such as the Employee Name section, hours worked section, pay rate section
    # and the gross pay section.
    print("EMPLOYEE NAME                      HOURS WORKED            PAY RATE                      GROSS PAY")
    # Adding line breakage throughout the sections.
    print("------------------                 -------------           ---------                  ------------    ")

    # The next statement is a for loop stating: For employeeNo in the range and length
    # of the employeeNamesList: To print and format the employeeNamesList, hoursWorkedList
    # , payRateList and grossPayList to the verified area it needs to beat. Afterwards, it
    # will print”---------------“ to add breakage.q
    for employeeNo in range(len(employeeNamesList)):
        print(format(employeeNamesList[employeeNo], '<39s'),
              format(hoursWorkedList[employeeNo], '<20s'),
              format(payRatesList[employeeNo],'<29s'),
              format(grossPayList[employeeNo], '>0s'))
    print("--------------------------------------------------------------------------------------------------")
# This states that the main function is being called and will run whatever is in the
# main function.
main()
