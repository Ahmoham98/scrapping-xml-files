#Creating a configuration file for the system
class configuration :
    DATABASE = None
    DATABASE_USERNAME = None
    DATABASE_PASSWORD = None
    DATABASE_HOST = None
    DATABASE_PORT = None
    DEBUG_MODE = None
    
    
    def __init__ (self):
        pass
    #Setting configuration function
    def configure ( self,
                    database = 'mongodb',
                    database_username = 'Ahmad',
                    database_password = "Enter you password here",
                    database_host = 'localhost',
                    database_port = 27017,
                    debug_mode = True
                    ):
        self.DATABASE = database
        self.DATABASE_USERNAME = database_username
        self.DATABASE_PASSWORD = database_password
        self.DATABASE_HOST = database_host
        self.DATABASE_PORT = database_port
        self.DEBUG_MODE = debug_mode