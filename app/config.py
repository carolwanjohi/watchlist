class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: parent class with general config settings
    '''
    pass

class DevConfig(Config):
    '''
    Development config child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True