Submitting Changes
------------------

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

Pull Request
------------

After your implementation is complete, push your commits to your forked repository on GitHub.  Then issue a pull request to Vapor's main branch.

Manual Review:
    If these tests pass, Vapor's team will review the Pull Request to make sure that Vapor's `Code Conventions <https://github.com/NCAR/VAPOR/wiki/Vapor-Coding-Convention>`_ were honored, and that the logic and structure of the code is sound.

After review, further changes may be requested.  If everything looks good, the Pull Request will be merged into Vapor's main repository.


`Vapor Coding Conventions <https://github.com/NCAR/VAPOR/wiki/Vapor-Coding-Convention>`_
