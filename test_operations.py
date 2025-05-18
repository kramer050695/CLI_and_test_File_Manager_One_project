import unittest
import tempfile
import shutil
import os
from operations import (
     copy_file,
     delete_path,
     count_files_in_dir,
     find_files_in_dir
)


class TestOperations(unittest.TestCase):

     def setUp(self):
          self.test_dir = tempfile.mkdtemp()
          self.file1 = os.path.join(self.test_dir, "test1.txt")
          self.file2 = os.path.join(self.test_dir, "sample.doc")
          with open(self.file1, 'w') as f:
               f.write("hello")
          with open(self.file2, 'w') as f:
               f.write("world")

          self.subdir = os.path.join(self.test_dir, "subfolder")
          os.mkdir(self.subdir)
          self.subfile = os.path.join(self.subdir, "subfile.txt")
          with open(self.subfile, 'w') as f:
               f.write("subcontent")


def tearDown(self):
     shutil.rmtree(self.test_dir)


def test_copy_file(self):
     dest_file = os.path.join(self.test_dir, "copied.txt")
     copy_file(self.file1, dest_file)
     self.assertTrue(os.path.exists(dest_file))


def test_delete_file_and_folder(self):
     delete_path(self.file1)
     self.assertFalse(os.path.exists(self.file1))
     delete_path(self.subdir)
     self.assertFalse(os.path.exists(self.subdir))


def test_count_files_in_dir(self):
     count = count_files_in_dir(self.test_dir)
     self.assertEqual(count, 2)


def test_find_files_in_dir(self):
     results = find_files_in_dir(self.test_dir, r".*\.txt$")
     self.assertIn(self.file1, results)


if __name__ == '__main__':
     unittest.main()