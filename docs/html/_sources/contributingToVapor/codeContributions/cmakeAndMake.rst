CMake and make
--------------

To build from source, create a directory where the build will take place.  For example:

    > cd ~/VAPOR
    > mkdir build
    > cd build

Windows
    Enter your build directory as the "Where to build the binaries" field in the CMake GUI.  Click *Configure*, *Generate*, and then *Open Project* in that order.  Visual Studio will open, and you can build the target *PACKAGE* to compile the source code.

UNIX:
    From your build directory, configure the software with cmake like so.  Additional arguments can be added with *-D<additional-argument>*.

    cmake ..

    Now compile with make

    make

.. note:: Some libraries have been optimized with the optional OpenMP API.  If you wish to compile with these optimizations, you'll need a compiler that supports OpenMP, as well as a few compiler flags which are documented :ref:`here <compilingWithOpenMP>`.

If compilation is successful, you can find Vapor's executable in the *bin* directory within your *build* directory.

Changing CMake Variables
========================

Some users may want their build to target a different library than what is distributed with Vapor's 3rd party library bundle.  Different libraries can be targetted in two ways, 1) through the *ccmake* tool, and 2) by editing the file located in <source-directory>/site_files/site.NCAR.

ccmake
======

Cmake provides an interface to set build variables called *ccmake*.  From your build directory, you can issue the ccmake command, followed by the path to Vapor's source code.  If your build directory is in <source_directory>/build, issuing ccmake from this directory would look like this:

    ccmake ..

.. figure:: /_images/ccmake.png
     :align: center
     :figclass: align-center

     ccmake's interface for changing build variables after issuing "*ccmake ..*" on Vapor's source directory.  This is assuming your build directory is in <vapor_source>/build.

The above interface allows you to set targets for some (but not all) of Vapor's libraries.  `More information on ccmake can be found here. <https://cmake.org/cmake/help/v3.0/manual/ccmake.1.html>`_  Your changes will be saved in your build directory in a file named CMakeLists.txt.  If this file gets deleted, your changes will be lost.  To set your libraries in a more permanent fashion, you can edit the site.NCAR file, described below.

A configuration to generate a release installer may look like this:

camke -DBUILD_TYPE=Release -DDIST_INSTALLER=ON .. && make

