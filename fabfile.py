from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test easyus')
    local('git add -p & git commit')

def deploy():
    with lcd('/srv/www/easyus/'):
        local('git pull /srv/www/easyus')
        local('python manage.py migrate')
        local('python manage.py runserver')
