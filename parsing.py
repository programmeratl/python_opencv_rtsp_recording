import xml.sax
from PyDictionary import PyDictionary
class XMLParser( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.name = ""
      self.url = ""
      self.fps = ""
      self.schedule = ""
      self.detail={}
      self.counter=0
     
   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "stream":
         print "*****Stream*****"
         self.url = attributes["url"]
         print "RTSP:", self.url

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "name":
         print "Name:", self.name
	 #self.detail.update({self.counter:[1, 3.5, "Hello"]})
	 self.detail.update({self.counter:[self.name,self.url, self.fps, self.schedule]})
      elif self.CurrentData == "fps":
         print "FPS:", self.fps
	 #self.detail.update({'fps': self.fps})
	 self.detail.update({self.counter:[self.name,self.url, self.fps, self.schedule]})
      elif self.CurrentData == "schedule":
         print "Schedule:", self.schedule
	 #self.detail.update({'schedule': self.schedule})
	 self.detail.update({self.counter:[self.name,self.url, self.fps, self.schedule]})
      else:
	 self.counter+=1	
      self.CurrentData = ""
      #self.detail.update({self.counter:[self.name,self.url, self.fps, self.schedule]})
     
     
   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "name":
         self.name = content
      elif self.CurrentData == "fps":
         self.fps = content
      elif self.CurrentData == "schedule":
         self.schedule = content
   #return detail object
   def get_detail(self):   
	  return self.detail
"""
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = XMLParser()
   parser.setContentHandler( Handler )
   
   parser.parse("data.xml")
"""