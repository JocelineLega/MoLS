Packaging and Deploying MoLS

1. Prerequisites for Deployment 

A. If MATLAB Runtime version 9.1 (R2016b) has not been installed, install it in one of 
   these ways:

i. Run the package installer, which will also install the MATLAB Runtime.
NOTE: You will need administrator rights to run the installer. 

ii. Download the Windows 64-bit version of the MATLAB Runtime for R2016b from:

    http://www.mathworks.com/products/compiler/mcr/index.html
   
iii. Run the MATLAB Runtime installer provided with MATLAB.

B. Verify that a Windows 64-bit version of Python 2.7, 3.3, and/or 3.4 is installed.

2. Installing the MoLS Package

A. Go to the directory that contains the file setup.py and the subdirectory MoLS. If you 
   do not have write permissions, copy all its contents to a temporary location and go 
   there.

B. Execute the command:

    python setup.py install [options]
    
If you have full administrator privileges, and install to the default location, you do 
   not need to specify any options. Otherwise, use --user to install to your home folder, 
   or --prefix="installdir" to install to "installdir". In the latter case, add 
   "installdir" to the PYTHONPATH environment variable. For details, refer to:

    https://docs.python.org/2/install/index.html


3. Using the MoLS Package

The MoLS package is on your Python path. To import it into a Python script or session, 
   execute:

    import MoLS

If a namespace must be specified for the package, modify the import statement accordingly.
