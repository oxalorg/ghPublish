import requests
import os
import json
import getpass
from requests.auth import HTTPBasicAuth


class PassPromptAuth(HTTPBasicAuth):
    def __init__(self, username):
        self.username = username
        self.password = getpass.getpass()


class Authorization():
    config_file = os.path.join(os.path.expanduser('~'), '.ghPublish')
    AUTH_URL = 'https://api.github.com/authorizations'

    def __init__(self, user):
        self.user = user.lower()

    def get_auth_details(self):
        return (self.user, self.get_api_token())

    def get_api_token(self):
        try:
            return self._get_config()['tokens'][self.user]
        except KeyError:
            return self._update_config()

    def _get_config(self):
        try:
            if not os.path.exists(self.config_file):
                config = {"tokens": {}, "defaults": {}, "settings": {}}
                with open(self.config_file, 'a') as f:
                    json.dump(config, f)
            else:
                with open(self.config_file) as f:
                    config = json.load(f)
            return config

        except JSONDecodeError:
            raise SystemExit(
                'Your configuration file seems to be broken! JSON cannot be decoded.')
        except IsADirectoryError:
            raise SystemExit(
                "~/.ghPublish must not exist as a directory. Cannot store configuration.")

    def _request_access_token(self):
        note = "ghPublish: Directly publish your blog posts to GitHub Pages from the command line."
        note_url = 'https://github.com/MiteshNinja/ghPublish'
        scopes = ["public_repo"]
        payload = dict(note=note, scopes=scopes, note_url=note_url)
        print("Visit: https://github.com/settings/tokens to manage tokens.\n")
        print("Requesting one-time ACCESS TOKEN for user: " + self.user)
        r = requests.post(self.AUTH_URL,
                          auth=PassPromptAuth(self.user),
                          data=json.dumps(payload))

        rj = r.json()
        if r.status_code == 201:
            return rj['token']
        elif r.status_code == 401 and rj['message'].lower(
        ) == 'bad credentials':
            raise SystemExit('Bad credentials!')
        elif r.status_code == 422 and rj['message'].lower(
        ) == 'validation failed':
            raise SystemExit(
                'Validation has failed!\nThe response received was:\n {}'.format(
                    rj))
        else:
            raise SystemExit(
                'An error has occurred while creating a token!\nThe response received was:\n {}'.format(
                    rj))

    def _update_config(self):
        config = self._get_config()
        token = self._request_access_token()
        config['tokens'][self.user] = token
        with open(self.config_file, 'w') as f:
            json.dump(config, f)
        return token


if __name__ == '__main__':
    a = Authorization('MiteshNinja')
    print(a.get_auth_details())
