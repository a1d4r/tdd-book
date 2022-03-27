Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see [`nginx.template.conf`](nginx.template.conf)
* replace SITENAME with, e.g., `staging.my-domain.com`

## Systemd service

* see [`gunicorn-systemd.template.service`](gunicorn-systemd.template.service)
* replace SITENAME with, e.g., `staging.my-domain.com`

## Folder structure:

Assume we have a user account at /home/USER

```
/home/USER
└── sites
    └── SITENAME
         ├── db.sqlite3
         ├── manage.py etc
         ├── static
         └── virtualenv
```