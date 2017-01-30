import os
import traceback

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    args = 'up | down'
    help = 'Flag this server for maintenance - this stops the LB from sending new requests this way'

    def handle(self, *args, **options):
        if 'up' in args:
            try:
                if os.path.exists(settings.HEARTBEAT_FILENAME):
                    os.unlink(settings.HEARTBEAT_FILENAME)

                self.stdout.write('\nThis server is now available and should start ' \
                    'receiving new requests shortly.\n')
            except OSError as e:
                raise CommandError('FAILED to delete the heartbeat file: %s' % e)
            except:
                raise CommandError('FAILED to delete the heartbeat file: %s' % traceback.format_exc())

        if 'down' in args:
            try:
                open(settings.HEARTBEAT_FILENAME, 'w').write('0')

                self.stdout.write('\nThis server is now flagged for maintenance and ' \
                    'should stop receiving new requests shortly.\n' \
                    'Please allow a few moments for current requests to finish ' \
                    'before stopping the server.\n')
            except OSError as e:
                raise CommandError('FAILED to write the heartbeat file: %s' % e)
            except:
                raise CommandError('FAILED to write the heartbeat file: %s' % traceback.format_exc())
