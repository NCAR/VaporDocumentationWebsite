Codesigning MacOS
-----------------

To codesign a MacOS .dmg installer, follow these steps:

1) Acquire VAPOR's *Developer ID Application* certificate from our administrators and register it on your keychain
2) Generate a personal app-specific password and register it on your keychain*
3) Install your .dmg in the /Applications directory
4) Run the bash script buildutils/codesignMacOS.sh

.. note:: Read more about app-specific passwords here: https://support.apple.com/en-us/102654

A codesigned .dmg installer will now have been generated in the /Applications directory.  If the code signature reports back from the Apple notarytool as invalid, it can be debugged by applying the submission's hash as follows:

.. code-block:: console

     xcrun notarytool log --keychain-profile "<my app-specific password name>" <hash>
