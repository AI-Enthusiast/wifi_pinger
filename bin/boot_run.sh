#!/bin/bash

# Set the path to the directory where the script is located
cd "$(dirname "$0")" || exit

# Go to the root directory, currently in its /bin directory
cd ..

# Initiate logging
run_date="$(date +'%Y-%m-%d--%H-%M')"
exec 2>> ~/wifi_pinger/log/logfile_parent_${run_date}.log

# Update the code
git remote set-url origin git@github.com:AI-Enthusiast/wifi_pinger.git
git pull origin main

# Build and run the Docker container
docker build -t wifi_pinger . 1>> ~/wifi_pinger/log/logfile_${run_date}.log 2>> ~/wifi_pinger/log/errfile_${run_date}.log
docker run --rm -v "$(pwd)"/archive:/ping_google/archive wifi_pinger 1>> ~/wifi_pinger/log/logfile_${run_date}.log 2>> ~/wifi_pinger/log/errfile_${run_date}.log

# Clean up Docker resources
docker image rm wifi_pinger 1>> ~/wifi_pinger/log/logfile_${run_date}.log 2>> ~/wifi_pinger/log/errfile_${run_date}.log
docker container prune -f 1>> ~/wifi_pinger/log/logfile_${run_date}.log 2>> ~/wifi_pinger/log/errfile_${run_date}.log