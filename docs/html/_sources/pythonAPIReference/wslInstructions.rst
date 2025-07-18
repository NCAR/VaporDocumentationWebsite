Windows Instructions
--------------------

*Vapor-python is currently not supported for Windows machines. This guide provides a temporary workaround*

To run VAPOR Python on Windows distributions, we recommend installing the Windows Subsystem for Linux (`WSL <https://docs.microsoft.com/en-us/windows/wsl/install>`_). This will allow you to run your workflows in a Linux-based environment on your Windows machine. To get started, follow these steps:

1. Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator".
2. Enter the following command to install WSL:

   .. code-block:: console

       wsl --install

3. After the installation finishes, restart your machine for these changes to take effect.
4. Next, press the Windows key, search for "Ubuntu," and run the Ubuntu app. Follow the setup instructions it provides.
5. After Ubuntu setup, install Conda by running the two commands below. (To paste into your Ubuntu environment, right click anywhere in the terminal)

   .. code-block:: console

       wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
       bash Miniconda3-latest-Linux-x86_64.sh

6. Follow the instructions it provides, and make sure to say "yes" when it asks if you want to update your shell profile to automatically initialize conda. Close and reopen Ubuntu for these changes to take effect.
7. Install VAPOR Python using conda:

   .. code-block:: console

       conda create -n vapor_python
       conda activate vapor_python
       conda install -c conda-forge -c ncar-vapor vapor

8. After vapor installation is complete, you can open a coding environment of your choice:

   **Jupyter Lab:** With Jupyter Lab, first run a command to let Jupyter see your new vapor environment. Then launch Jupyter Lab and copy and paste one of the provided links into your browser.

   .. code-block:: console

       python -m ipykernel install --user --name vapor-python --display-name "Vapor Python"
       jupyter lab

   **VS-Code:** Alternatively, you can install `Visual Studio Code <https://code.visualstudio.com/Download>`_ along with its `WSL extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_. Then, restart Ubuntu and run:

   .. code-block:: console

       code .


Note: VS code extensions that you have installed on your Windows machine will not be automatically installed in your WSL environment. Before running a Jupyter notebook in WSL, make sure you install the Jupyter extension.