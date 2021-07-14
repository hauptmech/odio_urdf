## What is it?

Odio URDF allows one to build a data structure of similar form to URDF using python
classes. This allows a natural integration into python code for calculation and
is just nicer to work with than XML and XACRO. 

The structure can dump it's URDF XML equivalent at any time.

Robot models can be built by in-place definition, or sequential construction, 
which ever best suits the task.

> odio_urdf depends on catkin_pkg, which needs to be manually installed if you want to use it on a non ROS environment. `pip install catkin_pkg`

## But my model is a beautiful hierarchy of Xacro

This is much more powerful and easier to use than xacro.

There is some code in place to allow working with directly copied xacro based URDF's
by processing xacro elements, including macro references embedded in strings. This help
speed transcribing a xacro based model if you need to.


`/test/coman/coman.py` provides a demo of odio_urdf in action and is a convesion of 
[iit-coman-ros-pkg](https://github.com/EnricoMingo/iit-coman-ros-pkg) on github which
makes moderate use of xacro.

`/test/iiwa/iiwa7.urdf.py` is demo of the Kuka iiwa7 from the [data of iiwa_stack](https://github.com/SalvoVirga/iiwa_stack).

## So how do I use it?

Each URDF element has a corresponding odio_urdf class of the same name in title case.

`<robot ...>` has a corresponding class `Robot()` for instance.

One may construct a robot in place, duplicating a URDF structure, if one wants.

To duplicate the [tutorial urdf here](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file), your python code would look like:

```python
# If you have OCD and need a clean namespace, change to standard import
from odio_urdf import * 

my_robot = Robot(
    Link(name="link1"),
    Link(name="link2"),
    Link("link3"), #String arguments without keys are assumed to be 'name'
    Link(name="link4"),

    Joint("joint1", Parent("link1"), Child("link2"), type="continuous"),
    Joint("joint2", 
        Parent("link1"),
        Child("link2"),
        type="continuous" #KeyValue arguments go at the end of a call
    ),
    Joint("joint3", Parent("link3"), Child("link4"), type="continuous")
) 

print(my_robot) #Dump urdf to stdout
```

(You can check it works before installing by running the code from the src folder. Copy the code to `src/test.py` and run it from that directory. `cd src; python test.py`)

However, if you prefer, (or need), a sequential style, it works well. A bit of 
niceness is that the element name will be extracted from the python dictionary
if you don't specify it explicitly.

```python
my_robot = Robot()
link1 = Link() #name 'link1' will be used unless link1.name is set 
link2 = Link() 
link3 = Link("special_name") #This link has the name 'special_name' 

#Add first elements to robot

my_robot(link1,link2,link3)

base = Parent("link1")
joint1 = Joint(base, Child("link2"), type="continuous") 
joint2 = Joint(base, Child("link3"), type="continuous")
joint3 = Joint(Parent("link3"), Child("special_name"), type="continuous")

my_robot(joint1,joint2,joint3)

print(my_robot)
```

It can be useful to spread robot definitions across python modules, or to have
standard, re-usable components. To facilitate this, there is a 'Group' class
that is like Robot, but when included in an existing robot will be flattened.

legs.py
```python
left_leg = Group(Link(),Link(),Joint())
```

robot.py
```python
my_robot = Robot()

import legs

my_robot(legs.left_leg) 
```

Finally, as a bit of syntactic sugar, one can pass the class name only to get
a default instantiation. 

```python
quick = Joint(Origin) #Adds a default origin element
```

As a reminder, for each URDF element and attribute, there is a corresponding 
odio_urdf class and attribute. Each child element is accessed list style. Each 
attribute is accessed class member style.

```python
grey =      Material(Color(rgba="0.5 0.5 0.5 1"))
grey[0].rgba = "0.1 0.1 0.1 1"
```
### Launch File

One question that has come up is, "how do I use it?" This is the beauty of using 
a programming language for data description. The executable is the data.

Here's a launch file for the iit-coman package with the original robot_description
commented out and replaced with the odio_urdf equivalent.

```xml
<launch>
     <arg name="gui" default="true" />

     <!-- send the coman robot XML to param server -->
     <!--param name="robot_description" command="$(find xacro)/xacro.py '$(find coman_urdf)/urdf/coma
n.urdf.xacro'" /-->
     <param name="robot_description" command="$(find coman_urdf)/odio_urdf/coman.py" />
     <param name="robot_description_semantic" textfile="$(find coman_srdf)/srdf/coman.srdf" />
     <param name="use_gui" value="$(arg gui)"/>
     <param name="rate" value="50.0"/>


     <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
     <param name="publish_default_efforts" value="True"/>
     </node>

    <!-- start robot state publisher -->
    <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher" outpu
t="screen" >
        <param name="publish_frequency" type="double" value="250.0" />
    </node>

</launch>
```

### I want to use 3rd party xacro files

odio_urdf elements can be passed the xml output from xacro via `xacro_xml`, and/or hand crafted xml via `xmltext`.

```python
# source all necessary ros setup.* environments before running this code
from odio_urdf import *
import subprocess

# Start with a rotating base
my_robot = Robot("panda_with_a_twist",
                Link("swivel_base"),
                Joint("swivel_joint", Parent("swivel_base"), Child("panda_link0"), type="continuous"),
)

# Use xacro to get the franka panda arm
res = subprocess.run(['rosrun', 'xacro', 'xacro', 'panda_arm.urdf.xacro'], capture_output=True)

my_robot(xacro_xml=res.stdout)

print(my_robot)

```

### Extending odio_urdf with new elements

It's easy to add new elements and monkey patch the existing ones in an ad-hoc manner.

See `tests/new_elements_how_to.py`

---
This is a work in progress with a few rough edges. Please file issues if you see 
an opportunity for improvement. (Or even better, pull requests)
