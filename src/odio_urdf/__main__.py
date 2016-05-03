"""
  Partially converts the file on the command line from xacro to python as an aid
to converting existing xacro based models to odio_urdf code.

"""
import sys
import odio_urdf

inf = open(sys.argv[1])
print(odio_urdf.dump_urdf(inf.read()))
