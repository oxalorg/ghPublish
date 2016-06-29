import argparse
import os
import requests
import json
import base64
from ghPublish import auth


class Publish:
    def __init__(self, user, fp, repo=None, path=None):
        # Set required derived variables
        self.title = os.path.basename(fp)
        self.path = path + '/' + self.title if path else '_posts/' + self.title
        self.owner = user
        if repo:
            self.repo = repo
        else:
            self.repo = self.owner + '.github.io'
        self.fp = fp
        self.api_url = 'https://api.github.com/repos/{owner}/{repo}/contents/{path}'.format(
            owner=self.owner, repo=self.repo,
            path=self.path)

        # Set base64 encoded content of file
        with open(os.path.abspath(self.fp)) as f:
            self.content_base64 = base64.b64encode(f.read().encode('utf-8'))

    def get_auth_details(self):
        return auth.Authorization(self.owner).get_auth_details()

    def get_sha_blob(self):
        """
        if the current file exists
            returns the sha blob
        else
            returns None
        """
        r = requests.get(self.api_url, auth=self.get_auth_details())
        try:
            return r.json()['sha']
        except KeyError:
            return None

    def publish_post(self):
        """
        If it's a new file, add it.
        Else, update it.
        """
        payload = {'content': self.content_base64.decode('utf-8')}

        sha_blob = self.get_sha_blob()
        if sha_blob:
            commit_msg = 'ghPublish UPDATE: {}'.format(self.title)
            payload.update(sha=sha_blob)
            payload.update(message=commit_msg)
        else:
            commit_msg = 'ghPublish ADD: {}'.format(self.title)
            payload.update(message=commit_msg)

        r = requests.put(self.api_url,
                         auth=self.get_auth_details(),
                         data=json.dumps(payload))
        try:
            url = r.json()['content']['html_url']
            return r.status_code, url
        except KeyError:
            return r.status_code, None
