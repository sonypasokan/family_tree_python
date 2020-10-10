from person import Male, Female

class FamilyTree:
    """Operations on Family level is handled here."""

    def __init__(self, male_name, female_name):
        """Family should contain a minimum of a male and a female in Lengaburu. 
        (This is as per the constraints in the problem statement of King Shan's family.)
        @male_name : Name of male person.
        @female_name: Name of the female person.
        """
        self.family_root = None
        self._start_family_tree(male_name, female_name)
        self._establish_family_tree()
    
    def do_operations_read_from_file(self, file_content):
        """This function performs the operations as per the commands used.
        @file_content: Provide the list of lines from the file
        """
        for line in file_content:
            keywords = line.split()
            if not keywords: # the line is empty
                continue
            command = keywords[0].lower()
            if command == "get_relationship" and len(keywords) == 3:
                self.get_relative(keywords[1], keywords[2])
            elif command == "add_child" and len(keywords) == 4:
                child_added = self.add_child(keywords[1], keywords[2], keywords[3])
                if child_added:
                    print("CHILD_ADDITION_SUCCEEDED")
            elif command == "add_spouse" and len(keywords) == 3:
                spouse_added = self.add_spouse(keywords[1], keywords[2])
                if spouse_added:
                    print("SPOUSE_ADDITION_SUCCEEDED")
            else: # Other commands are it's operations are not established.
                print("WRONG_OPERATION")
        
    def _start_family_tree(self, male_name, female_name):
        """Family starts with two people in Lengaburu - one male and one female.
        @male_name : Name of male
        @female_name : Name of the female.
        """
        male_person = Male(male_name)
        female_person = Female(female_name)
        male_person.spouse = female_person
        female_person.spouse = male_person
        self.family_root = male_person # This can be the female also.
    
    def _establish_family_tree(self):
        """King's family already has many members.
        This function establishes the existing family members with their relationship.
        """
        self.add_child("Anga", "Chit", "Male")
        self.add_child("Anga", "Ish", "Male")
        self.add_child("Anga", "Vich", "Male")
        self.add_child("Anga", "Aras", "Male")
        self.add_child("Anga", "Satya", "Female")
        self.add_spouse("Chit", "Amba")
        self.add_spouse("Vich", "Lika")
        self.add_spouse("Aras", "Chitra")
        self.add_spouse("Satya", "Vyan")
        self.add_child("Amba", "Dritha", "Female")
        self.add_child("Amba", "Tritha", "Female")
        self.add_child("Amba", "Vritha", "Male")
        self.add_child("Lika", "Vila", "Female")
        self.add_child("Lika", "Chika", "Female")
        self.add_child("Chitra", "Jnki", "Female")
        self.add_child("Chitra", "Ahit", "Male")
        self.add_child("Satya", "Asva", "Male")
        self.add_child("Satya", "Vyas", "Male")
        self.add_child("Satya", "Atya", "Female")
        self.add_spouse("Dritha", "Jaya")
        self.add_spouse("Jnki", "Arit")
        self.add_spouse("Asva", "Satvy")
        self.add_spouse("Vyas", "Krpi")
        self.add_child("Dritha", "Yodhan", "Male")
        self.add_child("Jnki", "Laki", "Male")
        self.add_child("Jnki", "Lavnya", "Female")
        self.add_child("Satvy", "Vasa", "Male")
        self.add_child("Krpi", "Kriya", "Male")
        self.add_child("Krpi", "Krithi", "Female")

    
    def add_spouse(self, person_name, spouse_name):
        """This function adds the spouse to an existing person in the family.
        @person_name : Existing person's name.
        @spouse_name : Spouse who has to be added.
        """
        person = self.family_root.find_person(person_name)
        if not person:
            print("PERSON_NOT_FOUND", spouse_name)
            return
        if person.spouse:
            print("SPOUSE_ADDITION_FAILED")
            return
        if person.gender == "male":
            spouse = self._create_child(spouse_name, "female")
        else:
            spouse = self._create_child(spouse_name, "male")
        person.spouse = spouse
        spouse.spouse = person
        return True
    
    def add_child(self, mother_name, child_name, child_gender):
        """Function that adds child to the given mother.
        @mother_name : Name of existing mother.
        @child_name : Name of the child.
        @child_gender : Gender of the child. Accepted values are male and female (case insensitive).
        """
        child = self._create_child(child_name, child_gender)
        mother = self.family_root.find_person(mother_name)
        if not mother: # Person does not exist in the family
            print("PERSON_NOT_FOUND")
            return
        if mother.gender != "female": # Person exists in the family, but is a male.
            print("CHILD_ADDITION_FAILED")
            return
        child.mother = mother
        mother.add_child(child)
        return True
    
    def get_relative(self, person_name, relationship):
        """This function will list down the relatives with the given relationship.
        @person_name : Name of the person.
        @relationship : Expected relationship.
        """
        person = self.family_root.find_person(person_name)
        if not person: # Given person does not exist in the family.
            print("PERSON_NOT_FOUND")
            return
        relationship = relationship.lower()
        if relationship == "son":
            relatives = person.get_child_by_gender("male")
        elif relationship == "daughter":
            relatives = person.get_child_by_gender("female")
        elif relationship == "siblings":
            relatives = person.get_siblings()
        elif relationship == "paternal-uncle":
            relatives = person.get_parents_siblings(parent_gender="male", sibling_gender="male")
        elif relationship == "maternal-uncle":
            relatives = person.get_parents_siblings(parent_gender="female", sibling_gender="male")
        elif relationship == "paternal-aunt":
            relatives = person.get_parents_siblings(parent_gender="male", sibling_gender="female")
        elif relationship == "maternal-aunt":
            relatives = person.get_parents_siblings(parent_gender="female", sibling_gender="female")
        elif relationship == "sister-in-law":
            relatives = person.get_siblings_in_law("female")
        elif relationship == "brother-in-law":
            relatives = person.get_siblings_in_law("male")
        else: # This relationship is not established.
            print("RELATIONSHIP_NOT_FOUND")
            return
        if not relatives: # No person found as a relative.
            print("NONE")
            return
        print(" ".join([relative.name for relative in relatives]))
    
    def _find_person(self, current_person, person_name_to_find, spouse_checked=False):
        """Private function that finds a person if name of the person is given.
        @current_person : From which person node, the execution to start.
        @person_name_to_find : Person node which is being searched.
        @spouse_checked : Boolean flag that checks if the spouse of the current_person is checked or not.
            This flag is used to ensure that the program does not run into infinite loop
            by checking the spouse.
        """
        if current_person.name == person_name_to_find:
            return current_person
        if current_person.spouse and not spouse_checked:
            person_found = self._find_person(current_person.spouse, person_name_to_find, True)
            if person_found:
                return person_found
        if current_person.gender == "male": # All possible cases of male is over.
            return
        for child in current_person.children:
            person_found = self._find_person(child, person_name_to_find)
            if not person_found:
                continue
            return person_found    
    
    def _create_child(self, child_name, child_gender):
        """This function creates the child node.
        @child_name : Name of the child.
        @child_gender : Gender of the child. Accepted values are male and female.
        """
        child = None
        if child_gender.lower() == "male":
            child = Male(child_name)
        elif child_gender.lower() == "female":
            child = Female(child_name)
        return child