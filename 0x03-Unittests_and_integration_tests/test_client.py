#!/usr/bin/env python3
''' Test utils '''
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from requests import HTTPError
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class

from fixtures import TEST_PAYLOAD
TEST_PAYLOAD = TEST_PAYLOAD[0]


class TestGithubOrgClient(unittest.TestCase):
    ''' Test github org client '''
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        ''' Test org '''
        mock_get_json.return_value = MagicMock(return_value=expected)
        org = GithubOrgClient(org_name)
        self.assertEqual(org.org(), expected)
        mock_get_json.assert_called_once_with(
            org.ORG_URL.format(org=org_name)
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        ''' Test public repos '''
        payload = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"},
        ]
        mock_get_json.return_value = payload
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_repos_url:
            org = GithubOrgClient("google")
            repo = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = repo
            self.assertEqual(org.public_repos(), ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(repo)

    def test_public_repos_url(self):
        ''' Test public repos url '''
        repo = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": repo}
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            org = GithubOrgClient("google")
            self.assertEqual(org._public_repos_url, repo)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        ''' Test has license '''
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0],
        "repos_payload": TEST_PAYLOAD[1],
        "expected_repos": TEST_PAYLOAD[2],
        "apache2_repos": TEST_PAYLOAD[3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    ''' testIntegrationGithubOrgClient class '''

    @classmethod
    def setUpClass(cls):
        ''' Set up class '''
        cls.github_api_base_url = "https://api.github.com"
        cls.org_url = "{}/orgs/google".format(cls.github_api_base_url)
        cls.repos_url = "{}/orgs/google/repos".format(cls.github_api_base_url)

        cls.github_api_responses = {
            cls.org_url: cls.org_payload,
            cls.repos_url: cls.repos_payload,
        }

        def mock_get_response(url):
            ''' Mock side effect '''
            if url in cls.github_api_responses:
                mock_response = Mock()
                mock_response.json.return_value = cls.github_api_responses[url]
                return mock_response
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=mock_get_response)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        ''' Tear down class '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        ''' Test public repos '''
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        ''' Test public repos with license '''
        org = GithubOrgClient("google")
        output = org.public_repos(license="apache-2.0")
        self.assertEqual(output, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
