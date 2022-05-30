#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

def health(self):
    return HttpResponse('200 - todo ok')
