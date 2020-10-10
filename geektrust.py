from input_reader import InputReader
from family_tree import FamilyTree

def main():
    file_content = InputReader().read_input()
    family = FamilyTree(male_name="Shan", female_name="Anga") # Initializing with Kind and spouse.
    family.do_operations_read_from_file(file_content)


if __name__ == "__main__":
    main()