Acquire VAPOR
-------------

Any questions can be answered `on our forum <https://vapor.discourse.group>`_.

Vapor's code is hosted on `GitHub <https://www.github.com/NCAR/vapor>`_. To contribute you will need to sign up for a `free GitHub account <https://github.com/signup/free>`_. We use `Git <http://git-scm.com/>`_ for version control to allow many people to work together on the project.  Git can also be acquired by package managers like apt-get (Ubuntu), yum (RedHat), and choco (Windows).

`Follow these instructions <http://help.github.com/set-up-git-redirect>`__ for installing and configuring git, and
setting up your SSH key.

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

After completing your work, your changes can be submitted for review through a Pull Request from your Fork into Vapor's main repository.  This is done under the Pull Requests tab in Vapor's github repository.  From this tab, create a new pull request that brings the changes from your forked repo into Vapor's main repo.  More details on this step are included in the :ref:`Submitting Your Changes <contributing.submitting>` section of this document.

For more information on the Forking Workflow, please see `Atlassian has a tutorial <https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow>`_ on basics and best practices.

.. figure:: ../_images/mergeFork.png
     :align: center
     :figclass: align-center

     Submitting a pull request to Vapor's main branch.
