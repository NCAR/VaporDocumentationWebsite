Running VAPOR on Casper
=======================
In this tutorial, we will walk through the process of launching VAPOR on NCAR's Casper supercomputer. This involves setting up a remote desktop on Casper and connecting to it using a VNC Client.

Prerequisites
-------------
* **Access to Casper** - To access Casper, you will need a `user account <https://arc.ucar.edu/knowledge_base/74317885>`_ along with your project code.

* **VNC Client** - You will also need to install a VNC client on your local machine. CISL recommends the `TigerVNC <https://tigervnc.org/>`_ client, and provides this video to help users install it: `Installing TigerVNC on a Mac laptop <https://www.youtube.com/watch?v=hVFN4AXLbWQ>`_.

Connecting to a Remote Desktop
------------------------------
1. Start a VNC session on Casper by running the following command in a terminal on your local machine. Replace ``YOUR_USERNAME`` with your Casper login and ``PROJECT_CODE`` with the code associated with your project.

.. code-block:: console

    ssh -t -l YOUR_USERNAME casper.ucar.edu /glade/u/apps/opt/vncmgr/bin/vncmgr create VAPOR -A PROJECT_CODE -t 4:00:00 --gl-desktop

.. note::

    * The ``--gl-desktop`` flag allows the server to use GPU resources, which is important for running VAPOR.
    * The ``-t 4:00:00`` flag specifies the time the server will run for in HH:MM:SS format. The default is 4 hours and the maximum is 24 hours.
    * For additional options, you can run ``vncmgr --help`` when signed into Casper.


2. After following the prompts to log in, you should get a message that looks like this:

.. figure:: ../_images/SSH_tunnel_instructions.png
    :align: center
    :figclass: align-center

3. Run the ssh command provided in this message. In the screenshot above, this command is boxed in red. You should see something similar with your login information. After running this command, it will prompt you to log in again. Then, you should get the following message:

.. figure:: ../_images/VNC_instructions.png
    :align: center
    :figclass: align-center

This message will provide you with the localhost information and the one-time password needed to connect to the desktop with your VNC client. Next, use your VNC client to connect to your remote desktop:

4. Open your VNC client
5. Enter the localhost information and click connect

.. figure:: ../_images/VNC_server.png
    :align: center
    :figclass: align-center
    :width: 50%

6. Enter the one-time password

.. figure:: ../_images/one_time_password.png
    :align: center
    :figclass: align-center
    :width: 50%

Running VAPOR on your Remote Desktop
------------------------------------

Once you've connected to your remote desktop, follow these steps to run VAPOR:

1. Before launching VAPOR for the first time, it is recommended to change the desktop's settings for clicking files and folders. This will make it easier to open multi-file datasets. Navigate to "System Settings", then under "Clicking files or folders" select "Selects them" and click "Apply". Capser will save your preferences between sessions, so this only needs to be done once.

.. figure:: ../_images/casperSettings.png
    :align: center
    :figclass: align-center
    :width: 80%

2. To run VAPOR, open Konsole from the task bar at the bottom and run the following commands:

.. code-block:: console

    module load vapor
    vglrun vapor

Ending your Session
-------------------
Your remote desktop will use compute resources until either the amount of time you specified has elapsed or until you manually end it. To end your session manually, follow these steps:

1. Sign into Casper and run the ``vncmgr`` command. You will be able to see your active servers that are currently running
2. Type ``kill VAPOR`` to end the session named VAPOR
3. Wait for the session to end