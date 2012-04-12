
from fabric.api import env, local
import os

env.hosts = ['localhost']
#env.user = 'deploy'
#env.keyfile = ['$HOME/.ssh/deploy_rsa']
#env.directory = '/path/to/virtualenvs/project'
#env.activate = 'source /path/to/virtualenvs/project/bin/activate'

def test():
    ''' Run the unit tests '''
    local('py.test trayify test_trayify.py')

def coverage():
    ''' Run the unit tests and generate a coverage report '''
    local('py.test --cov trayify test_trayify.py')

def coverage_html():
    ''' Generate the HTML coverage report '''
    local('coverage run test_trayify.py; coverage html; firefox htmlcov/index.html')

def coverage_loop():
    ''' Run the coverage report in an infinite loop '''
    while True:
        coverage()
        local('read')

def pep8():
    ''' Check the code base for PEP8 Compatibility '''
    local('pep8 trayify/')

def pep8_loop():
    ''' Run the pep8 report in an infinite loop '''
    while True:
        pep8()
        local('read')

def clean():
    '''
        Clean the *.pyc files from the working tree. Additionally, remove all
        the __pycache__ directories
    '''
    local('find . -type d -name "*__pycache__*" -exec rm -rv {} \;')
    local('find . -iname "*.pyc" -exec rm -v {} \;')
