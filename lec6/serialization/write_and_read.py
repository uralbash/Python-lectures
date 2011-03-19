import sys, cPickle

try:
   file = open( "users.dat", "w" )   
except IOError, message:             
   print >> sys.stderr, "File could not be opened:", message
   sys.exit( 1 )

inputList = []

inputList.append( "A" ) 
inputList.append( "B" ) 
inputList.append( "C" ) 

cPickle.dump( inputList, file )  

file.close()

# Reading and printing pickled object in a file.

try:
   file = open( "users.dat", "r" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )
   
records = cPickle.load( file ) 
file.close()

for record in records:         
   print record[ 0 ].ljust( 15 ),
