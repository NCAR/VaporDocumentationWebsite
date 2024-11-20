Third-Party Libraries
---------------------

.. include:: <Third Party Libraries>

:ref:`Download third party libraries here <Third Party Libraries>`

Windows:
    Unzip the third-party libraries for Windows into the root of your C:\\ directory.

Linux and MacOS:
    The third party libraries must be placed in /usr/local/VAPOR-Deps/ along with a symbolic link named "current" that points to them.

.. code-block:: console

    $ ln -s /usr/local/VAPOR-Deps/2023-Jun /usr/local/VAPOR-Deps/current

MacOS:
    A "quarantine" flag will be added to the binaries and libraries you build from source.  This will prevent them from being run.  To remove the flag, run:

.. code-block:: console

    $ sudo xattr -dr com.apple.quarantine /usr/local/VAPOR-Deps/current/* after building the libraries.

.. _contributing.build3rdParty:

Building Third-Party Libraries
______________________________

:ref:`Download source files here <Third Party Libraries>`.

See ~/VAPOR/scripts/build3rdParty.sh to compile the libraries and see specifics on how they are configured for maxOSx86, appleSilicon, and Ubuntu.

.. code-block:: console

    ~/VAPOR/scripts/build3rdParty.sh -o macOSx86
    ~/VAPOR/scripts/build3rdParty.sh -o appleSilicon
    ~/VAPOR/scripts/build3rdParty.sh -o Ubuntu

Build instructions for `Windows can be found here <https://drive.google.com/a/ucar.edu/file/d/1nPZyNtH516D00Te2AwttRrPDTi0bDIbl/view?usp=sharing>`_.

.. note:: The file <vapor-source>/site_files/site.NCAR may be used to specifiy the location of the libraries.  To do this, build your version of the libraries in /usr/local/VAPOR-Deps/current, or change the THIRD_PARTY_LIB_DIR path in site.NCAR.

+--------------+---------+
| Vapor        | 3.9.3   |
+==============+=========+
| assimp       | 5.2.5   |
+--------------+---------+
| expat        | 2.5.0   |
+--------------+---------+
| freetype     | 2.13.0  |
+--------------+---------+
| glew         | N/A     |
+--------------+---------+
| glm          | 0.9.9.8 |
+--------------+---------+
| hdf5         | 1.12.2  |
+--------------+---------+
| hdf5 plugins | 1.12.2  |
+--------------+---------+
| jpeg         | 9e      |
+--------------+---------+
| libgeotiff   | 1.7.1   |
+--------------+---------+
| netCDF       | 4.9.1   |
+--------------+---------+
| Ospray       | 2.11.0  |
+--------------+---------+
| proj         | 7.2.1   |
+--------------+---------+
| python       | 3.9.16  |
+--------------+---------+
| Qt           | 5.15.8  |
+--------------+---------+
| tiff         | 4.5.0   |
+--------------+---------+
| udunits      | 2.2.28  |
+--------------+---------+
| xcb-proto    | 1.15.2  |
+--------------+---------+
| libxcb       | 1.15.0  |
+--------------+---------+


Install System Libraries
------------------------

Building Vapor from source requires system libraries that are not natively available on all UNIX platforms.  The following commands can be used to acquire these libraries.

Ubuntu:
    sudo apt-get install git freeglut3-dev libexpat1-dev libglib2.0-0 libdbus1-3
