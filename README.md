# markdown-figcap

Extension for [Python-Markdown] to handle `<figure>` and `<figcaption>`.

## Usage

- `%%%`  start a `<figure>`
- `%:`  start a `<figcaption>`

```python
from markdown import Markdown

text = r'''
%%%

%%% figure-class here
    ![img-alt](/source/of/img.jpg){: img-attributes here}

    %: figcaption here
    {: figcaption-attributes here}

%: will not be a figcaption
'''

md = Markdown(extensions=['markdown_figcap','attr_list'])
print(md.convert(text))
```

Output:

```html
<p>%%%</p>
<figure class="figure-class here">
<img alt="img-alt" here="here" img-attributes="img-attributes" src="/source/of/img.jpg" />
<figcaption figcaption-attributes="figcaption-attributes" here="here">figcaption here</figcaption>
</figure>
<p>%: will not be a figcaption</p>
```

## Notice

- The attributes rendering (except `<figure>`'s class) is supported by the origin [Python-Markdown]'s  [`attr_list`] extension.
- Figure starter only will not be rendered as `<figure>`.
- Figcaption starter will not take effect until it is in the `figure` block.
- If the `<p>` in `<figure>` has no text and only one `<img>` child, the `<p>` tag will be got rid of.

## Installation

From [PyPI]:
```
pip install markdown-figcap
```

[Python-Markdown]: https://python-markdown.github.io/
[PyPI]: https://pypi.org/project/markdown-figcap/
[`attr_list`]: https://python-markdown.github.io/extensions/attr_list/
