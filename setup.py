from setuptools import setup

setup(
    name='google-photos-archiver',
    version='2.2.0',
    py_modules=['gparch', 'gparch_cli'],
    install_requires=[
        'piexif',
        'pillow',
        'tqdm',
        'requests',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'colorama',
        'sanitize-filename'
    ],
    entry_points={'console_scripts': ['gparch_cli=gparch_cli:main']},
    author='Nicholas Dawson',
    description='Tool to mirror your Google Photos library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='GPLv3',
)
