from abc import ABCMeta, abstractmethod


class IAction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

    @abstractmethod
    def do_action(self):
        pass
