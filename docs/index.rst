.. pai documentation master file, created by
   sphinx-quickstart on Mon Dec 24 01:47:53 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _pai_index:

.. raw:: html

    <style> .red {color:red} </style>
    <style> .blue {color:blue} </style>
    <style> .green {color:green} </style>

pai v0.0.1 documentation
========================

What is pai?
------------

pai helps with code

pai knows what code is, from a programmer's POV: algorithms to control flows of data to / from connections.

Structure
---------

Code is expressed in a language, such as `Python <https://github.com/jalanb/pym/blob/master/pym/ast/parse.py#L9>`_ or `Bash <https://github.com/jalanb/parsher/blob/master/parsher/__init__.py#L32>`_, `etc <https://pypi.python.org/pypi/grako/3.6.6#abstract-syntax-trees-asts>`_, so can be parsed to a `Structured Tree <https://github.com/jalanb/pym/blob/master/pym/ast/nst.py#L88>`_, and annotated with interesting structural and dynamic properties.

pai treats parsing and rendering as separate operations, but ideally they should be a single, reversible process. They are pai's "back end" connecting stored plain text to structured text which `can be editted <https://github.com/jalanb/pym/blob/master/pym/edit/main.py#L41>`_, and tested, committed, traced, logged, debugged, `... <https://github.com/jalanb/pym/blob/master/pym/edit/main.py#L41>`_. Editting is handled by `pym <https://pym.readthedocs.io/en/latest/#editing>`_.

Programs
--------

A program is a history of a flow of ideas into a structured text representing a working algorithm.

Those ideas are *intentions* - what the coder thinks will happen at run time.

Usage
-----

    $ pai <program> <method>


You are shown the code of that method.

You can move around the structure, flows and call stack with keyboard.

You can edit the structure of the method (which changes the availability of run-time data).

Colours
-------

Red is bad, green is good, blue is links, white has never been run.

Indices and tables
==================

Parts of the documentation:

.. toctree::
   :maxdepth: 2

   parsing
   renderers
   miscellaneous

* :ref:`genindex`
* :ref:`search`

