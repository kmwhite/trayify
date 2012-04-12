
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

def pep8():
    ''' Check the code base for PEP8 Compatibility '''
    local('pep8 .')

def coverage_loop():
    ''' Run the coverage report in an infinite loop '''
    while True:
        coverage()
        local('read')

def clean():
    ''' Clean the *.pyc files from the working tree '''
    local('find . -iname "*.pyc" -exec rm -v {} \;')
