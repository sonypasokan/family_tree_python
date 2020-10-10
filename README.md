# PROJECT - Lengaburu Family Tree
Existing family members are already setup in the program. The program can accept more family members and get the relationship.
This can be done using specific commands which are mentioned in below section "Commands Accepted".

### COMMANDS ACCEPTED
1. ADD_CHILD        : Provide mother's name, person's name and person's gender.
eg. : ADD_CHILD Alice Bhanu Female
2. GET_RELATIONSHIP : Provide person's name and expected relationship.
eg. : GET_RELATIONSHIP Alice daughter
3. ADD_SPOUSE       : Provide existing person's name and spouse's name.
eg. : ADD_SPOUSE Bhanu Charlie

#### Note
The commands should be provided in a separate file, which has to be given as an input argument while running the script. See the next section to run the script with input file.


### HOW TO RUN
> python3 -m geektrust <file_name_with_path>

### HOW TO TEST THE CODE
A sample test file is available along with the source code. This contains all the sample use cases given in the problem statement, along with ADD_SPOUSE command used with one success and with one failure case. To run this, enter the command-
> python3 -m geektrust test_file.txt


### OUTPUT
Output will be printed in the console for every input command in the given input file.
#### For ADD_CHILD command
1. CHILD_ADDITION_SUCCEEDED : When child is successfully added.
2. CHILD_ADDITION_FAILED : Child cannot be added because the given mother is not a female.
3. PERSON_NOT_FOUND : Child cannot be added because the given mother not exist in the family.
#### For GET_RELATIONSHIP command
1. "Name1" "Name2" ... "NameN" : When relationship is found, all relatives names will be printed.
2. PERSON_NOT_FOUND : When given person does not exist in the family.
3. NONE : When the given person does not have any member with given relationship.
4. RELATIONSHIP_NOT_FOUND : When given relationship is not established in the program.
#### For ADD_SPOUSE command
1. SPOUSE_ADDITION_SUCCEEDED : When spouse added successfully.
2. SPOUSE_ADDITION_FAILED : When the given person already has a spouse and hence a new spouse cannot be added.
3. PERSON_NOT_FOUND : When given person does not exist in the family.
#### For file input
1. FILE_NOT_FOUND : When input file path is wrong or cannot be read.


#### Note
Existing family members with relationship is already added to the program.
For this, there will be no output messgae returned from the program.
This means, only for the inputs that are received through the input file, output will be printed in the console.
