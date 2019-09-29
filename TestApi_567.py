import unittest
from unittest.mock import patch


class BuggyApiTest(unittest.TestCase):

    @patch('Api_567.get_github')
    def test_check_api(self, mock_get_github):
        mock_get_github.return_value = ['Repo: hellogitworld Number of commits: 30',
                                        'Repo: helloworld Number of commits: 6',
                                        'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2',
                                        'Repo: threads-of-life Number of commits: 1']
        self.assertEqual(['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6',
                          'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2',
                          'Repo: threads-of-life Number of commits: 1'],mock_get_github('richkempinski'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
