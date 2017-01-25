============
 desistar
============

Introduction
============

This repository is intended for hosting the software products for the analysis
of spectra for the DESI Milky Way Survey (MWS).

.. _DESI: https://desi.lbl.gov


Product Name
============

desistar

Creating a New Product From Scratch
===================================

This product was initilly created from the desitemplate package.


Installing a Product
====================

DESI_ Python packages should be installable by pip_.  For example::

    pip install git+https://github.com/desihub/desitemplate.git@1.1.0

In this example the string ``@1.1.0`` means "install tag 1.1.0".  You can
also use this method to install branches (by branch name) or specific commits
(using the git hash).

At NERSC_, DESI_ products should be installed with desiInstall.  The main purpose
of desiInstall is to ensure that different versions of a package are kept
separate and to install `Module files`_.  desiInstall is not part of this package,
but part of desiutil_.

.. _pip: http://pip.readthedocs.org
.. _NERSC: http://www.nersc.gov
.. _desiutil: https://github.com/desihub/desiutil
.. _`Module files`: http://modules.sourceforge.net

Product Contents
================

Directory Structure
-------------------

A DESI **Python** product may contain these top-level directories.  It may contain
additional directories, but the directories listed here have special
meaning for desiInstall.

bin/
    This directory is only needed if the product contains executable scripts.
    If you do not have any scripts, you can omit this directory from your
    product.
doc/
    Contains high-level documentation of the software.  Typically, the code
    itself will contain its own documentation.  This area is for
    documentation that discusses the product as a whole.  Sphinx_
    will process files placed in this directory.
    Sphinx_ documents should be .rst files.
etc/
    Contains small data and configuration files used by the code.  This does not
    mean you should be checking in large data files!  This directory also
    contains the template module file for the product.  If additional files
    are found in this directory, desiInstall will install them automatically.
    However, you should not rely on pip installing these files for you.
py/
    Contains Python code.  Top-level Python package directories should be
    placed *within* the ``py/`` directory.  This simplifies the specification
    of the ``$PYTHONPATH`` variable.

For a standard DESI_ Python package, you will probably need all of these
directories, with the possible exception of the bin directory.

.. _Sphinx: http://sphinx-doc.org

Top-level Files
---------------

README.rst Files
~~~~~~~~~~~~~~~~

Of course your product should have a README(.rst) file!  The preferred name and
format is ``README.rst``.  If your product lives on GitHub, it will automatically
be rendered!

If your product is in svn, be sure that the svn:mime-type property is set::

    svn propset svn:mime-type text/x-rst README.rst

This will allow Trac to render your README.rst file in HTML.  In fact, you should
set this mime-type for any and all .rst files that you have (in svn).

setup.py
~~~~~~~~

Your Python product should have a setup.py file.  See
the setup.py file included with this template product for further details.
This will allow the package to be installed with pip.
In addition, desiInstall will process this file with::

    python setup.py install --prefix=$INSTALL_DIR.

**If your product contains a setup.py file, desiInstall will assume that your
product is Python-based and will process it accordingly.**

LICENSE Files
~~~~~~~~~~~~~

The 3-clause BSD-style license is the standard adopted by DESI and used for
this package.

Automation Support Files
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the standard ``.gitignore`` file, there are two other
hidden files included in this product.

.coveragerc
    Configuration for the test coverage.  You will need to edit this file
    to change the name of the product.

.travis.yml
    This is the configuration file for `Travis CI`_ tests.  This file might
    need to be adjusted to suit your package.  In particular, the file
    included with this package has Python 3 tests that your package might not
    be ready for yet.  Just comment those out.

.. _`Travis CI`: http://travis-ci.org

Requirements File
~~~~~~~~~~~~~~~~~

The requirements.txt file contains other Python packages required by this
package.  In particular, this file will be processed during Travis tests to
install packages needed for the tests.  This file is processed with the
command::

    pip install -r requirements.txt

Manifest File
~~~~~~~~~~~~~

The ``MANIFEST.in`` file contains instructions for the setup system that will
be used to construct an "official" tarball of the package.  For example,
this file will be used by the command::

    python setup.py sdist

This file is absolutely necessary if your package will be distributed via
PyPI_.

.. _PyPI: http://pypi.python.org

Other Files
-----------

.module file
~~~~~~~~~~~~

In the etc/ directory is a file called ``desistar.module``.  This file is used to
create a module file for the product at install time.  This file allows
customization and dependencies should be added here.

Module files are intended for use at NERSC_.  They are not processed
automatically by pip.

Version File
~~~~~~~~~~~~

In the top-level of the py/desistar directory, you will see a file called
``_version.py``.  This file is created and maintained by the command::

    python setup.py version

This file should not be altered except by that command.  In preparation for a
new tag of the product, you can use the variant::

    python setup.py version --tag 1.2.3

To set the version string to exactly '1.2.3'.  Make sure you check in your
changes and immediately tag after doing this!

Links to Automation
===================

DESI_ uses several online resources to test software and build documentation.
This section contains example links to those services.

Full Documentation
------------------

Please visit `desistar on Read the Docs`_

.. image:: https://readthedocs.org/projects/desistar/badge/?version=latest
    :target: http://desistar.readthedocs.org/en/latest/
    :alt: Documentation Status

.. _`desistar on Read the Docs`: http://desistar.readthedocs.org/en/latest/

Travis Build Status
-------------------

.. image:: https://img.shields.io/travis/desihub/desistar.svg
    :target: https://travis-ci.org/desihub/desistar
    :alt: Travis Build Status


Test Coverage Status
--------------------

.. image:: https://coveralls.io/repos/desihub/desistar/badge.svg?service=github
    :target: https://coveralls.io/github/desihub/desistar
    :alt: Test Coverage Status

License
=======

desistar is free software licensed under a 3-clause BSD-style license. For details see
the ``LICENSE.rst`` file.
