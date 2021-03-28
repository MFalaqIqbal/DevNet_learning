class Singleton:
    __instance = None

    @staticmethod  # execute getInstance before even instantiate an object
    def getInstance():
        """ Static access method. By calling get instance will create an instance"""
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


# s = Singleton.getInstance()
# print(s)
#
# s = Singleton.getInstance()
# print(s)

s = Singleton()  # Allowed
print(s.getInstance())

a = Singleton()  # Not allowed as an instance has already been setup
print(a)
