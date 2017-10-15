#!/bin/bash

#we need to update the package definitions
  sudo apt-get update

# install ruby
  sudo apt-get install ruby

#install nginx
  sudo apt-get install nginx
  sudo mkdir /var/www/html/homeautomation
  #configure

# download and install the deploy service install
  # change to home to download the deploy service install
  cd /home/ubuntu
  # download the install from s3
  wget https://bucket-name.s3.amazonaws.com/latest/install
  # add the execute permissions
  chmod +x ./install
  # install the deploy service
  sudo ./install auto
  # clean up the deploy install file
  rm ./install


