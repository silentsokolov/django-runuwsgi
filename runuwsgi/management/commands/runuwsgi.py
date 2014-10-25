import os

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-p', '--port', dest='port', help='Port'),
        make_option('-s', '--socket', dest='socket', help='Socket, example: /tmp/project.sock'),
        make_option('--home', dest='home', help='Virtualenv dir (home)'),
        make_option('-c', '--chdir', dest='chdir', help='Project dir (chdir)'),
        make_option('-m', '--module', dest='module', help='Module (wsgi script)'),
        make_option('-r', '--autoreload', dest='autoreload', default=1, help='Auto reload'),
        make_option('--static-map', dest='static-map', action='append', help='list static-map uwsgi'),
        make_option('--static-index', dest='static-index', action='append', help='list static-index uwsgi'),
    )

    run_command = 'uwsgi ' \
                  '--uid={uid} ' \
                  '--gid={gid} ' \
                  '{port}'\
                  '--socket {socket} ' \
                  '--chmod-socket=666 ' \
                  '--home={home} ' \
                  '--chdir={chdir} ' \
                  '--module={module} ' \
                  '{autoreload} ' \
                  '{static_maps} ' \
                  '{static_index} '

    def handle(self, *args, **options):
        if not options.get('socket'):
            raise CommandError('socket is required')
        socket = options.get('socket')

        if not options.get('home'):
            raise CommandError('home is required')
        home = options.get('home')

        if not options.get('chdir'):
            raise CommandError('chdir is required')
        chdir = options.get('chdir')

        if not options.get('module'):
            raise CommandError('module is required')
        module = options.get('module')

        port = ''
        if options.get('port'):
            port = '--http :{} '.format(int(options.get('port')))

        autoreload = ''
        if options.get('autoreload'):
            autoreload = '--py-autoreload={} '.format(int(options.get('autoreload')))

        static_maps = ''
        if options.get('static-map'):
            for m in options.get('static-map'):
                static_maps += '--static-map {} '.format(m)

        static_index = ''
        if options.get('static-index'):
            for index in options.get('static-index'):
                static_index += '--static-index {} '.format(index)

        os.system(self.run_command.format(
            uid=os.getuid(),
            gid=os.getgid(),
            port=port,
            socket=socket,
            home=home,
            chdir=chdir,
            module=module,
            autoreload=autoreload,
            static_maps=static_maps,
            static_index=static_index,
        ))
