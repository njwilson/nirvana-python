======================
Nirvana Python Library
======================

.. warning:: This project is still in the early planning/development
    phase. I'm starting with some Documentation Driven Development (DDD)
    where I write documentation before code to help ensure a good, usable
    interface design. I was going to link to Wikipedia's article on DDD
    but apparently they don't have one. Hmm... I swear I'm not crazy.
    Well, anyways, there's a good chance that nothing you see here
    actually exists yet. If it does, it probably doesn't work.

.. warning:: The NirvanaHQ API hasn't been released yet. I don't have any
   insider information about how the API will work other than what can be
   observed from the web app (which uses the API and is subject to change
   without notice). I'm delaying work on the lower-level part of this
   library that communicates with the API and am instead focusing on the
   higher-level interface for developer's using this library.

This is a Python library that provides access to the web-based task
management software from `NirvanaHQ <http://nirvanahq.com>`_, which is
based on David Allen's popular `Getting Things Done (GTD)
<http://www.davidco.com/about-gtd>`_  methodology.

.. note:: Other than being huge fans, the developers of this library are
   not affiliated with NirvanaHQ in any way, and either is this library.

Overview
========

The goal of this library is to provide full access to NirvanaHQ's API for
use in Python programs. Let's start by showing you some of the things this
library can do.

Authenticating with the API and accessing the user's data is simple::

    >>> import nirvana
    >>> auth = nirvana.auth.BasicAuth('username', 'password')
    >>> nirv = nirvana.Nirvana(auth)

Let's print a welcome message to the user::

    >>> print("Welcome, {0}!".format(nirv.user.first_name))
    Welcome, Nick!

Next actions are easily accessible::

    >>> for task in nirv.tasks.next():
    ...     print(task.name)
    Task 1
    Task 2

To create a new task::

    >>> from nirvana.models import Task
    >>> nirv.tasks.create('Task 3', state=Task.NEXT)
    <Task: Task 3>

When you're done, synchronize the changes back to NirvanaHQ::

    >>> nirv.sync()

Keep reading for more details on how you can use this library to access
the rest of the features provided by NirvanaHQ's API.

Installation
============

The easiest way to install the Nirvana library is with `pip
<http://www.pip-installer.org/>`_::

    $ pip install nirvana

See the :doc:`installation<user/installation>` section of the :doc:`user
guide<user/index>` for more information and other installation options.

User Guide
==========

See the :doc:`user guide<user/index>` for more details on using the
Nirvana library in your own Python application.

Sitemap
=======

.. toctree::

   self
   user/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
