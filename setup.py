from setuptools import setup, find_packages

setup(
    name = 'alternative',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository - needs entry in `dependency_links`
        'diff-match-patch'
    ],

    dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        'git+ssh://git@github.com:fmoyaj/diff-match-patch.git#egg=diff-match-patch'
    ]
)