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
- Run the command `ghPublish <username> <path to blog post>`

---

# License

MIT License

Copyright (c) 2016 Mitesh Shah
