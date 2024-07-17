from class_structure.Repository import Repository
from class_structure.DeveloperCommit import DeveloperCommit
from class_structure.File import File
from class_structure.ClassStructure import ClassStructure
from class_structure.Method import Method
from class_structure.Developer import Developer
from class_structure.AmendmentType import *

class Main():

    def __init__(self) -> None:
        pass

    def test_run(self):
        repository = Repository("https://stgit.dcs.gla.ac.uk/DerekSomerville/marking.git")
        developer = Developer("Derek Somerville")
        developer_commit = DeveloperCommit("1234", "Derek Somerville", "27-Jun-2024", "Test", repository, developer)
        repository.add_commit(developer_commit)
        file = File("Test.py", added)
        developer_commit.add_file(file)
        class_structure = ClassStructure("ClassName", added, file)
        file.add_class(class_structure)
        method = Method("method_name", added, file)
        class_structure.add_method(method)

def main():
    main = Main()
    main.test_run()

if __name__ == "__main__":
    main()