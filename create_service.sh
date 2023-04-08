#!/bin/bash
# Create the symlink
sudo ln -s ~/stem-course/mobilenet_based_classifier.service /lib/systemd/system

# Reload the service files so the system knows about this new one
sudo systemctl daemon-reload

sudo systemctl enable mobilenet_based_classifier.service
