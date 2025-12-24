"""Button platform for Bloomin8 Bluetooth Wake."""
from __future__ import annotations

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

import bleak
from bleak import BleakClient, BleakScanner

from .const import (
    DOMAIN,
    BLE_SERVICE_UUID,
    BLE_CHAR_UUID,
    BLE_WAKE_PAYLOAD,
    CONF_MAC_ADDRESS,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the button entity."""
    mac_address = entry.data[CONF_MAC_ADDRESS]
    name = entry.title
    
    async_add_entities([Bloomin8WakeButton(mac_address, name)])


class Bloomin8WakeButton(ButtonEntity):
    """Representation of a Bloomin8 Wake Button."""

    def __init__(self, mac_address: str, name: str) -> None:
        """Initialize the button."""
        self._mac = mac_address
        self._attr_name = name
        self._attr_unique_id = f"{mac_address}_wake_button"
        self._attr_icon = "mdi:bluetooth-connect"

    async def async_press(self) -> None:
        """Handle the button press."""
        _LOGGER.info("Sending BLE wake signal to %s", self._mac)
        
        try:
            device = await BleakScanner.find_device_by_address(self._mac, timeout=10.0)
            if not device:
                 _LOGGER.warning("Device %s not found during scan", self._mac)
                 return

            async with BleakClient(device) as client:
                if not client.is_connected:
                     _LOGGER.error("Failed to connect to %s", self._mac)
                     return

                # Write the confirmed magic byte
                await client.write_gatt_char(BLE_CHAR_UUID, BLE_WAKE_PAYLOAD, response=True)
                _LOGGER.info("Wake signal sent successfully!")
                
        except Exception as e:
            _LOGGER.error("Failed to send wake signal: %s", e)
