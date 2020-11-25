import os
class File_Recursion(object):
    def find_files(self, suffix, path):
        """
            Find all files beneath path with file name suffix.

            Note that a path may contain further subdirectories
            and those subdirectories may also contain further subdirectories.

            There are no limit to the depth of the subdirectories can be.

            Args:
            suffix(str): suffix if the file name to be found
            path(str): path of the file system

            Returns:
            a list of paths
        """
        return self.find_files_fast(path, 0)
    def find_files_fast(self, path, index):
        if index == len(os.listdir(path)):
            return
        list_ = sorted(os.listdir(path))
        while len(list_) != 0:
            first_ele = list_.pop(0)
            traverse_path = os.path.join(path, first_ele)
            if os.path.isfile(traverse_path):
                print (traverse_path)
            elif os.path.isdir(traverse_path):
                print (traverse_path)
                self.find_files_fast(traverse_path, 0)
        return
# Let us print the files in the directory in which you are running this script

dir = 'testdir'
current_path = os.getcwd()
dir_to_recurse = os.path.join(current_path, dir)
FR = File_Recursion()
print(dir_to_recurse)
FR.find_files(".c", dir_to_recurse)
