import ranger.api.commands
from .filter import FzfFilter

# noinspection PyUnreachableCode
# This is done to enhance auto-completion and inference in the editor.
if False:
    import ranger.core.fm

KEY_FZF_FILTER = 'fzf_filter'


# noinspection PyPep8Naming,PyUnresolvedReferences
class fzf_filter(ranger.api.commands.Command):
    """
    :fzf_filter <query>

    This command allows you to use fzf fuzzy search to filter files and directories in the ranger.
    """

    def execute(self):
        fm = self.fm  # type: ranger.core.fm.FM
        # Check if a filter is already set
        _filter = fm.thisdir.__dict__.get(KEY_FZF_FILTER, None)
        if isinstance(_filter, FzfFilter):
            # If a filter is set, just update the query
            _filter.set_query(self._get_query())
        else:
            # If no filter is set, build a new one
            fm.thisdir.__dict__[KEY_FZF_FILTER] = self._build_filter()

        fm.thisdir.refilter()
        if self.quickly_executed:
            fm.open_console(self.line)

    def cancel(self):
        fm = self.fm  # type: ranger.core.fm.FM
        fm.thisdir.__dict__[KEY_FZF_FILTER] = None
        fm.thisdir.refilter()

    def quick(self):
        return True

    def _get_query(self):
        """
        Get the search query.

        Returns:
            str: The search query.
        """
        return self.rest(1)

    def _build_filter(self):
        """
        Build a new FzfFilter.

        Returns:
            FzfFilter: A new FzfFilter object with the current directory and search query.
        """
        return FzfFilter(self.fm.thisdir, self._get_query())
