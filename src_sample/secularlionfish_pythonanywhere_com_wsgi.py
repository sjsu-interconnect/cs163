# This file contains the WSGI configuration required to serve up your
# web application at http://secularlionfish.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError


import sys

# add your project directory to the sys.path
project_home = u'/home/secularlionfish/cs163/src_sample'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path



# need to pass the flask app as "application" for WSGI to work
# for a dash app, that is at app.server
# see https://plot.ly/dash/deployment
from app4 import app
application = app.server