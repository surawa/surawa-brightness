# coding: utf-8
from beaglebone.surawabone import SurawaBone
import cherrypy


class RESTResource(object):
    """
    Base class for providing a RESTful interface to a resource.
    
    To use this class, simply derive a class from it and implement the methods
    you want to support.  The list of possible methods are:
    handle_GET
    handle_PUT
    handle_POST
    handle_DELETE
    """
    @cherrypy.expose
    def default(self, *vpath, **params):
        method = getattr(self, "handle_" + cherrypy.request.method, None)
        if not method:
            methods = [x.replace("handle_", "")
               for x in dir(self) if x.startswith("handle_")]
            cherrypy.response.headers["Allow"] = ",".join(methods)
            raise cherrypy.HTTPError(405, "Method not implemented.")
        return method(*vpath, **params);

class SurawaRessource(RESTResource):
    
    
    def __init__(self):
        RESTResource.__init__(self)
        # init hardware interface class
        self.bb = SurawaBone()
        
        
    def handle_GET(self, *vpath, **params):
        if len(vpath) == 2 and  len(params) == 0 and vpath[0] == "brightness" and vpath[1] == "value":
            return self.bb.getPhotoresistorValue()
#            return "1249" # debug purpose  
        else:
            retval = "Path Elements:<br/>" + '<br/>'.join(vpath)
            query = ['%s=>%s' % (k,v) for k,v in params.items()]
            retval += "<br/>Query String Elements:<br/>" + \
                '<br/>'.join(query)
            return "UNKNOWN ressource</br>"+ \
                "DEBUG : " + str(len(vpath))+" "+ str(vpath)+"</br>"+\
                retval


class Root(object):
    surawa = SurawaRessource()

    @cherrypy.expose
    def index(self):
        return "REST API for Surawa architecture.</br> Prototype 1 : Is it shiny or cloudy?</br>"


def run_server():
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(Root())

              


