Problem Definition
----------------------------------------
The goal of this programming assignment is to enable the student to practice programming using functions and lists.
Write a program that has either a two dimensional list or four separate parallel lists for each type of information to store employee information.

The program will have four functions that do the following: A main() function that first reads a file of employee data (name, hours, pay rate for each employee per line) into list(s).

Close the file after reading the into lists. You may use the split string function to break a line into name, hours, pay rate.
The program then enters a loop that ends when 4 is selected by a user and that processes a menu of the following items: 1. Input employee’s information, 2. Compute pay for all employees, 3. Display payroll report and 4. Exit.

When the user enters 1 the inputData() function is called passing the list(s) as parameter(s), 2 computePay() function is called, and 3 displayPay() function is called. When the user enters 4, the program should write the list(s) data to the file by overwriting, and display a message: “Thank you for using our payroll application”.

An inputData() function has a loop. Inside the loop are statements to input employee name, hours worked and pay rate for one employee and save them in the list(s). The loop repeats to read multiple employee information until a user enters ‘n’ in response to the question, “Do you have more employees to enter? (y/n).” 

A computePay() function to calculate the gross amount to be paid to each employee and save the amount in the list based on the formula: a) For the first 40 hours, the rate is the given rate; b) For hours over 40, the rate is 1.5 times the given rate. A displayPay() function loops through the two dimensional list (or parallel lists) to display a table.

Analysis
----------------------------------------
We have picked Python as our language for this project because we are currently learning the programming language in class. The program will head into the main() section that will host the other three sections that develop the program as needed. The other sections will be named computePay(), inputData() and displayPay() and these sections will hold the content that must be applied to create the program project.

However, the program will not until the main() is called in the program. Once called into play, the main will create four empty list named employeeNameList, hoursWorkedList, payRatesList and grossPayList. This states that an empty list is created within the main. After the empty lists are created, the program will start to open the ‘employeeFile.txt file inside the computer to read within it. The program uses the open function to read the information from the file. The program uses ‘r’ to do so. Afterwards the program will .readline the employee file. This states that it is reading the input that the user typed within the employeeFile and will finish once the line is read from the project file. 

Next within the program states into a while loop breaking down the different indexes and the appending the information from the user to the file. The next line will state while readingLine is not empty to do a certain process within the loop. After that a variable called employeeInfo will be assigned to the last variable readingLine and will split what the variable contains. Which is ‘:’ in the variable. This will state the line of code will split the ‘:’ away from the users input information from the readline within the employee file.

The next lines of code will append the variable to the correct index and list. First, it starts appending the employeeInfo within the employeeNamesList and indexing it to the beginning. Which is stated at zero. Second, the program will append the employeeInfo within the hoursWorkedList and index it at the first spot.

Third, the line of code states that it is appending the employeeInfo within the payRateList and indexing it to the second index. Lastly, the line of code states that it is appending the employeeInfo within the grossPayList and indexing it. Which is stated at the third index. Finally, the employeeFile will dot notation to readline to read the input that the user typed within the employeeFile and finishes once the line is read from the project file. Afterwards, the program will no longer need the project files. So the program will need to use the .close() function to close the file until being called again by the open() function.

After the closing the file, the program will state the variable named option is equaled to 0. This variable will be the key to the loop amongst the user choices through input.  Afterwards, the program will head into a while loop stating that while option is not equal to four to go throughout the lines of code inside the block of the while loop. The program then enters a loop that ends when 4 is selected by a user and that processes a menu of the following items: 1. Input employee’s information, 2. Compute pay for all employees, 3. Display payroll report and 4. Exit.

Whatever the user inputs will get assigned to the variable option and the code will go into a if, else if and else statement to function correctly and go into the correct area of code. If the users option is equaled to one: The program will go into the inputData(). This will also have three parameters as employeeNamesList, hoursWorkedList and payRateList. The program will go into an else if statement if the user inputs 2 for their option. This will state the program will go into the computePay(). This will have two parameters known as hoursWorkedList and payRateList. Again, if the user enters in three for the option, the program will head into else if statement. However, before calling the displayPay() that is calling all parameters. It will have a nested if statement configuring if the length of the grossPayList is not zero, to head into the displayPay() and perform the actions in it.  Another nested else; If for some reason the list is not zero, to display a message saying “You cannot display an empty list.” The program will head into its last elif block statements saying if the users option is equaled to four: To display a thank you for using the application and will close. If the user hits anything besides those four: It will display an invalid input and to try again later.

Afterwards, the program will start to open the employeeFile.txt file inside the computer to write within it. The program uses the open function to write the information from the file. The program uses ‘w’ to do so. The program will head into a for loop stating for employee in the range and length of employeeNamesList: Write onto the file as the variable employee and formats the variable inside the employeeNameList, hoursWorkedLIsts, payRateList and grossPayList and converts them into strings while being written.

Heading into the inputData() once it is called within the option loop. The program will start with three parameters as well. The first thing that the function will do is state a variable named userResponse and it will get assigned from the input user implies from "Do you have any employees to enter? (y/n): " Heading into the block of code inside of the while loop for employee information states the variable employeeNames will be assigned to the user’s response to the input message containing "Enter employee name: " The next line of code implies that the employeeNames entered will be appended to the employeeNamesList. 

