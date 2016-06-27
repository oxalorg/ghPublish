import argparse
from ghPublish.ghPublish import preview_file, Publish


def cli():
    parser = argparse.ArgumentParser(
        description='Directly publish your blog posts to GitHub Pages from the command line.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    required_group = parser.add_argument_group(
        'Required',
        'you can either preview the file, or supply a user to publish the file')
    group = required_group.add_mutually_exclusive_group(required=True)
    group.add_argument('--preview',
                       dest='prev',
                       action='store_true',
                       help='preview a blog post locally.')
    group.add_argument('-u',
                       '--user',
                       dest='user',
                       default=None,
                       help='github username')
    required_group.add_argument('-f',
                                '--file',
                                dest='file',
                                required=True,
                                help='path to local file')
    optional = parser.add_argument_group(
        'Remote',
        'optional details for publshing to a custom location in a repository')
    optional.add_argument('-r',
                          '--repo',
                          dest='repo',
                          default=None,
                          help='optional repository name')
    optional.add_argument('-l',
                          '--loc',
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


if __name__ == '__main__':
    cli()
