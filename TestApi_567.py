import unittest

from Api_567 import get_github


class BuggyApiTest(unittest.TestCase):
    def test_check_api(self):
        self.assertEqual(get_github('woshitc8535'),
                         ['Repo: GitHubApi567 Number of commits: 3', 'Repo: hello-world Number of commits: 5',
                          'Repo: SSW_567 Number of commits: 10', 'Repo: wenxuanLiu Number of commits: 1'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
