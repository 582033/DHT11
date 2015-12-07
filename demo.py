#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_DHT as dht
import time

while True:
    time.sleep(0.5)
    h,t = dht.read_retry(dht.DHT11, 4)
    print 'Temp = %.1f"C, Humidity = %.1f%%RH' % (t, h)

