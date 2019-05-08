# Linio Numbers

## Coding Challenge

Write a program that prints all the numbers from 1 to 100. However, for multiples of 3, instead of the number, print **"Linio"**. For multiples of 5 print **"IT"**. For numbers which are multiples of both 3 and 5, print **"Linianos"**.

But here's the catch: you can use only one **"if"**. No multiple branches, ternary operators or **"else"**.

### Requirements

**1.** 1 **"if"**.
**2.** You can't use **"else"**, **"else if"** or ternary.
**3.** Unit tests.
**4.** Feel free to apply your **SOLID knowledge**.

## Solution

### Requirements/Dependencies

+ git version 2.21.0

Installation: https://git-scm.com/downloads

+ Docker version 18.09.0

Installation: https://docs.docker.com/install/#server

+ docker-compose version 1.23.2

Installation: https://docs.docker.com/compose/install/#prerequisites

### Clone Repository and Build the Application

+ Clone the solution repository.

+ Access the solution directory with the following command:

```bash
cd SOLUTION_DIRECTORY
```

+ Build the application, running the following command:

```bash
sudo docker-compose build
```

### Run for first time the Application

+ To start for first time the application, please run the following command:

```bash
sudo docker-compose up -d
```

### Run the Application

You have two ways to run the application.

First way, please run the following commands:

```bash
sudo docker-compose exec app bash
python linio_numbers.py
```

Second way, please run the following command:

```bash
sudo docker-compose exec app bash -c 'python linio_numbers.py'
```

### Run the Unit Tests

Ypu have two ways to run the unit tests.

First way, please run the following commands:

```bash
sudo docker-compose exec app bash
python -m pytest tests.py
```

Second way, please run the following command:

```bash
sudo docker-compose exec app bash -c 'python -m pytest tests.py'
```
