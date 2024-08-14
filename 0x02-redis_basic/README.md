# 0x02. Redis Basic

This project involves basic operations using Redis in Python. Redis is a fast, in-memory key-value store, often used for caching and other performance-related tasks.

## Project Structure

- **exercise.py**: Contains the main code for tasks 0-4, including the Cache class, decorators, and methods for storing and retrieving data from Redis.
- **web.py**: Contains the code for task 5, which involves implementing a simple web cache with expiration.
- **main.py**: A script used to test the functions implemented in exercise.py and web.py.
- **README.md**: This file contains documentation about the project, its structure, and how to run the code.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Redis server
- Redis Python client (`pip3 install redis`)
- pycodestyle for code style checks

## Installation

To install Redis on Ubuntu 18.04 LTS, use the following commands:

```sh
sudo apt-get -y install redis-server
pip3 install redis
