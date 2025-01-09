#!/bin/bash

# Get the current hour
current_hour=$(date +"%H")

# Create a hidden file with the current hour
touch ~/.current_hour_$current_hour
git add .
git commit -m "testing"
git push
