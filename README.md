# ghPublish

Directly publish your blog posts to GitHub Pages from the command line.

## How it works?

- Head over [here](https://github.com/settings/tokens/new) and generate a new token with only `public_repo` scope selected.
- For every github username you want to acess, create a file `~/.ghPublish` as following:
    ```json
    {
        'MiteshNinja': '<api token here>',
        'Computableverse': '<api token here>'
    }
    ```
    - You can make it `rw` only by you, using `chmod 600 ~/.ghPublish`
- Write a blog post in markdown.
- Rename the post appropriately to how you have Jekyll configured.
    - Default is `YYYY-MM-DD-slugged-title-string`
- Now read Usage below.

## Usage - Simple

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

## Usage - Detailed

```
$ python3 ghPublish --help
usage: ghPublish.py [-h] (--preview | -u USER) -f FILE [-r REPO] [-l LOC]

Publish your posts on GitHub pages.

optional arguments:
  -h, --help             show this help message and exit
  --preview              preview a blog post locally. (default: False)
  -u USER, --user USER   hithub Username (default: None)
  -f FILE, --file FILE   path to local file (default: None)
  -r REPO, --repo REPO   optional repository (default: None)
  -l LOC, --location LOC optional file path in repostiory (default: None)
```

---

# License

MIT License

Copyright (c) 2016 Mitesh Shah
