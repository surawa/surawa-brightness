surawa-brightness
=================

RESTful API for brightness analog sensor based on surawabone interface + photoresistor


Requirements
=================

Needs to install and refer to https://github.com/surawa/surawabone.git
Please refer to /schema/schema.png for informations about the hardware requirements

What is it ?
=================

WebServer based on CherryPy : http://www.cherrypy.org/
Hosted by a beaglebone : http://beagleboard.org/bone
And a custom circuit, that only uses a photoresistor : http://en.wikipedia.org/wiki/Photoresistor, pluged to an analogic pin
Based on an Ubuntu distribution for the BeagleBone : http://elinux.org/BeagleBoardUbuntu

The application reads the current value of the pin connected to the photoresistor and serves it as a REST ressource.
Server is listening on his IP (obtained by DHCP) and on port 8080
The prototype ressource is available on URL : http://<IP>:8080/surawa/brightness/value



How does it work ?
=================
http://ascii.io/a/1764
