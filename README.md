# Rpinfo

Rpinfo is a basic web app of information for Raspberry Pi

## Installation

### Prerequisites

- pip 20.x >=
- python 3.7 >=
- nodejs 12.4 >=  
- npm 13.6 >=

### First-time

Install virtual_env:

``` bash 
# debian / ubuntu
apt install virtualenv python3-devel
# fedora
dnf install python3-virtualenv  python3-devel
```

Create virtualenv:

``` bash
 virtualenv .env --python=python3
```

activate the virtualenv:

``` bash
source ~/.env/bin/activate
```

The dependencies install with following command:

``` bash
pip install -r requirements.txt
```

Then the **front** folder install nodejs dependencies with:

``` bash
npm install
```

and build the app

``` bash
npm run build
```

When this's finish, run the server with command `flask run` in the **back** folder.

## Usage

- System information
- Disk information
- CPU information
- RAM information

## TODO
- Make a install script
- Translate all to English
- Ethernet information

### issues

> There is possible more issues it isn't known.
