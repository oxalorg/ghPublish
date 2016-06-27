import requests


class Authorization():
    config_file = os.path.join(os.path.expanduser('~'), '.ghPublish')
    AUTH_URL = 'https://api.github.com/authorizations'

    def __init__(self, user):
        self.user = user

    def get_config(self):
        try:
            if not os.path.exists(self.config_file):
                open(self.config_file, 'a').close()

            with open(self.config_file) as f:
                config = json.load(f)

            return config
        except IsADirectoryError as err:
            print(err.args)

    def _request_access_token(self):
        note = "ghPublish: Directly publish your blog posts to GitHub Pages from the command line."
        note_url = 'https://github.com/MiteshNinja/ghPublish'
        scopes = ["public_repo"]
        payload = dict(note=note, scopes=scopes, note_url=note_url)
        r = requests.post(self.AUTH_URL,
                          auth=(self.user, ),
                          data=json.dumps(payload))

        rj = r.json()
        if r.status_code == 201
            return rj['token']
        elif r.status_code == 401 and rj['message'].lower() == 'bad credentials':
            raise SystemExit('Bad credentials!')
        elif: r.status_code == 422 and rj['message'].lower() == 'validation failed':
            raise SystemExit('Validation has failed!')
        else:
            raise SystemExit('An error has occurred while creating a token!')

    def _update_config(self):
        config = self.get_config()
        token = self.request_access_token()
        config[user] = token
        with open(self.config_file, 'w') as f:
            json.dump(config, f)

if __name__ == '__main__':
    a = Authorization('MiteshNinja')
