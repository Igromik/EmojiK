import json
from os import getcwd
from os.path import (join, isdir)


class JSONLoader:
    def __init__(self):
        self.path: str
        self.file: str

    def _set_path(self, path: str=None):
        if path:
            if not isdir(path):
                path = join(getcwd(), path)
                if isdir(path):
                    self.path = path
                else:
                    print("Unknown Directory")
        else:
            self.path = getcwd()

    def load_json(self):
        with open(join(self.path, self.file), "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def __call__(self, file: str, path: str=None):
        self.file = file
        self.path = path
        
        self._set_path(self.path)
        return self.load_json()
