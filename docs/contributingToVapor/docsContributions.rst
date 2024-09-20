Docs Contributions
==================

Vapor's documentation website is managed in its own `GitHub Repo <https://github.com/NCAR/VaporDocumentationWebsite>`_ and uses the `Sphinx <https://www.sphinx-doc.org/en/master/>`_ documentation generator. The documentation is generated from the .rst files within the docs directory. (Generating documentation for the `Python Class Reference <https://ncar.github.io/VaporDocumentationWebsite/pythonAPIReference/classReference.html>`_ has some extra steps, and is explained later.)

To make changes to the documentation, follow these steps:

1. Fork the documentation GitHub repository and clone the fork to your local machine
2. Within this clone, make changes to the appropriate .rst files
3. View your changes by generating the documentation locally, following the instructions below
4. Push the updated .rst and newly generated html files to your forked repository
5. Open a pull request to merge your fork with the main repository

To reproduce this documentation locally, we recommend setting up a conda environment with the environment.yml file included in this repo. Once installed, the .rst files located in the docs/ directory can be edited to produce new html.

To build your conda environment, run the following commands in your terminal.

.. code-block:: console

    cd VaporDocumentationWebsite
    conda config --add channels conda-forge
    conda env create -f environment.yml
    conda activate VaporDocumentationWebsite
    pip install sphinxcontrib-googleanalytics

Once this conda environment has been configured, the html can be generated with the following steps.

.. code-block:: console

    cd VaporDocumentationWebsite/docs
    make html
    cp -r html/* ../

The third line moves the html files from VaporDocumentationWebsite/docs/html to the root directory, VaporDocumentationWebsite. Without this step, github pages will not host the html files.

Contributing to Python Class Reference
======================================

If you want to make changes to the python class reference, there are a couple of additional steps. Sphinx builds the class reference from the version of Vapor Python installed in your current conda environment using comments within the code. To make changes to the function descriptions, you'll need to edit the comments for the function in the code, which will either be in a Python file or a C++ header file. Here is a step by step guide:

1. Fork both VAPOR's `main repository <https://github.com/NCAR/VAPOR>`_ and Vapor's `documentation repository <https://github.com/NCAR/VaporDocumentationWebsite>`_. You'll need to submit changes to both of these repositories. Clone each of these forks to your local machine.
2. Within the VAPOR clone, make changes to the comments in the appropriate .py and .h files.

    Editing the GetRenderer function in /VAPOR/apps/pythonapi/vapor/session.py using Python syntax:

    .. code-block:: python

        ...
        def GetRenderer():
            """
            Add new comment between triple quotes directly after function definition
            """
        ...

    Editing the SetAxisAnnotationEnabled function in /VAPOR/include/vapor/AxisAnnotations.h using C++ and Doxygen syntax:

    .. code-block:: cpp

        ...
        //! Add new comment directly before function definition
        bool SetAxisAnnotationEnabled(bool val);
        ...

3. Create the VaporDocumentationWebsite conda environment:

.. code-block:: console

    cd VaporDocumentationWebsite
    conda config --add channels conda-forge
    conda env create -f environment.yml
    conda activate VaporDocumentationWebsite
    pip install sphinxcontrib-googleanalytics
    pip install sphinx-copybutton

4. Build Vapor Python from the source code in your VAPOR clone following `these instructions <https://ncar.github.io/VaporDocumentationWebsite/contributingToVapor/codeContributions.html#building-vapor-s-python-api-from-source>`_.
5. Generate the html on your local machine

.. code-block:: console

    cd VaporDocumentationWebsite/docs
    make html
    cp -r html/* ../
6. Preview the html to make sure everything displays as intended
7. Push all changes you made in the VAPOR repository (.py and .h files) and in the VaporDocumentationWebsite repository (.rst and .html files).
8. Open a pull request in both repositories to merge the changes.
