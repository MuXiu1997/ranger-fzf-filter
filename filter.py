import os.path
import subprocess


class FzfFilter:
    """
    A filter class for FZF fuzzy search.

    Attributes:
        thisdir (ranger.container.directory.Directory): The current directory.
        query (str): The search query.
        source (list[str]): List of relative paths of all files in the current directory.
        result (list[str]): The result of fzf search.
    """

    def __init__(self, thisdir, query):
        """
        Initialize the FzfFilter class.

        Args:
            thisdir (ranger.container.directory.Directory): The current directory.
            query (str): The search query.
        """
        self.thisdir = thisdir
        self.files_all = thisdir.files_all

        self.query = query

        self.source = []
        self.recalc_source()

        self.result = []
        self.recalc_result()

    def recalc_source(self):
        """
        Recalculate the source list based on the files in the current directory.
        """
        self.source = [f.relative_path for f in self.thisdir.files_all]

    def recalc_result(self):
        """
        Recalculate the result list by executing the fzf command.
        """
        cmd = subprocess.Popen(
            ['fzf', '-f', self.query],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        stdout, _ = cmd.communicate('\n'.join(self.source).encode('utf-8'))
        self.result = stdout.decode('utf-8').strip().splitlines()

    def set_query(self, query):
        """
        Update the query and recalculate the result list.

        Args:
            query (str): The new search query.
        """
        self.query = query
        self.recalc_result()

    def __call__(self, fobj):
        """
        Perform the actual filtering.

        Args:
            fobj (ranger.container.file.File | ranger.container.directory.Directory): The file or directory to check.

        Returns:
            bool: True if the file or directory is in the result list, False otherwise.
        """
        # Check if the files in the current directory have changed, and if so, recalculate source and result
        if self.thisdir.files_all is not self.files_all:
            self.files_all = self.thisdir.files_all
            self.recalc_source()
            self.recalc_result()

        # Ensure the relative path start of the file or directory is in the current directory
        if os.path.relpath(fobj.path, fobj.relative_path) != '.':
            return True

        # Check if the relative path of the file or directory is in the result list
        return fobj.relative_path in self.result
