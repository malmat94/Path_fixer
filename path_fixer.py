class PathFixer():
    """Class that exchange every backlash with slash in given path"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.fp_list = []
        self.backslash = chr(92)
        self.slash = "/"
        self.slash_index = []

    def python_path_converter(self):   # Funkcja do konwersji ścieżki do pliku (zamiana backleshy na slashe)

        for letter in self.file_path:    #pętla tworząca listę ściężki z stringa
            self.fp_list.append(letter)

        for i in range(len(self.fp_list)):   #pętla tworząca listę indeksów backlashy w ścieżce

            if self.fp_list[i] == self.backslash:
                self.slash_index.append(i)

        for i in range(0, len(self.slash_index)):   #pętla zamieniająca backlsashe na slashe
            insert_slash = self.slash_index[i]
            self.fp_list[insert_slash] = self.slash

        self.fixed_file_path = str("".join(self.fp_list))
        self.fixed_file_path = self.fixed_file_path.replace(chr(34),"")
        return self.fixed_file_path

    def git_path_converter(self):   # Funkcja do konwersji ścieżki do pliku (zamiana backleshy na slashe)

        for letter in self.file_path:    #pętla tworząca listę ściężki z stringa
            self.fp_list.append(letter)

        for i in range(len(self.fp_list)):   #pętla tworząca listę indeksów backlashy w ścieżce

            if self.fp_list[i] == self.backslash:
                self.slash_index.append(i)

        for i in range(0, len(self.slash_index)):   #pętla zamieniająca backlsashe na slashe
            insert_slash = self.slash_index[i]
            self.fp_list[insert_slash] = self.slash

        self.fixed_file_path = str("".join(self.fp_list))
        self.fixed_file_path = self.fixed_file_path.replace(chr(34),"")
        self.fixed_file_path = "/" + self.fixed_file_path
        self.lower_driver = self.fixed_file_path[1].lower()
        self.fixed_file_path = self.fixed_file_path.replace(self.fixed_file_path[1], self.lower_driver)
        self.fixed_file_path = self.fixed_file_path.replace(self.fixed_file_path[2], "")
        return self.fixed_file_path

