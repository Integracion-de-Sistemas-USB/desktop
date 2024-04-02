import pytest
from unittest.mock import Mock
from .external_peripheral import ExternalPeripheral
from .constants import SHOOT_ACTION, PRESS_STATUS

POS_XY = (0, 0)

@pytest.fixture
def mocked_joycon():
    joycon_mock = Mock()
    joycon_mock.pointer = POS_XY
    joycon_mock.events.return_value = [(SHOOT_ACTION, PRESS_STATUS)]
    return joycon_mock

@pytest.fixture
def external_peripheral(mocked_joycon):
    external_peripheral_instance = ExternalPeripheral()
    external_peripheral_instance.joycon = mocked_joycon
    return external_peripheral_instance

def test_external_peripheral(external_peripheral):
    pointer_position = external_peripheral.get_pointer_position()
    assert pointer_position == POS_XY
    
    button_events = external_peripheral.get_button_events()
    assert button_events == [(SHOOT_ACTION, PRESS_STATUS)]
