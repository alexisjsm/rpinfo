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
 pip install -r virtualenv
```

create virtualenv:

``` bash
 virtualenv env --python=python3
```

activate the virtualenv:

``` bash
source ~/env/bin/active
```

The dependencies install with following command:

``` bash
pip install -r requirements.txt
```

Then the **front** folder install nodejs dependecies with:

``` bash
npm install
```

and build the app

``` bash
npm run build
```

When this's finish, run the server with command `python app.py` in the **back** folder.

## Usage

- System information
- Disk information
- CPU information
- RAM information

## TODO

- Translate all to English
- Ethernet information

### issues

> There is possible more issues it isn't know.
