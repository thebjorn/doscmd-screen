

Developing dosbox-screen
========================


Running tests
------------------------------------------------------------

I'm really not sure how to do any unit testing of this, since the
errors are mostly visual.

There is a `test_screen.py` script included that excercises the
functionality and creates a screen that can be inspected visually.

Coverage can be run with::

    coverage run test_screen.py && coverage report



Building documentation
------------------------------------------------------------
::

    python setup.py build_sphinx



Uploading to PyPI
-----------------

- only source distribution::

    python setup.py sdist upload

- source and windows installer::

    python setup.py sdist bdist_wininst upload

- source, windows, and wheel installer::

    python setup.py sdist bdist_wininst bdist_wheel upload

- create a documentation bundle to upload to PyPi::

    cd build/sphinx/html && zip -r ../../../pypi-docs.zip *
