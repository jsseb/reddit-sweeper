# reddit-sweeper
Small command-line program to download all imgur and gfycat links from a subreddit.

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [OPTIONS](#options)
- [FAQ](#faq)
- [BUGS](#bugs)
- [COPYRIGHT](#copyright)


# INSTALLATION
On Linux you can use pip:

    sudo pip install reddit-sweeper

Or just clone the repository and install the requirements:

    git clone https://github.com/jsseb/reddit-sweeper.git
    pip install -r requirements
    reddit-sweeper [OPTIONS] SUBREDDIT [SUBREDDIT...]

# DESCRIPTION
**reddit-sweeper** is a small command-line program to download imgur images and gfycat webm from
a given subreddit. It requires the Python interpreter, version 3.3+. It is released to the public domain,
which means you can modify it, redistribute it or use it however you like.

    reddit-sweeper [OPTIONS] SUBREDDIT [SUBREDDIT...]
    
# OPTIONS
    -h, --help                       Print this help text and exit
    --version                        Print program version and exit
    -i, --ignore-errors              Continue on download errors, for example to
                                     skip unavailable videos in a playlist

# FAQ

# BUGS
Bugs and suggestions should be reported at: <https://github.com/jsseb/reddit-sweeper/issues>.

# COPYRIGHT

reddit-sweeper is released into the public domain by the copyright holders.
