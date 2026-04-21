from loggers.logger import Logger

class ConsoleLogger(Logger):
    def log(self, info: dict):
        print(info)