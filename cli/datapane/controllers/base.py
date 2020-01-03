from cement import Controller, ex
from cement.utils.version import get_version_banner
from core.version import get_version

VERSION_BANNER = """
The quickest way to share datasets and results. %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'The quickest way to share datasets and results.'

        # text displayed at the bottom of --help output
        epilog = 'Usage: datapane command1 --foo bar'

        # controller level arguments. ex: 'datapane --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()
