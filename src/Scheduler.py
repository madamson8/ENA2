import os
from os.path import expanduser


class Scheduler(object):
    folderpath = expanduser("~")
    def main(self):
        print("Object Created.")
        if not os.path.exists(self.folderpath):
            os.makedirs(self.folderpath + "/.ena")
