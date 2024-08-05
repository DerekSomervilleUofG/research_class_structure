from unittest import TestCase
from class_structure.Developer import Developer

class DeveloperTest(TestCase):
    
    developer = Developer("derek", "derek.somerville@glasgow.ac.uk")
    
    def test_login_with_none_default(self):
        self.assertEqual("derek", self.developer.get_login(True))
        
    def test_login_with_none(self):
        self.assertEqual(None, self.developer.get_login())
        
    def test_login_with_login(self):
        developer = Developer("derek", "derek.somerville@glasgow.ac.uk","derek-somerville")
        self.assertEqual("derek-somerville", developer.get_login(True))
        
         