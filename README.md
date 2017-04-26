Project
=======

This ia a basic template for python (Django Rest Framework). With Pylint setup and
Test cases setup.

##Steps to Setup Local Environment.

###To clone the repository 
1. git clone git@proddevelopment.git.beanstalkapp.com:/proddevelopment/py-platform-services.git

###To setup local environment dependencies
1. Install python3.
   sudo apt-get install python3
2. See if it works and show version as 3.x.x
   python3
3. Install python3-dev
   sudo apt-get install python3-dev
4. Install python-virtualenv
   sudo apt-get install python-virtualenv
6. Create virtual environment.
   virtualenv pyvenv
7. Set its path
   virtualenv -p /usr/bin/python3.4 pyvenv
   or
   virtualenv -p /usr/local/bin/python3.5 pyvenv
8. Activate it.
   source pyvenv/bin/activate
9. Install dependencies:
   pip3 install -r requirements.txt

###To setup for Test cases
1. To run test cases we need to install fabric
   sudo apt-get install fabric or pip3 install fabric3

###How to get Pylint score
1. Command to test pylint errors on terminal
   fab lint_py
2. Also we can use below pylint command to create pylint report
   pylint --rcfile=pylint.cfg $(find . -maxdepth 1 -name "*.py" -print) project/ > out/pylint.log
   or
   pylint project

###How to get jsLint score
1. Install jshint
   npm install -g jshint
   npm install --save-dev jshint
2. Command to test jslint score
   jshint templates
   or
   jshint templates > out/jslint.log

###How to get cssLint score
1. Install css-lint
   npm install -g csslint
2. Command to test css-lint score
   csslint templates
   or
   csslint templates > out/csslint.log

###To run the server
1. python3 manage.py runserver

###To run test cases
1. Running all test cases
   fab test
2. Run a particular test file
   fab test:<folder.module>
   or
   python manage.py test <folder.module.filename.Classname.specific function name>

###For code Coverage
1. To generate coverage report
   fab coverage test
It will generate coverage folder in /out

###Gunicorn setup for local
1. Install Gunicorn:
   pip install gunicorn
2. Run command for gunicorn
   gunicorn project.wsgi:application --bind 127.0.0.1:8000 --workers=6 --threads=4 --log-file /var/log/gunicorn.log --log-level error
   or
   gunicorn project.wsgi:application --bind 127.0.0.1:8000

###Run logentries
1. sh path/to/logentries_install.sh ${LOG_ENTRIES_FLAG} ${LOGENTRIES_LICENSE_KEY} ${APPNAME}
   example 'sudo ./logentries_install.sh true <Key> Project'

   Required environment variables we need to declare:
   LOGENTRIES_LICENSE_KEY = <KEY>
   LOG_ENTRIES_FLAG = <True/False> Depending on environment its value will varry.
                      Its value will decide whether to intall logentries or not.
   APPNAME = <Application name e.g., 'Project'>
