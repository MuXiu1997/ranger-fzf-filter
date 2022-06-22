import ranger.api.commands

from .filter import FzfFilter


class fzf_filter(ranger.api.commands.Command):
    """
    :fzf_filter <query>

    Flags:
    -r   Filter through all subfolders recursively

    Filter with fzf
    """

    RECURSIVE_FILTER = 'r'

    def __init__(self, *args, **kwargs):
        super(fzf_filter, self).__init__(*args, **kwargs)
        self.flags, self.rest = self.parse_flags()

    def execute(self):
        if self.RECURSIVE_FILTER in self.flags:
            self.fm.execute_console('flat -1')

        self.fm.thisdir.__dict__['fzf_filter'] = self._build_filter()
        self.fm.thisdir.refilter()
        if self.quickly_executed:
            self.fm.open_console(self.line)

    def cancel(self):
        if self.RECURSIVE_FILTER in self.flags:
            self.fm.execute_console('flat 0')

        self.fm.thisdir.__dict__['fzf_filter'] = None
        self.fm.thisdir.refilter()

    def quick(self):
        return True

    def _build_filter(self):
        directory = self.fm.thisdir.path
        source = [i.relative_path for i in self.fm.thisdir.files_all]
        query = ' '.join(self.rest)
        return FzfFilter(directory, source, query)
