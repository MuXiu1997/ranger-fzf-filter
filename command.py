import ranger.api.commands
from .filter import FzfFilter


class fzf_filter(ranger.api.commands.Command):
    """
    :fzf_filter <query>

    Filter with fzf
    """

    def execute(self):
        # If a filter is already set, just update the query
        _filter = self.fm.thisdir.__dict__.get('fzf_filter', None)
        if isinstance(_filter, FzfFilter):
            _filter.set_query(self._get_query())
        else:
            self.fm.thisdir.__dict__['fzf_filter'] = self._build_filter()

        self.fm.thisdir.refilter()
        if self.quickly_executed:
            self.fm.open_console(self.line)

    def cancel(self):
        self.fm.thisdir.__dict__['fzf_filter'] = None
        self.fm.thisdir.refilter()

    def quick(self):
        return True

    def _get_query(self):
        return self.rest(1)

    def _build_filter(self):
        return FzfFilter(self.fm.thisdir, self._get_query())
