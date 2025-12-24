# BLOOMIN8 E-Ink Canvas Bluetooth Wake-up

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

A standalone Home Assistant integration to wake up the BLOOMIN8 E-Ink Canvas device using Bluetooth Low Energy (BLE).

This integration is useful if:
- Your device goes into deep sleep and disconnects from Wi-Fi.
- You want a dedicated button to wake the device.
- You want to use this alongside the main [bloomin8 integration](https://github.com/mistrsoft/bloomin8_eink_home_assistant) or as a standalone tool.

## Features

- **Wake-on-Bluetooth**: Sends a magic BLE packet (`0x01` to `0000f001-0000-1000-8000-00805f9b34fb`) to wake the device.
- **Dedicated Button**: Creates a `button` entity in Home Assistant (e.g., `button.bloomin8_wake_button`).
- **Configurable**: Easily set the device's Bluetooth MAC address via the UI.

## Installation

### Option 1: HACS (Recommended)

1.  Open HACS in Home Assistant.
2.  Go to **Integrations** > **Triple dots** (top right) > **Custom repositories**.
3.  Add `https://github.com/mistrsoft/bloomin8_bt_wake` as `Integration`.
4.  Search for "Bloomin8 Bluetooth Wake" and install it.
5.  Restart Home Assistant.

### Option 2: Manual

1.  Copy the `custom_components/bloomin8_bt_wake` folder to your Home Assistant's `custom_components` directory.
2.  Restart Home Assistant.

## Configuration

1.  Go to **Settings** > **Devices & Services**.
2.  Click **Add Integration**.
3.  Search for **Bloomin8 Bluetooth Wake**.
4.  Enter the **Bluetooth MAC Address** of your E-ink Canvas.
    *   *Tip: You can find this in the official mobile app or by scanning for BLE devices nearby.*

## Usage

Once installed, you will have a button entity (e.g., `button.my_canvas_wake_button`).
Pressing this button will connect to the device via BLE and send the wake command.

## Credits

Reverse engineered and developed for the Bloomin8 community.
