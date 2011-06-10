from __future__ import with_statement
import getpass

from django.core import management
import settings as django_settings
management.setup_environ(django_settings)

from fabric.api import *
from fabtastic.fabric.commands import *

# The name of the user executing this script. Needed for building some
# of the roledefs below for config updates.
LOCAL_USERNAME = getpass.getuser()

# REALLY IMPORTANT: You need to generate an SSH key if you don't already
# have one. You'll also need to send it to a server admin to get it added.
env.key_filename = os.path.expanduser('~/.ssh/id_rsa.pub')
env.REMOTE_CODEBASE_PATH = '/home/mcserv/creeperslament'
# Path relative to REMOTE_CODEBASE_PATH.
env.PIP_REQUIREMENTS_PATH = 'deployment/requirements.txt'
# The standardized virtualenv name to use.
env.REMOTE_VIRTUALENV_NAME = 'mcserv'

# This is used for reloading gunicorn processes after code updates.
env.GUNICORN_PID_PATH = os.path.join(env.REMOTE_CODEBASE_PATH, 'gunicorn.pid')

"""
Role definitions group various hosts together, for use with the 'roles'
decorator. See source below for examples of this in practice.

The *_cfg roles below are used for updating the server deployment config
files. For these, we have to login as your current user (which much have a
corresponding account on the servers), and go through sudo.

These are populated by staging() and prod().
"""
# Nginx proxies.
env.roledefs['proxy_servers'] = []
# The Django + gunicorn app servers.
env.roledefs['webapp_servers'] = []
# Postgres servers.
env.roledefs['db_servers'] = []

def prod():
    """
    Sets env.hosts to the sole staging server. No roledefs means that all
    deployment tasks get ran on every member of env.hosts.
    """
    for role in env.roledefs.keys():
        env.roledefs[role] = ['mcserv@184.106.219.155']
    env.hosts = ['mcserv@184.106.219.155']

def deploy():
    """
    Full git deployment. Migrations, reloading gunicorn.
    """
    git_pull()
    run('cd ~/zombiepygman && git pull')
    south_migrate()
    gunicorn_restart_workers()
    flush_cache()
    mediasync_syncmedia()
