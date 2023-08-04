"""Constants for the Philips Hue Play HDMI Sync Box integration."""
import logging

DOMAIN = "huesyncbox"
LOGGER = logging.getLogger(__package__)

DEFAULT_PORT = 443


MANUFACTURER_NAME = "Signify"

REGISTRATION_ID = "registration_id"

INTENSITY_SUBTLE = "subtle"
INTENSITY_MODERATE = "moderate"
INTENSITY_HIGH = "high"
INTENSITY_INTENSE = "intense"

INTENSITIES = [INTENSITY_SUBTLE, INTENSITY_MODERATE, INTENSITY_HIGH, INTENSITY_INTENSE]

SYNC_MODE_VIDEO = "video"
SYNC_MODE_MUSIC = "music"
SYNC_MODE_GAME = "game"

SYNC_MODES = [SYNC_MODE_VIDEO, SYNC_MODE_MUSIC, SYNC_MODE_GAME]


INPUT_HDMI1 = "input1"
INPUT_HDMI2 = "input2"
INPUT_HDMI3 = "input3"
INPUT_HDMI4 = "input4"

INPUTS = [INPUT_HDMI1, INPUT_HDMI2, INPUT_HDMI3, INPUT_HDMI4]


SERVICE_SET_BRIDGE = "set_bridge"
SERVICE_SET_SYNC_STATE = "set_sync_state"

ATTR_BRIDGE_ID = "bridge_id"
ATTR_BRIDGE_USERNAME = "bridge_username"
ATTR_BRIDGE_CLIENTKEY = "bridge_clientkey"


ATTR_SYNC = "sync"
ATTR_SYNC_TOGGLE = "sync_toggle"

ATTR_MODE = "mode"
ATTR_MODE_NEXT = "mode_next"
ATTR_MODE_PREV = "mode_prev"

ATTR_INTENSITY = "intensity"
ATTR_INTENSITY_NEXT = "intensity_next"
ATTR_INTENSITY_PREV = "intensity_prev"

ATTR_INPUT = "input"
ATTR_INPUT_NEXT = "input_next"
ATTR_INPUT_PREV = "input_prev"


ATTR_ENTERTAINMENT_AREA = "entertainment_area"
