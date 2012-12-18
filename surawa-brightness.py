# coding: utf-8
"""
SURAWA Prototype -- author open.surawa@gmail.com // https://github.com/surawa/

Is it day or night ? Cloudy or Sunny ?

2012 - Suround awareness, helps bringing Nao to life

WebServer based on CherryPy : http://www.cherrypy.org/
Hosted by a beaglebone : http://beagleboard.org/bone
And a custom circuit, that only uses a photoresistor : http://en.wikipedia.org/wiki/Photoresistor, pluged to an analogic pin
Based on an Ubuntu distribution for the BeagleBone : http://elinux.org/BeagleBoardUbuntu

The application reads the current value of the pin connected to the photoresistor and serves it as a REST ressource.
Server is listening on his IP (obtained by DHCP) and on port 8080
The prototype ressource is available on URL : http://<IP>:8080/surawa/brightness/value


Licence : GPL 
"""

from surawarestengine.surawarestengine import *


if __name__ == "__main__":
    run_server()
    
