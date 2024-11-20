Building Vapor's Python API from source 
---------------------------------------

To build Vapor's Python API from source, you will need to install either Anaconda or Miniconda onto your system.  `Download here <https://www.anaconda.com/products/distribution>`_.  Once installed, :ref:`fork Vapor's github repository <contributing.environment>` then build and install the .tar.bz2 package by following the steps below.

Building the conda image
************************

These steps generate a .tar.bz2 bundle that you can locally install with conda, instead of fetching a package from a remote repository like conda-forge.

1) After cloning Vapor, installing Anaconda/Miniconda, and modifying source code if needed, cd into the /conda directory:

.. code-block:: console

    cd ~/VAPOR/conda

2) Install the conda-build package on your current Anaconda/Miniconda installation:

.. code-block:: console

    conda install conda-build

3) Install the conda-forge channel, which Anaconda/Miniconda will use to gather libraries for your build:

.. code-block:: console

    conda config --add channels conda-forge

4) Execute the conda build command on your current code base:

.. code-block:: console

    conda build .

Note: If you get a build error referencing CMakeLists.txt at this point, delete everything in your VAPOR/build directory and try re-running the above command.

Alternatively, add cmake build flags to your conda build such as the following:

.. code-block:: console

    DEBUG_BUILD=false MAP_IMAGES_PATH="<path_to_images>" conda build .


If the build is successful a conda package file will be created. The path to the file will be created at the end of the “conda build” step, and will look something like:

.. code-block:: console

    $CONDA_PREFIX/conda-bld/osx-64/vapor-3.6.0-ha5a8b8e_0.tar.bz2

.. note::

    $CONDA_PREFIX is an environment variable that points to your conda installation path.

Installing the conda image
**************************

Once you've built a .tar.bz2 conda image for your customized version of Vapor, follow these steps to install it:

1) Create a local conda channel on your computer that will host your new .tar.bz file for installation.  Note - If you're on OSX, name your directory osx-64, or if you're on linux, name it linux-64.

.. code-block:: console

    mkdir -p ~/channel/osx-64
    or
    mkdir -p ~/channel/linux-64

2) Move your created .tar.bz2 package from its initial directory into your channel

.. code-block:: console

    mv ~/tmp/miniconda/envs/xarray/conda-bld/osx-64/vapor-3.6.0-ha5a8b8e_0.tar.bz2 ~/channel/osx-64
    or
    mv ~/tmp/miniconda/envs/xarray/conda-bld/linux-64/vapor-3.6.0-ha5a8b8e_0.tar.bz2 ~/channel/linux-64

3) Index your new channel, so conda knows about it:

.. code-block:: console

    conda index ~/channel

4) If you have not done so already, ensure that you have added the conda-forge channel:

.. code-block:: console

    conda config --add channels conda-forge

5) Create a new conda environment to install Vapor onto, or select a pre-existing environment:

.. code-block:: console

    conda create --name vapor
    conda activate vapor
    or
    conda activate myEnvironment

6) Finally install the custon .tar.bz2 package:

.. code-block:: console

    conda install -c file://<pathToYourChannel> vapor

Note: It may be necessary to re-run *conda config --add channels conda-forge* at this step.

7) Verify that your new installation works:

.. code-block:: console

    python
    import vapor

Example python scripts and jupyter notebooks can be found in $CONDA_PREFIX/lib/python3.<version>/site-packages/vapor


Python Open Source Utilities
____________________________

Vapor Python supports a number of utility functions, found under apps/pythonapi/vapor/utils. If you write a function for your workflows that you believe would be useful to other users, we encourage you to add the function to Vapor utils.
