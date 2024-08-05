from class_structure.Structure import Structure
class Developer(Structure):

    logging_filter = []

    def __init__(self, name, email=None, login=None, primary_key=0):
        super().__init__(name, primary_key)
        self.email = email
        self.login = login
        self.commits = []

    def set_developer_id(self, developer_id):
        self.set_primary_key(developer_id)

    def is_active(self):
        return True
    
    def get_login(self, default=False):
        login = self.login
        if login is None and default and self.valid_name_for_login(self.name):
            login = self.get_name()
        return login
    
    def valid_name_for_login(self, name):
        valid = True
        counter = 0
        if name[0] == "-" or name[len(name) - 1] == "":
            valid = False
        while valid and counter < len(name):
            if not name[counter].isalnum():
                valid = False
            counter += 1
        return valid
    
    def get_email(self):
        return self.email

    def add_commit(self, developer_commit):
        self.commits.append(developer_commit)

    def to_string(self, spacer="\n"):
        display = super().to_string(spacer) + spacer
        return display
