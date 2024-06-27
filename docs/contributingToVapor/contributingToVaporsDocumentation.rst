Contributing to Vapor's Documentation
_____________________________________

Vapor uses the `Sphinx <https://www.sphinx-doc.org/en/master/>`_ documentation generator.  

To contribute to Vapor's documentation, follow the three steps below.  Python version 3.7 or higher is required.

1) Install the following requirements.  There is more than one way to do this, and ``pip`` is one recommendation.

.. code-block:: console

    python -m pip install sphinx
    python -m pip install sphinx_rtd_theme
    python -m pip install sphinx_gallery
    python -m pip install xarray
    python -m pip install numpy
    python -m pip install matplotlib

2) Checkout Vapor's ``readTheDocs`` branch, then enter the ``docs`` directory.

.. code-block:: console

    cd ~/VAPOR
    git checkout readTheDocs
    cd docs

3) Explore Vapor's documentation by reading and editing the .rst files in this directory, then build the documentation

.. code-block:: console

    make html

The documentation .html files will be written in the ``html`` directory (ie. ~/VAPOR/docs/html) for viewing in a web browser.
