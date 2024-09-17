Code Contributions
__________________

If you've found an issue you'd like to fix, you'll need to compile Vapor, fix the issue at hand, and submit your changes for review and approval.  Prerequisite software includes:

    * Git for Vapor's version control
      
    * CMake (version 3.20 or higher) for Vapor's build system
      
    * One of the following compilers, dependent on which operating system you're using:

        * OSX - LLVM 10.0.1 (clang-1001.0.46.4)
        * Ubuntu/CentOS - g++ 7.5.0 or higher
        * Windows - Microsoft Visual Studio 2015, version 14

Version control, Git, and GitHub
--------------------------------

To a new developer, working with Git is one of the more daunting aspects of contributing to *Vapor*.  It can very quickly become overwhelming, but sticking to the guidelines below will help keep the process straightforward and mostly trouble free.  As always, if you are having difficulties please feel free to `ask for help <https://vapor.discourse.group>`_.

Vapor's code is hosted on `GitHub <https://www.github.com/NCAR/vapor>`_. To contribute you will need to sign up for a `free GitHub account <https://github.com/signup/free>`_. We use `Git <http://git-scm.com/>`_ for version control to allow many people to work together on the project.  Git can also be acquired by package managers like apt-get (Ubuntu), yum (RedHat), and choco (Windows).

The `GitHub help pages <http://help.github.com/>`_ are a great place to get started with Git.

`GitHub also has instructions <http://help.github.com/set-up-git-redirect>`__ for installing git,
setting up your SSH key, and configuring Git.  All these steps need to be completed before
writing code for Vapor. 

.. _contributing.environment:

Forking Vapor's code
--------------------

After installing Git and registering with GitHub, it's time to "Fork" Vapor's code base by clicking the Fork button on the upper right corner of `Vapor's GitHub repository <https://github.com/NCAR/VAPOR>`_.  This creates your own repository on GitHub that contains a copy of Vapor's current main branch.  

.. figure:: ../_images/forkVapor.png
     :align: center
     :figclass: align-center
     :width: 60%

     Click the "Fork" button in the top-left corner of we website.

.. figure:: ../_images/newFork.png
     :align: center
     :figclass: align-center

     The newly created fork, based off Vapor's main branch.  Note the new repository name (sgpearse/VAPOR).  This is the repository you will clone from.

Clone your forked repository to a suitable location on your local work machine.  This new remote repository is what will be merged with Vapor's main branch once your changes have been made.

After completing your work, your changes can be submitted for review through a Pull Request from your Fork, into Vapor's main repository.  This is done under the Pull Requests tab in Vapor's github repository.  From this tab, create a new pull request that brings the changes from your forked repo into Vapor's main repo.  More details on this step are included in the :ref:`Submitting Your Changes <contributing.submitting>` section of this document.

For more information on the Forking Workflow, please see `Atlassian has a tutorial <https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow>`_ on basics and best practices.

.. figure:: ../_images/mergeFork.png
     :align: center
     :figclass: align-center

     Submitting a pull request to Vapor's main branch.

Third-Party Libraries
---------------------

Download pre-built Third-Party Libraries (Recommended)
******************************************************

This is the recommended approach for acquiring the third-party libraries that Vapor depends on.  If you require additional libraries, or custom settings to the libraries currently used by vapor, see the :ref:`Building Third-Party Libraries section <contributing.build3rdParty>`.

After forking your new Vapor repository and cloning from it, you can download pre-built third-party libraries from the links below.  Be sure to select the correct libraries for the operating system you're building on.

    :ref:`Download third party libraries here <Third Party Libraries>`

*Windows*

Unzip the third-party libraries for Windows into the root of your C:\\ directory.

*Linux and OSX*

If building on Linux or OSX, the third party libraries must be placed in /usr/local/VAPOR-Deps/.  Then create a symbolic link from the extracted contents to a directory named *current*.

.. code-block:: console

   $ ln -s /usr/local/VAPOR-Deps/2023-Jun /usr/local/VAPOR-Deps/current

