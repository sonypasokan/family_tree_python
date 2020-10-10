import sys

class InputReader:
    """Input collector from command line."""

    def __init__(self):
        pass

    def read_input(self):
        """Function that reads the commandline argument and reads the given file.
        @self : Object pointer.
        """
        file_path = sys.argv[1]
        try:
            with open(file_path, "r") as file_pointer:
                file_content = file_pointer.readlines()
                return file_content
        except:
            print("FILE_NOT_FOUND")
            exit(0)
