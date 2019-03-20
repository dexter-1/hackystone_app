# Hackystone Application

Application code for indoor localization with Bluetooth Low Energy.


The backend is written in Python 3 and uses the `Flask` framework to handle HTTP
requests. The front end uses `p5.js` to draw the path of the tag as it moves
around the room. The `socket.io` framework is used in both the front and back end
to communicate position data in real time.

## Installing dependencies
To install the dependencies for this application, run the following:

```
$ pip install -r requirements.txt
```

This application also requires the installation of redis. Installation instructions
can be found here: https://redis.io/download. Alternatively, redis can also be
installed using a package manager such as homebrew:

```
$ brew install redis
```

## Environment Setup

Add the hackystone_app package to the `PYTHONPATH` environment variable.

## Running the application
To run the application, you must first start a redis server:

```
$ redis-server /usr/local/etc/redis.conf
```

After running the redis server, the application can be run as follows:

```
$ python3 server.py
```

To view the front end, go to http://localhost:5000

## Contributing Code

Run the `run_tests.py` script and ensure no code is broken.

If you are adding a new function or module, consider creating a test and adding it to `run_tests.py`.