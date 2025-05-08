from unittest import TestCase
from class_structure.File import File

class TestFile(TestCase):

    path = "src/main/java/Exam/Exam.java"

    def test_get_package_name(self):
        self.assertEqual("src/main/java/Exam", File.get_package_name(self.path))

    def test_get_package_name_at_depth_to_great(self):
        self.assertEqual("src/main/java/Exam", File.get_package_name_at_depth(self.path, 5))
    
    def test_get_package_name_at_depth_same(self):
        self.assertEqual("src/main/java/Exam", File.get_package_name_at_depth(self.path, 4))

    def test_get_package_name_at_depth_less(self):
        self.assertEqual("src/main/java", File.get_package_name_at_depth(self.path, 3))