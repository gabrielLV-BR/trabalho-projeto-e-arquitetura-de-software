from abc import abstractmethod

class Logger:
    @abstractmethod
    def log(self, info: any):
        pass

class Logging:
    listeners: list[Logger] = []

    def subscribe(listener: Logger):
        Logging.listeners.append(listener)

    def log(info: any):
        for listener in Logging.listeners:
            listener.log(info)
