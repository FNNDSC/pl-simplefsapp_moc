pl-simplefsapp_moc
================================

.. image:: https://badge.fury.io/py/simplefsapp_moc.svg
    :target: https://badge.fury.io/py/simplefsapp_moc

.. image:: https://travis-ci.org/FNNDSC/simplefsapp_moc.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/simplefsapp_moc

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-simplefsapp_moc

.. contents:: Table of Contents


Abstract
--------

A demo/testing simplefsapp for the MOC compute environment.


Synopsis
--------

.. code:: bash

    python simplefsapp_moc.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a 

.. code:: bash

    pip install simplefsapp_moc

and run with

.. code:: bash

    simplefsapp_moc.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    simplefsapp_moc.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing                             \
            fnndsc/pl-simplefsapp_moc simplefsapp_moc.py                        \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-simplefsapp_moc simplefsapp_moc.py                        \
            --man                                                       \
            /incoming /outgoing

Examples
--------





