from config.settings import LOCAL_APPS
from fabric.api import run, sudo, env, hosts

server_ip = '195.201.217.12'

virtual_env_name = 'richard'
env.is_test = False
enable_virtualenv = 'source /usr/share/virtualenvwrapper/virtualenvwrapper.sh'

local_apps = [app_dir.split('.')[1] for app_dir in LOCAL_APPS]


@hosts([server_ip])
def prod():
    env.hosts = [server_ip]
    env.branch = 'master'
    env.app_path = '/home/richard/linus'
    env.user = 'richard'
    env.password = 'stallman'


def git_stash():
    run('cd %s; git checkout %s; git stash' % (env.app_path, env.branch))


def git_pull():
    run('cd %s; git checkout %s; git pull' % (env.app_path, env.branch))


def pip():
    run('%s; cd %s; workon %s; pip install -r requirements.txt' % (enable_virtualenv, env.app_path, virtual_env_name))


def collectstatic():
    run('%s; cd %s; workon %s; python manage.py collectstatic -v0 --noinput'
        % (enable_virtualenv, env.app_path, virtual_env_name))


def manage(command='help'):
    run('%s; cd %s; workon %s; python manage.py %s' % (enable_virtualenv, env.app_path, virtual_env_name, command))


def make_migrations():
    command = 'makemigrations'
    command = '{} {}'.format(command, ' '.join(local_apps))
    manage(command)


def migrate():
    manage('migrate')


def supervisor_restart():
    sudo('supervisorctl update')
    sudo('supervisorctl restart all')


def nginx_restart():
    sudo('/etc/init.d/nginx restart')


def restart():
    supervisor_restart()
    nginx_restart()


def deploy():
    git_stash()
    git_pull()
    pip()
    collectstatic()
    make_migrations()  # comment when we stop putting migrations to the gitignore
    migrate()
    restart()


def createsuperuser():
    run('%s; cd %s; workon %s; python manage.py createsuperuser' % (enable_virtualenv, env.app_path, virtual_env_name))
