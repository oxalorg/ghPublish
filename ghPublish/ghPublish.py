import argparse
import preview
import os
import requests
import json
import base64


def preview_file(post):
    """
    Opens the rendered markdown file (as html) locally in a browser.
    """
    with open(post) as f:
        content = f.read()
    title = os.path.basename(post)
    preview.Preview(title, content).preview()


class Publish:
    def __init__(self, user, fp, repo=None, path=None):
        # Set required derived variables
        self.title = os.path.basename(fp)
        self.path = path + '/' + self.title if path else '_posts/' + self.title
        self.owner = user
        if repo:
            self.repo = repo
        else:
            self.repo = owner + '.github.io'
        self.fp = fp
        self.api_url = 'https://api.github.com/repos/{owner}/{repo}/contents/{path}'.format(
            owner=self.owner, repo=self.repo,
            path=self.path)

        # Set base64 encoded content of file
        with open(os.path.abspath(self.fp)) as f:
            self.content_base64 = base64.b64encode(f.read().encode('utf-8'))

        # Get config file
        with open(os.path.join(os.path.expanduser('~'), '.ghPublish')) as f:
            self.config = json.load(f)

    def get_auth_details(self):
        return (self.owner, self.get_api_token())

    def get_api_token(self):
        return self.config[self.owner]

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Publish your posts on GitHub pages.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--preview',
                       dest='prev',
                       action='store_true',
                       help='preview a blog post locally.')
    group.add_argument('-u',
                       '--user',
                       dest='user',
                       default=None,
                       help='hithub Username')
    parser.add_argument('-f',
                        '--file',
                        dest='file',
                        required=True,
                        help='path to local file')
    parser.add_argument('-r',
                        '--repo',
                        dest='repo',
                        default=None,
                        help='optional repository')
    parser.add_argument('-l',
                        '--location',
                        dest='loc',
                        default=None,
                        help='optional file path in repostiory')
    args = parser.parse_args()

    if args.prev:
        preview_file(args.file)
    elif args.user:
        status, url = Publish(args.user, args.file, args.repo,
                              args.loc).publish_post()
        if status in (200, 201):
            print('Sucessfuly published at {}'.format(url))
        else:
            print(
                'Error occurred! Contact the author at: mitesh@miteshshah.com')
    else:
        print("Run ghPublish --help for usage information")
