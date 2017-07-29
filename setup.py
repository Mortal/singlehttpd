from setuptools import setup, find_packages


DESCRIPTION = '''\
Serve a single file download via HTTP
'''.rstrip()

CONSOLE_SCRIPTS = [
    'singlehttpd = singlehttpd:main',
]


headline = DESCRIPTION.split('\n', 1)[0].rstrip('.')


setup(
    name='singlehttpd',
    version='0.1',
    description=headline,
    long_description=DESCRIPTION,
    author='https://github.com/Mortal',
    url='https://github.com/Mortal/singlehttpd',
    py_modules=['singlehttpd'],
    include_package_data=True,
    license='GPLv3',
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'aiohttp',
    ]
)
