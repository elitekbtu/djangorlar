# Project modules
from decouple import config


'''
Enviorenment id
'''

ENV_POSSIBLE_OPTIONS = (
    'local', 
    'prod', 
)

ENV_ID = config("DJANGORLAR_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure-k0p)vx3j^)hpc*#3tvoz*)f(e%%v!81cnhpcpsp4!7c_iohrep'