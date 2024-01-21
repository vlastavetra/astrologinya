# sb-gui-service

A FastAPI-based web application for managing and interacting with indices and benchmarks.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Introduction

This project is a FastAPI-based web application that allows users
to add a new indices and benchmarks.

## Features

- Add indices with associated methodology (PDF files).
- Add benchmark data from CSV files.
- Validate file extensions and sizes before adding data.
- CORS middleware to allow requests from specific origins.
- MongoDB integration for data storage.

## Prerequisites

- Python 3.10
- Required Python packages are listed in the `requirements.txt` file.

## Installation

1. Clone this repository

2. Run project in virtual environment 🚀

- Create virtual env:

```bash
        python -m virtualenv venv
```

- Create virtual environment version depend:

```bash
        virtualenv venv --python=python3.10
```

- activate

```bash
  .\venv\Scripts\activate.bat
```

- ctrl + shift + p: Python: Select interpreter
  should include Python interpreter related to your environment
- refresh terminal

3. Install requirements:
   There exist two requirements files one for production and one for development.

```bash
        pip install -r <Path_to_file>\requirements-dev.txt
```

- deactivate:

```bash
        deactivate
```

## Usage

1. Run the application:

```bash
uvicorn main:app --reload --port 8000
```

or

```bash
python main.py
```
