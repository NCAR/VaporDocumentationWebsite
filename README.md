# VaporDocumentationWebsite
This repository holds the html files that are used to host [Vapor's documentation github page](https://ncar.github.io/VaporDocumentationWebsite/).

We use the Sphinx documentation generator to produce the html for the website.

To reproduce this documentation locally, we recommend setting up a conda environment with the environment.yml file included in this repo.  Once installed, the .rst files located in the docs/ directory can be edited to produce new html.

    $ git clone https://github.com/NCAR/VaporDocumentationWebsite.git
    $ cd VaporDocumentationWebsite
    $ conda config --add channels conda-forge
    $ conda env create -f environment.yml
    $ conda activate VaporDocumentationWebsite
    $ pip install sphinxcontrib-googleanalytics

Once this conda environtment has been configured, the html can be generated with the following steps.

1) cd VaporDocumentationWebsite/docs
2) make html
3) cp -r html/* ../

Note that step 4 moves the html files from VaporDocumentationWebsite/docs/html to the root directory, VaporDocumentationWebsite.  Without this step, github pages will not host the the html files.
