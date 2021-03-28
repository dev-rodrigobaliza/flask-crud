class Config(object):
    """
    Common configurations
    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
