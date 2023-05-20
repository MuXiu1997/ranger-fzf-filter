import os.path
import subprocess


class FzfFilter:
    def __init__(self, thisdir, query):
        self.thisdir = thisdir
        self.files_all = thisdir.files_all

        self.query = query

        self.source = None
        self.recalc_source()

        self.result = None
        self.recalc_result()

    def recalc_source(self):
        """Recalculate the source list based on the files in the current directory"""
        self.source = [f.relative_path for f in self.thisdir.files_all]

    def recalc_result(self):
        # Recalculate the result list by executing the fzf command
        cmd = subprocess.Popen(
            ['fzf', '-f', self.query],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        stdout, _ = cmd.communicate('\n'.join(self.source).encode('utf-8'))
        self.result = stdout.decode('utf-8').strip().splitlines()

    def set_query(self, query):
        self.query = query
        self.recalc_result()

    def __call__(self, fobj):
        # Check if the files in the current directory have changed, and recalculate source and result if needed
        if self.thisdir.files_all is not self.files_all:
            self.files_all = self.thisdir.files_all
            self.recalc_source()
            self.recalc_result()

        if os.path.relpath(fobj.path, fobj.relative_path) != '.':
            return True

        return fobj.relative_path in self.result
