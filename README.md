# challenge-api

The backend service for interacting with project challenge database.

# Getting Started

Before you start, please check that the following are installed:

- python3
    ```bash
    $ python3 --version
    ```

- pip3
    ```bash
    $ pip3 --version
    ```

## Setup your virtual environments

Virtual environments in Python allow us to download Python libraries (also known as packages) for our project without installing them globally, i.e. on your machine.

### Installation

To install `virtualenv` run:

```bash
$ pip3 install virtualenv
```

Setup `virtualenv` in this project:

**Mac with Intel chip**

```bash
$ git clone git@github.com:iusmumn/challenge-api.git
$ cd challenge-api/
$ virtualenv venv
```

**Mac with Apple chip** _(Or if `virtualenv` just isn't working on your machine)_

```bash
$ git clone git@github.com:iusmumn/challenge-api.git
$ cd challenge-api/
$ python3 -m venv venv/
```

You will notice that a `venv/` directory was created. This is where all your future downloaded Python packages for this project will be stored from now on!

_Note: This only has to be done once. No need to do it again when developing._

### Using Virtual Environments

EVERY TIME you develop on this project, please run through the following process!

1. Activate `virtualenv`

    ```bash
    $ source venv/bin/activate
    ```

    - You should see a `(venv)` appear in your terminal indicating you are now in a virtual environment!
    
    - Now we can freely install Python packages we may need using `pip3` 🚀

1. Install any Python packages you may need

    ```bash
    $ pip3 install <package_name>
    ```
    Example:
    ```
    $ pip3 install flask
    ```

1. When you are done developing, exit the virtual environment like so

    ```bash
    $ deactivate
    ```

## Running the API

Follow these steps to run the Flask API server

1. Activate `virtualenv`

    ```bash
    $ source venv/bin/activate
    ```

1. If you haven't already, install the `flask` package

    ```bash
    $ pip3 install flask
    ```

1. Run the server

    ```bash
    $ python3 api.py
    ```
    
    Alternatively, you can also run it like this:

    ```bash
    $ export FLASK_APP=api.py
    $ flask run
    ## Or if you want to be fancy
    $ FLASK_APP=api.py flask run
    ```

1. Test the server

    ```bash
    $ curl http://localhost:5000/
    # should return the following
    > Hello, from Challenge API!
    ```

## Running and accessing the database

Follow these steps to run the Postgres database server

1. Turn on Docker and ensure it is running on your machine

1. Open your terminal and `cd` to this project

1. Run the database server (it usually takes no more than a minute to start)

    ```bash
    $ docker-compose up
    ```

    You should see this log statement which indicates the database server is ready

    ```bash
    LOG:  database system is ready to accept connections
    ```

1. Open PgAdmin4 and connect to the database

1. Shutdown database server with <kbd>CTRL</kbd>+<kbd>C</kbd> in the original terminal session

    ```bash
    $ docker-compose down -v
    ```