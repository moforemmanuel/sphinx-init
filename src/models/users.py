"""
This is the file for users
"""


class NOExecError(Exception):
    """
    Raised when No Exec Occurs
    """
    print("No Exec")


class User_Model:
    """
    This is the class declaration for the user model

    :cvar baseid: This is the id generated when a user model is created
    :type baseid: str
    """

    baseid = 0

    def __init__(self, name):
        """
        Instantiates a user instance

        :param name: str Name of user
        :type name: str
        :raise TypeError: If invalid
        :rtype: dict
        """
        self.name = name
        self.baseid += 1

    def create(self):
        """
        creates a user from the model

        :raises NOExecError: If No Exect
        :return: user object
        :rtype: User_Model
        """
        return {
            "user": self.name,
            "id": self.baseid
        }

