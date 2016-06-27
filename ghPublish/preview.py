import os
import webbrowser
from string import Template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from ghPublish import base_html


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class Preview:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.base_template = base_html.html
        self.template = Template(self.base_template)

    def render(self):
        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        marked = markdown(self.content)
        final_html = self.template.substitute(dict(title=self.title,
                                                   content=marked))
        return final_html

    def show(self, final_html):
        preview_file = '/tmp/ghPublishPreview.html'
        with open(preview_file, 'w') as f:
            f.write(final_html)
        webbrowser.open_new_tab(preview_file)

    def preview(self):
        preview_html = self.render()
        self.show(preview_html)


if __name__ == '__main__':
    # Unit test seemed excessive.
    # Also this is mostly producing a side effect (browser window),
    # and no need to test 'mistune'.
    title = 'Test markdown'
    with open(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'test.md')) as f:
        content = f.read()
    Preview(title, content).preview()
