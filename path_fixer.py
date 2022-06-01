class PathFixer():
    """Class that exchange every backlash with slash in given path"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.fp_list = []
        self.backslash = chr(92)
        self.slash = "/"
        self.slash_index = []

    def python_path_converter(self):
        """Function that convert given path to path compatibile with python syntax"""

        for letter in self.file_path:    # loop that convert given string to list
            self.fp_list.append(letter)

        for i in range(len(self.fp_list)):    # loop that gives the indexes of backslashes in the given path

            if self.fp_list[i] == self.backslash:
                self.slash_index.append(i)

        for i in range(0, len(self.slash_index)):    # loop that turns backslashes into slashes
            insert_slash = self.slash_index[i]
            self.fp_list[insert_slash] = self.slash

        self.fixed_file_path = str("".join(self.fp_list))    # converting list to string
        self.fixed_file_path = self.fixed_file_path.replace(chr(34),"")    # deleting " at the beginig and in the end of the path (if it apears)
        return self.fixed_file_path

    def git_path_converter(self):
        """Function that convert given path to path compatibile with git bash"""

        for letter in self.file_path:    # loop that convert given string to list
            self.fp_list.append(letter)

        for i in range(len(self.fp_list)):    # loop that gives the indexes of backslashes in the given path

            if self.fp_list[i] == self.backslash:
                self.slash_index.append(i)

        for i in range(0, len(self.slash_index)):    # loop that turns backslashes into slashes
            insert_slash = self.slash_index[i]
            self.fp_list[insert_slash] = self.slash

        self.fixed_file_path = str("".join(self.fp_list))    # converting list to string
        self.fixed_file_path = self.fixed_file_path.replace(chr(34),"")    # deleting " at the beginig and in the end of the fixed path (if it apears)
        self.fixed_file_path = "/" + self.fixed_file_path    # adding the slash at the beginning of the fixed path
        self.lower_driver = self.fixed_file_path[1].lower()    # converting driver symbol into lowercase
        self.fixed_file_path = self.fixed_file_path.replace(self.fixed_file_path[1], self.lower_driver)    # adding lowercase driver symbol to the fixed path
        self.fixed_file_path = self.fixed_file_path.replace(self.fixed_file_path[2], "")    # deleteing ":" symbol after driver symbol in fixed path
        return self.fixed_file_path

