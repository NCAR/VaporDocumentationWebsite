Prerequisite Software
---------------------

If you've found an issue you'd like to fix, you'll need to compile Vapor, fix the issue at hand, and submit your chang
es for review and approval.  Prerequisite software for all platforms includes:
    
    * Git
      
    * CMake (version 3.20 or higher)

One of the following compilers will be necessary:

+-------------------+---------------------------------------------------------+
| Operating System  | Compiler                                                |
+===================+=========================================================+
| MacOS             | `Custom OMP version of clang                            |
|                   | <https://vaporawsbucket.s3.us-west-2.amazonaws.com/     |
|                   | portClang.tar.xz>`_                                     |
+-------------------+---------------------------------------------------------+
| Ubuntu/CentOS     | g++ 7.5.0 or higher                                     |
+-------------------+---------------------------------------------------------+
| Windows           | Microsoft Visual Studio 2015, version 14                |
+-------------------+---------------------------------------------------------+

Finally, consult VAPOR's CI build system for necessary system libraries on `MacOS <https://github.com/NCAR/VAPOR/blob/12dc436b76a503150f51676088014170de2180fe/.circleci/config.yml#L128>`_, `Windows <https://github.com/NCAR/VAPOR/blob/12dc436b76a503150f51676088014170de2180fe/.circleci/config.yml#L149>`_, and `Linux <https://github.com/NCAR/VAPOR/blob/12dc436b76a503150f51676088014170de2180fe/.circleci/config.yml#L356>`_.
