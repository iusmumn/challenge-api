# challenge-api

The backend service for interacting with project challenge database.

# Getting Started

Before you start, please check that the following are installed:

- python3
    ```
    $ python3 --version
    ```

- pip3
    ```
    $ pip3 --version
    ```

## Setup your virtual environments

Virtual environments in Python allow us to download Python libraries (also known as packages) for our project without installing them globally, i.e. on your machine.

### Installation

To install `virtualenv` run:

```
$ pip3 install virtualenv
```

Setup `virtualenv` in this project:

```
$ cd challenge-api/
$ virtualenv venv
```

You will also notice that a `venv/` directory was created. This is where all your future Python packages for this project will be downloaded to from now on!

_Note: This only has to be done once. No need to do it again when developing._

### Usage

Whenever you develop on this project, please run through the following process!

1. Activate `virtualenv`

    ```
    $ source venv/bin/activate
    ```

    - You should see a `(venv)` appear in your terminal indicating you are now in a virtual environment!
    
    - Now we can freely install Python packages we may need using `pip3` 🚀

1. Install any Python packages you may need

    ```
    $ pip3 install <package_name>
    ```
    Example:
    ```
    $ pip3 install flask
    ```

1. When you are done developing, exit the virtual environment like so

    ```
    $ deactivate
    ```