Building Vapor's Python API from source 
---------------------------------------

For generating a tar.bz2 installer bundle for testing or hosting on a remote server such as the one we use on `Anaconda.org <htt    ps://anaconda.org/Ncar-vapor/repo>`_, you will need to install `Anaconda <https://www.anaconda.com/products/distribution>`_ or something similar.  Once installed, :ref:`fork Vapor's github repository <contributing.environment>`, then build and install the generated tar.bz2 bundle by following the steps below.

Building a local conda bundle
_____________________________

1. After forking Vapor and installing Anaconda, open a new console that will be in the (base) environment.  Add access to the conda-forge channel, create a new environment with the packages conda-build and activate it.

.. code-block:: console

    conda config --add channels conda-forge
    conda create -n myEnvironment conda-build
    conda activate myEnvironment

2. After making necessary changes to the source code, cd into VAPOR's /conda directory.

.. code-block:: console

    cd ~/VAPOR/conda

3. Execute the conda build command with default parameters or optional ones.

.. code-block:: console

    conda build . (default)
    DEBUG_BUILD=false MAP_IMAGES_PATH="<path_to_images>" conda build . (extra options)

.. note:: If you get a build error referencing CMakeLists.txt at this point, delete everything in your VAPOR/build directory and try re-running the above command.

If the build is successful a tar.xz bundle will be created in a directory shown below, where <OS> represents the operating system the bundle was built for.  $CONDA_PREFIX is a variable in your current conda environment.

.. code-block:: console

    $CONDA_PREFIX/conda-bld/<OS>/vapor-3.6.0-ha5a8b8e_0.tar.bz2

+------------------+-----------+
| Operating System | Directory |
+==================+===========+
| MacOS x86        | osx-64    |
+------------------+-----------+
| MacOS ARM        | osx-arm64 |
+------------------+-----------+
| Linux x86        | linux-64  |
+------------------+-----------+

Installing a local conda image
______________________________

Once you've built a tar.bz2 image or downloaded one from another source, you can install it as follows.

.. note:: If you downloaded your .tar.bz2 file from another source, you will need to create a new environment with access to the conda-forge channel, and the conda-build and python=3.9 packages.

   .. code-block:: console

      conda config --add channels conda-forge
      conda config --add channels ncar-vapor
      conda create -n myEnvironment python=3.9 conda-build
      conda activate myEnvironment

1) Within your conda environment, create a directory that will contain your installation.  Our team typically uses ~/channel.  Also create a subdirectory according to your operating system, shown below.

.. code-block:: console

    mkdir -p ~/channel/osx-64 (MacOS x86)
    mkdir -p ~/channel/osx-arm64 (MacOS ARM)
    mkdir -p ~/channel/linux-64 (Linux x86)

2) Move your created .tar.bz2 package from its build or download directory into your channel.

.. code-block:: console

    mv $CONDA_PREFIX/conda-bld/<OS>/vapor-3.6.0-ha5a8b8e_0.tar.bz2 ~/channel/osx-64
    or
    mv ~/Downloads/vapor-3.6.0-ha5a8b8e_0.tar.bz2 ~/channel/osx-64

3) Index your new local channel, so conda knows about it.

.. code-block:: console

    python -m conda_index path/to/my/channel

4) Install your .tar.bz2 package.  You must use a full file path to your channel.

.. code-block:: console

    conda install -c file:///path/to/my/channel vapor

The installation can be verified with the following commands in your console:

.. code-block:: console

    python
    import vapor

.. note:: Example python scripts and jupyter notebooks can be found in $CONDA_PREFIX/lib/python3.<version>/site-packages/vapor


Python Open Source Utilities
____________________________

Vapor Python supports a number of utility functions, found under apps/pythonapi/vapor/utils. If you write a function for your workflows that you believe would be useful to other users, we encourage you to add the function to Vapor utils.
