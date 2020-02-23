from logging.config import dictConfig
from pathlib import Path

dictConfig({
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'general': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': f'{Path.cwd().resolve()}/logs/general.log',
            'mode': 'a',
            'maxBytes': 8388608,  # 8MB in bytes
            'backupCount': 5,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['general', 'console']
    }
})

