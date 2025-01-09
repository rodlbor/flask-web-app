#!/bin/bash

# Get the current hour, minute, and second
current_time=$(date +"%H_%M_%S")

# Create a hidden file with the current time
touch ~/.current_time_$current_time

# Add, commit, and push changes to git
git add .
git commit -m "testing"
git push

