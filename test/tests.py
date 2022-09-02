import os
import subprocess
import unittest


class TestBundleDevBundle(unittest.TestCase):

    def test_can_start_batect(self):
        command = ['./batect', '--version']

        env = {
            **os.environ,
            'BATECT_QUIET_DOWNLOAD': 'true',
        }

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)

        if result.returncode != 0:
            raise AssertionError(f'Command failed with exit code {result.returncode} and output: \n{result.stdout}')


if __name__ == '__main__':
    unittest.main()
