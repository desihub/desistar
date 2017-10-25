============
gettemplate
============

Introduction
============

Script to interpolate stellar templates in a set of model libraries.
The code prepares input files, calls, and reads the output from 
FERRE (githum.com/callendeprieto/ferre), which does the actual interpolation.

The input libraries must be in FERRE format. Examples used in DESI are
available at
ftp://carlos:allende@ftp.ll.iac.es/bossgrids/nscgrids3


Product Name
============

gettemplate


Top-level Files
---------------
gettemplate.py -- python script

LICENSE Files
~~~~~~~~~~~~~

The 3-clause BSD-style license is the standard adopted by DESI and used for
this package.

Requirements File
~~~~~~~~~~~~~~~~~

The requirements.txt file contains other Python packages required by this
package.  In particular, this file will be processed during Travis tests to
install packages needed for the tests.  This file is processed with the
command::

    pip install -r requirements.txt

License
=======

desistar, and therefore gettemplate, is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
