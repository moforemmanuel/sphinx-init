"""
DatabaseSettingsModule

This is a module which has Class for DB and DB Settings
"""

class Database(object):
    """
    DB Class which is responsible for connecting to the db

    """

    def __init__(self, conn_str):
        """
        This is connection string to connect to sql server

        :param conn_str: stry
        """
        self.conn_str = conn_str

    def connect(self) -> True:
        """
        This method connects to the db

        :return: Bool
        """
        print("Connected to the database")