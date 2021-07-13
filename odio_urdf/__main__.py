"""
Author: hauptmech <hauptmech@gmail.com>
License in __init__.py
"""
import sys
import odio_urdf

if len(sys.argv) != 2:
    print("""
    Usage: odio_urdf xacro.xml
    
    Partially converts the file on the command line from xacro to python as an aid
    to converting existing xacro based models to odio_urdf code.
    """)
    exit(0)

inf = open(sys.argv[1])
print(odio_urdf.urdf_to_odio(inf.read()))