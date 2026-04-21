from loggers.logger import Logger
import json

class FileLogger(Logger):
    file_path: str
    
    def __init__(self, path):
        self.file_path = path

    def log(self, info: dict):
        with open(self.file_path, 'a') as f:
            json.dump(info, f)
            f.write('\n')