# Install charm-crypto

## Install Linux 20.04 LTS
Download [ubuntu-20.04.6-desktop-amd64.iso](https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso)

Install new virtual machine in vmware

## From now on everything is on the vm

optional: install [vscode](https://code.visualstudio.com/download)

## Download charm-dev.zip from github
Via [charm-dev.zip](https://github.com/JHUISI/charm/archive/refs/heads/dev.zip)

## Commands to execute on terminal
Install necessary packages
```
sudo apt update
sudo apt install gcc make python3 m4 flex bison subversion python3-pip libgmp-dev libssl-dev -y
```
Create a link to python3 (so that python is enough to execute)
```
sudo ln -s /usr/bin/python3 /usr/bin/python
```
Install python package
```
pip install pyparsing==2.4.6
```
Change directory to Downloads to download and install charm, gmp and pbc
```
cd ~/Downloads/
```
Download GMP
```
wget https://ftp.gnu.org/gnu/gmp/gmp-5.1.3.tar.bz2
```
Download PBC
```
wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
```
Extract GMP to /usr/loca/src
```
sudo tar -jxvf gmp-5.1.3.tar.bz2 -C /usr/local/src
```
Extract PBC to /usr/loca/src
```
sudo tar -zxvf pbc-0.5.14.tar.gz -C /usr/local/src
```
Extract charm-dev to /usr/local/src
```
sudo unzip charm-dev.zip -d /usr/local/src
```
1. Move to extracted gmp to install it
```
cd /usr/local/src/gmp-5.1.3/
```
Installation commands:
```
sudo ./configure
sudo make
sudo make install
```
Expected output:

![alt text](img/image.png)

2. Move to extracted PBC to install it
```
cd ../pbc-0.5.14
```
installation commands:
```
sudo ./configure
sudo make
sudo make install
```
Expected output:

![alt text](img/image-1.png)

3. Move to extracted charm-dev to install it
```
cd ../charm-dev/
```
Commands to install:
```
sudo ./configure.sh
sudo make
sudo make install
```
Expected output:

![alt text](img/image-2.png)

## Test
```
python tests/test_abe.py
python tests/test_ibe.py
```