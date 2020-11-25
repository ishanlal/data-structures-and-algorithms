import os
class File_Recursion(object):
    path_list = []
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
        self.path_list = []
        return self.find_files_fast(path, suffix, 0)
    def find_files_fast(self, path, suffix, index):
        if os.path.isfile(path):
            f_list = []
            extension = os.path.splitext(path)
            if extension[1] == suffix:
                f_list.append(path)
            return f_list
        if os.path.isdir(path):
            if index == len(os.listdir(path)):
                return []
            sub_list = os.listdir(path)
            while len(sub_list) != 0:
                first_ele = sub_list.pop(0)
                traverse_path = os.path.join(path, first_ele)
                if os.path.isfile(traverse_path):
                    extension = os.path.splitext(traverse_path)
                    if extension[1] == suffix:
                        self.path_list.append(traverse_path)
                elif os.path.isdir(traverse_path):
                    self.find_files_fast(traverse_path, suffix, 0)
        return self.path_list
# Let us print the files in the directory in which you are running this script

#Test case 1
FR = File_Recursion()
path = "./testdir"
suffix = ".c"
file_list = FR.find_files(suffix, path)
print("Printing Test case 1...")
for i in range(len(file_list)):
    print(file_list[i])
#Test case 2
FR = File_Recursion()
path = "./test.py"
suffix = ".py"
file_list = FR.find_files(suffix, path)
print("Printing Test case 2...")
for i in range(len(file_list)):
    print(file_list[i])
