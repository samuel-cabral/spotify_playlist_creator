from setuptools import setup, find_packages

setup(
    name='spotify-playlist-creator',
    version='0.0.1',
    author='Samuel Cabral',
    description='Uma simples aplicação python para criar playlists na sua conta do Spotify',
    packages=find_packages(),
    install_requires=[
        'spotipy',
        'python-dotenv'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
