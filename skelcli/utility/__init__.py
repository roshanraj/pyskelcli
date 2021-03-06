#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re
import os
import ast
import datetime
import unicodedata
import configparser


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root


def slugfy(text):
    try:
        slug = unicodedata.normalize("NFKD", text).encode("UTF-8", "ignore")
    except:
        slug = text
    slug = re.sub(r"[^\w]+", " ", slug)
    slug = "-".join(slug.lower().strip().split())
    if not slug:
        return None
    return slug


def conf(section, ini="config.ini"):
    config = configparser.ConfigParser()
    if os.path.isfile(os.path.join(PROJECT_PATH, ini)):
        config.read(os.path.join(PROJECT_PATH, ini))
    else:
        config.read(os.path.join(PROJECT_PATH, "config.sample.ini"))
    _dict = {}
    options = config.options(section)

    for option in options:
        try:
            _dict[option] = ast.literal_eval(config.get(section, option))
        except:
            try:
                _dict[option] = config.get(section, option)
            except:
                _dict[option] = None

    return _dict


def log_it(s, name=u"core"):
    with open("/tmp/openmining-{}.log".format(name), "a") as log:
        msg = u"{} => {}\n".format(datetime.now(), s)
        log.write(msg.encode('utf-8'))


def __from__(path):
    try:
        _import = path.split('.')[-1]
        _from = u".".join(path.split('.')[:-1])
        return getattr(__import__(_from, fromlist=[_import]), _import)
    except TypeError:
        return object

