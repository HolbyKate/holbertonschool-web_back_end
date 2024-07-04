#!/usr/bin/env python3
"""set up the TestGithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        response = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, expected_response)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Method that test expected result"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        client = GithubOrgClient('google')
        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):

        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient('google')
            repos = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            """Test that the mocked get_json was called once with the correct argument"""
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
