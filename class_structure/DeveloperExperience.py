from class_structure.Structure import Structure
from datetime import datetime
class DeveloperExperience(Structure):

    input_format = "%Y-%m-%dT%H:%M:%SZ"
    output_format = "%Y%m%d%H%M%S"

    def __init__(self, developer, repository_name, date, language):
        super().__init__(repository_name)
        self.developer = developer
        self.pull_date = datetime.strptime(date, self.input_format)
        self.language = language

    def get_pull_date(self):
        return self.pull_date.strftime(self.output_format)

