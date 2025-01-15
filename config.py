#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7771972842:AAFwt18xjqx9hYMY4gDnw6IxaCqz_xngegM")
    API_ID = int(os.environ.get("API_ID", "21008992"))
    API_HASH = os.environ.get("API_HASH", "da87f6dea5ed8cfe1a53617e33a35742")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7548265642")
