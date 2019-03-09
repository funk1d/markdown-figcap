from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='markdown-figcap',
    version='0.1.1',
    description=
    'Extension for Python-Markdown to handle <figure> and <figcaption>.',
    url='https://github.com/funk1d/markdown-figcap',
    author='funkid',
    author_email='fuunk1d@g.mailcom',
    license='BSD License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['markdown_figcap'],
    install_requires=['Markdown>=3.0.1'],
    classifiers=[
        'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: HTML'
    ])