Afterwards, it will head into another while loop stating: While not employeeNames is not alphabetic: It will display an invalid input because you entered something that was not alphabetic. If stated as a digit: It will have you re-enter some input again stating to be alphabetic.Afterwards, append the employeeNames to the employeeNamesList. Heading into a variable named as hoursWorked. This assigns the user input as a float and to the variable. The message displayed will be "Enter amount of hours worked: " After the input for hoursWorked is entered: It will be appended into the hoursWorkedList. Heading into a variable named as payRate. This assigns the user input as a float and to the variable. The message displayed will be "What is the pay rate?" After the input for payRate is entered: It will be appended into the payRateList.  Afterwards, the variable userResponse will be assigned as a input from the user displaying a message such as "Do you have more employees to enter? (y/n): " It will continue into a if statement if the users response is "n": If userResponse is equal to 'n'. It will display a message saying "Thank you for using our payroll application. Have a wonderful day! Also, it will exit the program. The else statement here states that if all else an invalid input message will appear. Displays an invalid message displaying "Invalid input. Please try again later. Goodbye!"

Heading into the computePay() once the it is called within the option loop. The program will start with two parameters as well. Known as hoursWorkedList and payRatesList. Once inside the computePay(), it will go into a for loop stating for employee in the range and length in the payRateList. Within the for loop processes different indexes and goes inside the if statement. If the hoursWorkedList of the employee is greater than forty. If greater than forty, assigns a variable named overTimePay. That variable is equaled to the work of the hoursWorkedList minus forty times the payRateList times one point five. The grossPay of the employee is assigned when its equaled to forty times the payRateList of the employee plus the overTimePay that was assigned in the last line of code. The grossPay that was assigned will get appended to the grossPayList. Heading into the else statement if the hoursWorked is anything else. Stating that the grossPay of the employee is assigned and equaled to the hoursWorkedList of the employee plus the payRateList of the employee. The grossPay that was assigned will get appended to the grossPayList.

Heading into the displayPay() once the it is called within the option loop. The program will start with four parameters as well. Known as hoursWorkedList, employeeNamesList, payRatesList and grossPayList. Displaying the Title of the payroll of the DooDad Manufacturing Company in December and displaying the different sections of the payroll such as the Employee Name section, hours worked section, pay rate section and the gross pay section. Also, adding line breakage throughout the sections. The next statement is a for loop stating: For employeeNo in the range and length of the employeeNamesList: To print and format the employeeNamesList, hoursWorkedList, payrateList and grossPayList to the verified area it needs to be at. Afterwards, it will print”---------------“ to add breakage. After that line of code states that the main function is being called and will run whatever is in the main function.

Design
-----------------------------------------
Here is the Pseudocode: ------------------------------------------------------------------------
•	Define the main function
o	Define an empty list for the employee names
o	Define an empty list for the hours worked
o	Define an empty list for the pay rate
o	Define an empty list for the gross pay
o	Open the employee file for reading in .txt
o	Read the input from the user within the file
o	Head into a while statement that is not an empty string
♣	The employee info assigned will be the line and split
♣	Use the info as an index and append that information to the name list
♣	Use the info as an index and append that information to the hour’s list
♣	Use the info as an index and append that information to the pay list
♣	Use the info as an index and append that information to the gross list
♣	Read the input that the user typed within the employee file
o	The program will close until the program needs it again
o	Assign zero to the variable name option
o	Head into a while loop that option is not equaled to 4
♣	Display "------------PAYROLL MENU-------"
♣	Display "1. Input employee’s information"
♣	Display "2. Compute pay for all employees"
♣	Display "3. Display payroll report"
♣	Display "4. Exit"
♣	Display "-------------Selection---------"
♣	Assign option to the user’s input
♣	If the users option is equaled to one
•	Call the inputData function
♣	 Else if the option is equaled to two
•	Call the computePay function
♣	Else if the option is equaled to three 
•	If the length of the grossPayList is not zero
o	Call displayPay function
•	Else display an Invalid input message
♣	Else if the option is equaled to four
•	Display a thank you message for using the application
♣	Else display an invalid message
♣	Open the employee file once more but for writing onto it this time
♣	For employee in the range and length of the employee name list
•	Write and format the name, pay, hours and gross into strings
♣	Head into the inputData(If user picked the right choice
•	Assign the user response to the input of any employees (y or n)
•	While the user’s response is equaled to “y”
o	Assign a name for the employee
o	Append the name into the employee names list 
o	While name is not alphabetic
♣	Display invalid input
♣	User must re-enter input
♣	Append the name to the employee names list
o	Assign the amount of hours worked and set float
o	Append hours worked to the hoursWorkedList
o	Assign the pay rate to and set to float
o	Append the pay rate to the payRateList
o	Ask the user for any more employees to enter through input
•	If user’s response is equaled to “n”:
o	Display a thank you message and exit
•	If all else fails
o	Display an invalid message and exit
♣	Head into the computePay(If user picked the right choice
•	For employee in the range and length of the pay rates list
o	If hours worked list is greater than forty
♣	Over time pay will be assigned to the algorithm of the hour’s list minus forty times the pay rate list times one point five.
♣	The gross pay will be assigned to the algorithm of forty times the pay rate list plus overtime pay.
♣	Append the gross pay to the gross pay list
o	If all else fails
♣	The gross pay is assigned to the hours worked plus the pay rate list
♣	Append the gross pay to the gross pay list
♣	Head into the DisplayPay(If user picked the right choice)
•	Display DOODAD MANUFACTURING COMPANY DECEMBER PAYROLL
•	Display the different sections as Employee name, Hours worked, Pay rate and gross pay.
•	Display “------------------ -----------------  ------------   ----------------“
•	For employee number in the range and length of employee names list
o	Display and format employeeNamesList to its section
o	Display and format hoursWorkedList to its section
o	Display and format payRatesList to its section
o	Display and format grossPayList to its section
o	Display “-----------------------------------------------------------“
•	Call the main function to run the program 

