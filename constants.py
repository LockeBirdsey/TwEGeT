from enum import Enum


class BuildState(Enum):
    NOTHING = 1
    UPDATING = 2
    BUILDING_NEW = 3
    BUILDING_WEB = 4
    SETUP = 5
    PENDING = 6


NPM = "npm"
NPX = "npx"
TWEEGO = "tweego"
DETAILS_FILE_NAME = "tweget.json"
YARN_PACKAGE_FILE = "package.json"

ELECTRON_SOURCE_DIR = "src"

# Keys
## Lib keys
NPM_LOCATION = "npm_location"
NPX_LOCATION = "npx_location"
TWEEGO_LOCATION = "tweego_location"

## Project keys
PROJ_NAME = "name"
PROJ_DIR = "directory"
PROJ_HTML = "html"
PROJ_PARENT_DIR = "output_directory"
PROJ_BUILD_DIR = "build_directory"
PROJ_VERSION = "version"
PROJ_DIMS_WIDTH = "width"
PROJ_DIMS_HEIGHT = "height"
PROJ_ICON_LOCATION = "icon_location"
PROJ_KEYWORDS = "keywords"
PROJ_LAST_UPDATED = "last_updated"

## Author Keys
AUTHOR_NAME = "Name"
AUTHOR_EMAIL = "Email"
AUTHOR_REPO = "Repository"

HELP_STRING = "TODO\nFor more support visit: https://github.com/LockeBirdsey/TwEGeT"

INDEX_JS = "index.js"
INDEX_JS_TEMPLATE_PATH = "./templates/" + INDEX_JS
JS_WIDTH_KEY = "%WIDTH%"
JS_HEIGHT_KEY = "%HEIGHT%"

# Media suffixes
IMG = "img"
AUDIO = "audio"
VIDEO = "video"
# Audio
WAV_SUFFIX = "wav"
FLAC_SUFFIX = "flac"
MP3_SUFFIX = "mp3"
OGG_SUFFIX = "ogg"
AUDIO_SUFFIXES = {
    WAV_SUFFIX,
    FLAC_SUFFIX,
    MP3_SUFFIX,
    OGG_SUFFIX
}

# Images
PNG_SUFFIX = "png"
JPG_SUFFIX = "jpg"
JPEG_SUFFIX = "jpeg"
GIF_SUFFIX = "gif"
IMAGE_SUFFIXES = {
    PNG_SUFFIX,
    JPEG_SUFFIX,
    JPG_SUFFIX,
    GIF_SUFFIX
}

# Video
MP4_SUFFIX = "mp4"
MOV_SUFFIX = "mov"
VIDEO_SUFFIXES = {
    MP4_SUFFIX,
    MOV_SUFFIX
}

DUMMY_IMG_BASE64 = b'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAD/SURBVHhe7dExAQAgDMCwgX/P40FEjuapgJ7dnTjubxANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTQE0xBMQzANwTSEMvMA+80DxT1NiBwAAAAASUVORK5CYII=='
