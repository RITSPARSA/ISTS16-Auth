"""
Configuration settings.
"""
import os
import logging
import sys

class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

class ErrorFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR

WHITETEAM_USERNAME = "theblindmince"
WHITETEAM_PASSWORD = "basedgodboyuan1016"

REDTEAM_USERNAME = "raiders"
REDTEAM_PASSWORD = "miserylovescompany96"

NUMBER_OF_TEAMS = 12
TEAMS = [x for x in range(1, NUMBER_OF_TEAMS+1)]
DEFAULT_PASSWORD = 'Changeme-2018'
DEFAULT_BALANCE = 1000
SQLALCHEMY_DATABASE_URI = 'mysql://root:youwontguess23$@localhost/ists'

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'info_filter': {
            '()': InfoFilter,
        },
        'error_filter': {
            '()': ErrorFilter,
        }
    },
    'handlers': {
        'info': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  '/var/www/ISTS16-Auth/app/logs/info.log',
            'mode': 'a',
            'backupCount': '16',
            'filters': ['info_filter']
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  '/var/www/ISTS16-Auth/app/logs/error.log',
            'mode': 'a',
            'backupCount': '16',
            'filters': ['error_filter']
        },
    },
    'loggers': {
        'api_log': {'handlers': ['info', 'error'], 'level': 'DEBUG', 'propagate': False},
    }
}
