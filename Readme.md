# Project Overview

This project explores the intricate correlation between system calls and CPU execution time through a comprehensive analytical pipeline. The process involves data collection from diverse Python code repositories on GitHub, system call tracing, and predictive modeling using machine learning algorithms. The developed model is deployed through a user-friendly web application, allowing users to input Python code and receive real-time predictions of CPU execution time.

## Running the Code

### Install WSL 2.0

Follow Microsoft's official documentation to install Windows Subsystem for Linux (WSL) 2.0.

### Install Python 3

After setting up WSL, open the terminal and run the following commands:

```bash
sudo apt-get update
sudo apt-get install python3
```
## Install Required Python Packages

Install Flask, scikit-learn, and pickle using:

```bash
pip3 install Flask scikit-learn pickle
```
## Run the Application

Navigate to your project directory and execute:

```bash
python3 app.py
```
