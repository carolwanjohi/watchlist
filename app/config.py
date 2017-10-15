class Config:
    '''
    General configuration parent class
    '''
    # Store movie base URL
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

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