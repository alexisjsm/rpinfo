#! /usr/bin/python3
import sys
import logging
import site

logging.basicConfig(stream=sys.stderr)

site.addsitedir("/var/www/index/rpinfo/.env/lib/python3.7/site-packages")

sys.path.insert(0,"/var/www/index/rpinfo/back")

from app import  app as application
