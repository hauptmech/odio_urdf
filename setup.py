try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import xml.etree.ElementTree as ET

pkg_info = ET.parse("package.xml")
info = pkg_info.getroot()

setup(
    name="{}".format(info.find("name").text),
    version="{}".format(info.find("version").text),
    maintainer="{}".format(info.find("maintainer").text),
    maintainer_email="{}".format(info.find("maintainer").attrib["email"]),
    description="{}".format(info.find("description").text),
    license="{}".format(info.find("license").text),
    packages=["odio_urdf"],
    package_dir={"odio_urdf": "odio_urdf"},
)
