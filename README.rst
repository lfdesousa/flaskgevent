Demo flask webapp with gevent
============

This is a demo webapp using flask servicing requests with asynchronous I/O through gevent which uses the libevent library demonstrating asynchronous I/O performance and usage in a webapp, or any other urllib2 using python library.

.. image:: https://api.travis-ci.org/pkittenis/flaskgevent.png?branch=master
	:target: https://travis-ci.org/pkittenis/flaskgevent

************
Siege results on static json page under gunicorn
************

This is a simple test, would get better performance under heavy load by using gunicorn under apache as a proxy passthrough, see gunicorn documentation.

::

  ** SIEGE 3.0.1
  ** Preparing 500 concurrent users for battle.
  The server is now under siege...
  Lifting the server siege...      done.

  Transactions:		       27856 hits
  Availability:		      100.00 %
  Elapsed time:		       29.46 secs
  Data transferred:	        0.61 MB
  Response time:	        0.03 secs
  Transaction rate:	      945.55 trans/sec
  Throughput:		        0.02 MB/sec
  Concurrency:		       23.90
  Successful transactions:     27856
  Failed transactions:	           0
  Longest transaction:	        3.13
  Shortest transaction:	        0.00
