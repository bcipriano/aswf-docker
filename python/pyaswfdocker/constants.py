import typing
from . import versioninfo

VERSIONS = {
    "packages": {
        "clang": ["1"],
        "python": ["2018", "2019", "2020"],
        "boost": ["2018", "2019", "2020"],
        "tbb": ["2018", "2019", "2020"],
        "cppunit": ["2018", "2019", "2020"],
        "glew": ["2018", "2019", "2020"],
        "glfw": ["2018", "2019", "2020"],
        "log4cplus": ["2018", "2019", "2020"],
        "qt": ["2018", "2019", "2020"],
        "pyside": ["2018", "2019", "2020"],
        "blosc": ["2018", "2019", "2020"],
        "openexr": ["2018", "2019", "2020"],
        "alembic": ["2018", "2019"],
        "ocio": ["2018", "2019"],
        "oiio": ["2018", "2019"],
        "opensubdiv": ["2018", "2019"],
        "ptex": ["2018", "2019"],
        "openvdb": ["2019"],
        "usd": ["2019"],
    },
    "images": {
        "common": ["1"],
        "base": ["2018", "2019", "2020"],
        "openexr": ["2018", "2019", "2020"],
        "openvdb": ["2018", "2019", "2020"],
        "ocio": ["2018", "2019"],
        "opencue": ["2018", "2019", "2020"],
        "usd": ["2019"],
        "vfxall": ["2019"],
    },
}

GROUPS = {
    "packages": {
        "common": ["clang"],
        "base": ["python", "boost", "tbb", "cppunit", "glew", "glfw", "log4cplus"],
        "baseqt": ["qt"],
        "basepyside": ["pyside"],
        "vfx": [
            "blosc",
            "openexr",
            "alembic",
            "ocio",
            "oiio",
            "opensubdiv",
            "ptex",
            "openvdb",
            "usd",
        ],
    },
    "images": {
        "common": ["common"],
        "base": ["base"],
        "vfx": ["openexr", "openvdb", "ocio", "opencue", "usd", "vfxall"],
    },
}

VERSION_INFO = {
    "2018": versioninfo.VersionInfo(
        version="2018",
        label=None,
        aswfVersion="2018.X",
        ciCommonVersion="1",
        pythonVersion="2.7",
    ),
    "2019": versioninfo.VersionInfo(
        version="2019",
        label="latest",
        aswfVersion="2019.X",
        ciCommonVersion="1",
        pythonVersion="2.7",
    ),
    "2020": versioninfo.VersionInfo(
        version="2020",
        label="preview",
        aswfVersion="2020.X",
        ciCommonVersion="1",
        pythonVersion="3.7",
    ),
}

PUBLISH_DOCKER_ORG = "aswf"
TESTING_DOCKER_ORG = "aswftesting"
# this org is not valid, but this ensures that the test will not accidently pull an existing image
FAKE_DOCKER_ORG = "aswflocaltesting"
