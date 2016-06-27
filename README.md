# ghPublish

Directly publish your blog posts to GitHub Pages from the command line.

## Installation

Install it directly from PyPI using `pip3`. Only supported on Python 3.x.

`pip3 install ghPublish`

## How it works?

1. Head over [here](https://github.com/settings/tokens/new) and generate a new token with only `public_repo` scope selected.
2. For every github username you want to acess, create a file `~/.ghPublish` as following:
    - ```javascript
      {
          'MiteshNinja': '<api token here>',
          'Computableverse': '<api token here>'
      }
      ```
    - You can make it `rw` only by you, using `chmod 600 ~/.ghPublish`
3. Rename your blog post appropriately to how you have Jekyll configured.
    - Default is `YYYY-MM-DD-slugged-title-string`
5. Now read Usage below.

### Usage - Simple

Now that you have the file ready.

1. You need to **preview** the file *locally*.
    - `ghPublish --preview -f <path to file>`
    - This will render your markdown file to html
    - Then open it in your default web browser for previewing.
    - You can also use this command to render any markdown files.
2. **Commit** the changes to github.
    - `ghPublish -u <Username> -f <path to file>`
    - This works for both adding new files, and updating existing ones.
    - *PS: Username should **exactly** match to a Key in ~/.ghPublish json file.*

That's it. Your blog has been pushed live to `username.github.io`.

### Usage - Detailed

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
