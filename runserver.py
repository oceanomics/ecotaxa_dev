# -*- coding: utf-8 -*-
# This file is part of Ecotaxa, see license.txt in the application root directory for license informations.

from appli import app
import logging,sys
import logging.handlers



if __name__ == '__main__':
    app.debug = True
    handler = logging.handlers.RotatingFileHandler('MyAppli.log', maxBytes=10000, backupCount=1)
    #handler = logging.FileHandler('MyAppli.log')
    handler.setLevel(logging.INFO)
    LoggingFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handler.setFormatter(logging.Formatter(LoggingFormat))
    app.logger.addHandler(handler)
    app.logger.info("App Startup")
    # L'executable est l'interpreteur qui à permis de lancer, mais en WSGI c'est écrasé par le lanceur WSGI
    app.PythonExecutable=sys.executable



    app.run()
