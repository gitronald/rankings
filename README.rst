Rankings
========

Rankings is a Python package for comparing ranked lists and
quantifying their differences and similarities.

Development
   https://github.com/gitronald/rankings


Download
--------

To install the git version run:

::

    $ git clone git://github.com/gitronald/rankings.git
    $ cd rankings
    $ pip install .


Usage
-----

A quick example that finds the shortest path between two nodes in an undirected graph::

   >>> import rankings
   >>> list1 = ['sam', 'sue', 'stew', 'baloo', 'baloo']
   >>> list2 = ['sue', 'sam', 'baloo', 'new', 'baloo']
   >>> compare_ranks(list1, list2)
   (0.6, 3)

Bugs
----

Our issue tracker is at https://github.com/gitronald/rankings/issues.
Please report any bugs that you find.  Or, even better, fork the repository on
GitHub and create a pull request.  We welcome all changes, big or small, and we
will help you make the pull request if you are new to git
(just ask on the issue).

License
-------

Distributed with a BSD license; see LICENSE::

   Copyright (C) 2017 Ronald E. Robertson <rer@ronalderobertson.com>

