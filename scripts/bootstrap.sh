# install aws-cli
  sudo apt-get update
  sudo apt-get install awscli 

# download and install the deploy service install
  # change to home to download the deploy service install
  cd /home/ubuntu
  # download the install from s3
  wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
  # add the execute permissions
  chmod +x ./install
  # install the deploy service
  sudo ./install auto
  # clean up the deploy install file
  rm ./install


