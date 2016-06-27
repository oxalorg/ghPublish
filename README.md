# ghPublish

Directly publish your blog posts to GitHub Pages from the command line.

## Installation

Install it directly from PyPI using `pip3`. Only supported on Python 3.x.

`pip3 install ghPublish`

## Quickstart

- Write a top kek blog post, preferably in markdown or html.
- Rename your blog post appropriately to how you have Jekyll configured.
    - Default is `YYYY-MM-DD-slugged-title-string.md`

Now that you have the file ready.

1. You need to **preview** the file *locally*.
    - `ghPublish --preview -f <path to file>`
    - This will render your markdown file to html and automagically open in le browser.
2. **Publish** the changes to github.
    - `ghPublish -u <Username> -f <path to file>`
    - This works for both adding new files, and updating existing ones.
    - Password is asked only once, then a token is generated and stored in a config file.

That's it. Your blog has been pushed live to `<username>.github.io`.

### Slowstart

```
$ ghPublish --help
usage: ghPublish [-h] (--preview | -u USER) -f FILE [-r REPO] [-l LOC]

Directly publish your blog posts to GitHub Pages from the command line.

optional arguments:
  -h, --help            show this help message and exit

Required:
  you can either preview the file, or supply a user to publish the file

  --preview             preview a blog post locally. (default: False)
  -u USER, --user USER  github username (default: None)
  -f FILE, --file FILE  path to local file (default: None)

Remote:
  optional details for publshing to a custom location in a repository

  -r REPO, --repo REPO  optional repository name (default: None)
  -l LOC, --loc LOC     optional file path in repostiory (default: None)
```

---

# Contributors

Author: [Mitesh Shah](http://miteshshah.com)
Please send a pull request, or file an issue!

# License

MIT License

Copyright (c) 2016 Mitesh Shah
