import unittest

from Api_567 import get_github


class BuggyApiTest(unittest.TestCase):
    def test_check_api(self):
        self.assertEqual(get_github('richkempinski'),
                         ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6',
                          'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2',
                          'Repo: threads-of-life Number of commits: 1']
                         )


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
