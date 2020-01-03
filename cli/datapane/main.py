from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .api.service import Service
from .controllers.datasets import DataSets
from .core.exc import DatapaneError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('datapane')
CONFIG['datapane']['host'] = '127.0.0.1'
CONFIG['datapane']['port'] = '8000'


def set_api_service(app):
    host = app.config.get('datapane', 'host')
    port = app.config.get('datapane', 'port')
    app.log.info('Remote set to {}:{}'.format(host, port))

    app.extend('apiservice', Service(host, port))


class Datapane(App):
    """Datapane primary application."""

    class Meta:
        label = 'datapane'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register hooks
        hooks = [
            ('post_setup', set_api_service),
        ]

        # register handlers
        handlers = [
            Base,
            DataSets,
        ]


class DatapaneTest(TestApp, Datapane):
    """A sub-class of Datapane that is better suited for testing."""

    class Meta:
        label = 'datapane'


def main():
    with Datapane() as app:
        app.args.add_argument('-i', '--id',
                              help='id of the dataset',
                              action='store',
                              dest='id')
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except DatapaneError as e:
            print('DatapaneError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
