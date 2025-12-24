import asyncio
import logging
from bleak import BleakClient, BleakScanner

# Constants from our integration
MAC_ADDRESS = "F4:90:E2:21:DE:78"
SERVICE_UUID = "0000f000-0000-1000-8000-00805f9b34fb"
CHAR_UUID = "0000f001-0000-1000-8000-00805f9b34fb"
PAYLOAD = b"\x01"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ble_test")

async def run():
    logger.info(f"Looking for {MAC_ADDRESS}...")
    device = await BleakScanner.find_device_by_address(MAC_ADDRESS, timeout=20.0)
    
    if not device:
        logger.error("Device not found!")
        return

    logger.info(f"Found {device.name}. Connecting...")
    
    async with BleakClient(device) as client:
        logger.info(f"Connected: {client.is_connected}")
        
        logger.info("Services:")
        for service in client.services:
            logger.info(f"  {service.uuid}")
            for char in service.characteristics:
                 logger.info(f"    {char.uuid} ({char.properties})")

        logger.info(f"Writing {PAYLOAD} to {CHAR_UUID}...")
        try:
            await client.write_gatt_char(CHAR_UUID, PAYLOAD, response=True)
            logger.info("Write successful!")
        except Exception as e:
            logger.error(f"Write failed: {e}")

if __name__ == "__main__":
    asyncio.run(run())
