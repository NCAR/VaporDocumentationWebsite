Building VAPOR with SPACK
=========================
In some cases it may be desirable to host a build of VAPOR that is compiled with `SPACK <https://spack.io/>`_.  This can be done with the following set of commands, assuming you are using bash.

.. code-block:: console

    git clone -c feature.manyFiles=true https://github.com/spack/spack.git
    cd spack
    source share/spack/setup-env.sh
    export SPACK_DISABLE_LOCAL_CONFIG=true
    spack compiler find
    spack install -j 4 vapor ^hdf5~mpi
