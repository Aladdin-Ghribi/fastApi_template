import logging
from logging.config import dictConfig



def configure_logging() -> None:
    dictConfig(

        {
            "version": 1,
            "disable_existing_loggers":False,
            "formatters":{
                "standard":{
                    "format":"[%(levelname)s %(name)s - %(message)s]",
                }
            },
            "handlers":{
                "console":{
                    "class":"logging.StreamHandler",
                    "formatter": "standard",
                    "level":"INFO",
                }
            },
            "root":{
                "handlers": ["console"],
                "level":"INFO",
            }
        }
    )