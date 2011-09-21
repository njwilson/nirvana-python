User Guide
==========

Supported Pythons and Platforms
-------------------------------

Python 2.6 and 2.7 are currently supported. There are no plans to support
2.5, but 3.x is `coming "soon"
<https://github.com/njwilson/nirvana-python/issues/1>`_.

I develop and test this library on Mac and Linux. I'd like to be friendly
to other platforms (e.g., Windows) as well, but it may be a while before I
get around to setting up a development environment under Windows to test
it.

Library Structure
-----------------

The Nirvana library is split into two parts:

#. The low-level interface is a thin Python layer on top of NirvanaHQ's API.
   It allows your Python programs to make calls directly with the API.
   Using the library at this level requires knowledge of the API that can
   be obtained from their API documentation.

#. The high-level interface builds on top of the low-level interface to
   provide nice, object-oriented, *pythonic* access to a user's tasks and
   related data. This is the way most developers will use this library.
   The documentation on this site should be sufficient for Using the
   library at this level. NirvanaHQ's API documentation should not be
   required.

Getting Started
---------------

Ready to start developing your Nirvana app? Let's go!

Table of contents:

.. toctree::
   installation
   api/index
