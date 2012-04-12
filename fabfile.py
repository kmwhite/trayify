
from fabric.api import env, local
import os

env.hosts = ['localhost']
#env.user = 'deploy'
#env.keyfile = ['$HOME/.ssh/deploy_rsa']
#env.directory = '/path/to/virtualenvs/project'
#env.activate = 'source /path/to/virtualenvs/project/bin/activate'

def test():
    local('py.test trayify test_trayify.py')

def coverage():
    local('py.test --cov trayify test_trayify.py')

def pep8():
    local('pep8 .')

def coverage_loop():
    while True:
        coverage()
        local('read')
