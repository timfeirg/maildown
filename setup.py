from setuptools import setup
setup(
    name='maildown',
    version='0.0.2',
    packages=['maildown'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3', 'pypandoc', 'pynliner'],

    # metadata for upload to PyPI
    author='timfeirg',
    author_email='kkcocogogo@gmail.com',
    description='simple python markdown mailer',
    license='PSF',
    keywords='mail markdown',
    url='http://example.com/HelloWorld/',
)