.. note:: On MacOS, a "quarantine" flag will be added to the binaries and libraries you build from source.  This will prevent them from being run.  To remove the flag, run *sudo xattr -dr com.apple.quarantine /usr/local/VAPOR-Deps/current/* after building the libraries.

.. _contributing.build3rdParty:

Building Third-Party Libraries (Not recommended)
************************************************

This is an alternative to downloading our pre-built libraries that allows you to configure and store them wherever you want.  This is a more complex exercise.  If you choose to do this, you must also configure Vapor's CMake configuration to point to your custom directory.  

If you wish to go down this route, you may follow the build instructions for `Windows <https://drive.google.com/a/ucar.edu/file/d/1nPZyNtH516D00Te2AwttRrPDTi0bDIbl/view?usp=sharing>`_ and `UNIX <https://docs.google.com/document/d/1XNBmoUvxGn9I0fy9xvB1m5PQyOI32TtdyMbwfOve0QQ/edit?usp=sharing>`_.

The source code for these libraries may be downloaded `here <https://drive.google.com/open?id=1FG8ngmz9Tk3HKZgGejqwtbkBAVonm91z>`_.

.. note:: The file <vapor-source>/site_files/site.NCAR may be used to specifiy the location of the libraries.  To do this, build your version of the libraries in /usr/local/VAPOR-Deps/current, or change the THIRD_PARTY_LIB_DIR path in site.NCAR.

+--------------+---------+---------+
| Vapor        | 3.9.0   | 3.8.0   |
+==============+=========+=========+
| assimp       | 5.2.5   | 4.1.0   |
+--------------+---------+---------+
| expat        | 2.5.0   |         |
+--------------+---------+---------+
| freetype     | 2.13.0  | 2.10.1  |
+--------------+---------+---------+
| glew         | N/A     | 2.1.0   |
+--------------+---------+---------+
| glm          | 0.9.9.8 | 0.9.9.8 |
+--------------+---------+---------+
| hdf5         | 1.14.0  | 1.12.2  |
+--------------+---------+---------+
| hdf5 plugins | N/A     | 1.12.2  |
+--------------+---------+---------+
| jpeg         | 9e      | 9c      |
+--------------+---------+---------+
| libgeotiff   | 1.7.1   | 1.7.1   |
+--------------+---------+---------+
| netCDF       | 4.9.1   | 4.8.1   |
+--------------+---------+---------+
| Ospray       | 2.11.0  | 2.10.0  |
+--------------+---------+---------+
| proj         | 7.2.1   | 6.1.1   |
+--------------+---------+---------+
| python       | 3.9.16  | 3.6.9   |
+--------------+---------+---------+
| Qt           | 5.15.2  | 5.13.2  |
+--------------+---------+---------+
| tiff         | 4.5.0   | 4.0.10  |
+--------------+---------+---------+
| udunits      | 2.2.28  | 2.2.26  |
+--------------+---------+---------+
| xcb-proto    | 1.15.2  |         |
+--------------+---------+---------+
| libxcb       | 1.15.0  |         |
+--------------+---------+---------+


Install System Libraries
------------------------

Building Vapor from source requires system libraries that are not natively available on all UNIX platforms.  The following commands can be used to acquire these libraries.

Ubuntu:
    sudo apt-get install git freeglut3-dev libexpat1-dev libglib2.0-0 libdbus1-3

CentOS:
    sudo yum install dbus make freeglut-devel expat-devel libquadmath-devel libXrender-devel libSM-devel fontconfig-devel

.. note::
    Vapor uses docker images as a basis for its continuous integration test suite, which are built from Dockerfiles located in <source-directory>/share/docker.  The docker files in this directory can be used as a reference to how our different test systems build Vapor.

Building Vapor from source 
--------------------------

On all operating systems, create a directory where the build will take place.  One option is to put the build directory inside of the Vapor source code directory.

    > cd VAPOR
    > mkdir build
    > cd build

Windows
    Enter your build directory as the "Where to build the binaries" field in the CMake GUI.  Click *Configure*, *Generate*, and then *Open Project* in that order.  Visual Studio will open, and you can build the target *PACKAGE* to compile the source code.

UNIX:
    Navigate to your build directory and run the command *cmake <source_directory>*, where <source_directory> is the root directory of Vapor's source code.  If the configuration was successful, you can then run *make* to compile Vapor.

    cmake .. && make

.. note:: Some libraries have been optimized with the optional OpenMP API.  If you wish to compile with these optimizations, you'll need a compiler that supports OpenMP, as well as a few compiler flags which are documented :ref:`here <compilingWithOpenMP>`.

If compilation is successful, you can find Vapor's executable in the *bin* directory within your *build* directory.

Changing CMake Variables
========================

Some users may want their build to target a different library than what is distributed with Vapor's 3rd party library bundle.  Different libraries can be targetted in two ways, 1) through the *ccmake* tool, and 2) by editing the file located in <source-directory>/site_files/site.NCAR.

ccmake
======

Cmake provides an interface to set build variables called *ccmake*.  From your build directory, you can issue the ccmake command, followed by the path to Vapor's source code.  If your build directory is in <source_directory>/build, issuing ccmake from this directory would look like this:

    ccmake ..

.. figure:: ../_images/ccmake.png
     :align: center
     :figclass: align-center

     ccmake's interface for changing build variables after issuing "*ccmake ..*" on Vapor's source directory.  This is assuming your build directory is in <vapor_source>/build.

The above interface allows you to set targets for some (but not all) of Vapor's libraries.  `More information on ccmake can be found here. <https://cmake.org/cmake/help/v3.0/manual/ccmake.1.html>`_  Your changes will be saved in your build directory in a file named CMakeLists.txt.  If this file gets deleted, your changes will be lost.  To set your libraries in a more permanent fashion, you can edit the site.NCAR file, described below.

site.NCAR
=========

The site.NCAR file is what is used by the Vapor team to define what third party libraries a build should link to.  This file is located at <vapor_source>/site_files/site.NCAR, and contains conditionals for buildong on Darwin (OSX), Windows, and Linux (Ubuntu/CentOS).  There are also conditionals for building on NCAR's visualization cluster, Casper.

The THIRD_PARTY_DIR variable in this file may be overloaded to re-target the location of Vapor's libraries.  Special values exist for the Qt and Python libraries becasuse they are built outside of the THIRD_PARTY_DIR, and must be manually overridden.  These variables are:

+---------------------+-----------------------------------------------------------------+
| QTDIR               | Directory where the Qt library has been built/installed         |
+---------------------+-----------------------------------------------------------------+
| Qt5Core_DIR         | Directory where the Qt5Core shared library was built/installed  |
+---------------------+-----------------------------------------------------------------+
| QT_QMAKE_EXECUTABLE | Location of Qt's QMake executable                               |
+---------------------+-----------------------------------------------------------------+
| PYTHONDIR           | Directory containing Python's libraries and headers             |
+---------------------+-----------------------------------------------------------------+
| PYTHONPATH          | Directory containing Python's site packages                     |
+---------------------+-----------------------------------------------------------------+
| PYTHONVERSION       | Version of Python                                               |
+---------------------+-----------------------------------------------------------------+
| NUMPY_INCLUDE_DIR   | Directory containing numpy's header files                       |
+---------------------+-----------------------------------------------------------------+
| OSPRAYDIR           | Directory containing Ospray's librarieses                       |
+---------------------+-----------------------------------------------------------------+

Adding to the Code Base
-----------------------

After successfully compiling Vapor, you can make changes to the code base.  Make sure to follow Vapor's `Code Conventions <https://github.com/NCAR/VAPOR/wiki/Vapor-Coding-Convention>`_.  If building on a UNIX system, eliminate all compiler warnings.

.. What pieces of code you add or modify will depend on the issue you're trying to fix.  Most often, contributors will be doing one of two things:

.. .. toctree::
..    :maxdepth: 1

..    createDataReader
..    createRenderer

Build and Test an Installer
---------------------------

Before submitting your changes for review, it's worth the time to build an installer to see if libraries are properly linked, and optimized code works correctly.

To build an installer, run *ccmake <vapor-source-dir>* so that the field *CMAKE_BUILD_TYPE Debug* is changed to *CMAKE_BUILD_TYPE Release*.  Also change the field *DIST_INSTALLER OFF* to be *DIST_INSTALLER ON*.  Alternatively to ccmake, you can hand-edit the file CMakeLists.txt, which is located in the root of Vapor's source directory.

On Windows, make sure that the Visual Studio setting for the build is in *Release* mode, not *Debug*, and build the target *PACKAGE*.

On OSX, run *cmake <vapor-source-dir> && make && make installer* from your build directory.

On Linux, run  *cmake <vapor-source-dir> && make linuxpreinstall && make installer* from your build directory.

.. _contributing.submitting:

Submitting Your Changes
-----------------------

After your implementation is complete, push your commits to your forked repository on GitHub.  Then issue a pull request to Vapor's main branch.

Manual Review:
    If these tests pass, Vapor's team will review the Pull Request to make sure that Vapor's `Code Conventions <https://github.com/NCAR/VAPOR/wiki/Vapor-Coding-Convention>`_ were honored, and that the logic and structure of the code is sound.  

After review, further changes may be requested.  If everything looks good, the Pull Request will be merged into Vapor's main repository.


`Vapor Coding Conventions <https://github.com/NCAR/VAPOR/wiki/Vapor-Coding-Convention>`_
----------------------------------------------------------------------------------------


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
----------------------------

Vapor Python supports a number of utility functions, found under apps/pythonapi/vapor/utils. If you write a function for your workflows that you believe would be useful to other users, we encourage you to add the function to Vapor utils.
