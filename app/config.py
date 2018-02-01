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

WHITETEAM_USERNAME = "theblindmice"
WHITETEAM_PASSWORD = "basedgodboyuan1016"

REDTEAM_USERNAME = "raiders"
REDTEAM_PASSWORD = "miserylovescompany96"
REDTEAM_KEY = "EUBCG"

NUMBER_OF_TEAMS = 11
DEFAULT_PASSWORD = 'Changeme-2018'
DEFAULT_BALANCE = 1000
SQLALCHEMY_DATABASE_URI = 'mysql://root:youwontguess23$@localhost/ists'

TEAM_PRIVATE_KEYS = ['3DM3Z', 'JV8IB', '4ZWA6', '4URL3', 'WEF54', 'C4009',
                     '1V032', 'CFI4D', '697YU', '5AVCN']

TEAM_PUBLIC_KEYS = ['EMJACC1YG2LWUZTW', 'H665KSBR8KO1NOLO', '0X3RY1YBBB6IVEYN',
                    'OD489SDPOCBZQI2D', 'R3M61E4CEL7B2ED7', 'Y9P95CK2H8BXAIKU',
                    'FBTOCZTKRZN6QGYQ', 'FNKBRP973DH59ZW1', 'UOWNLGH0KAT719UX',
                    '798Q57EHULEAM01A', 'AL415FDQM9EAIZ47']

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
