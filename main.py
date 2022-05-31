from path_fixer import PathFixer

print("Welcome to the path fixer!")
print("--------------------------\n")
print("1 - fixing path for python\n2- fixing path for GIT\n")

type = input("Choose Your fixing type: ")

path_fix_comm = ("Your fixed path is: ")
cont = "y"
while cont == "y":

    if type == "1":
        path_ff = input("Insert path to be fixed: ")
        print("")

        path = PathFixer(path_ff)
        fixed_path = path.python_path_converter()
        print(path_fix_comm)
        print(fixed_path)
        cont = input("Are You going to fix another path? (y - yes/n - no): ")


    elif type == "2":
        path_ff = input("Insert path to be fixed: ")
        print("")

        path = PathFixer(path_ff)
        fixed_path = path.git_path_converter()
        print(path_fix_comm)
        print(fixed_path)

input("Press ENTER to exit")