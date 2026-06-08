# Python examples

This folder contains simple host-side Python examples for the MeatPi USB CAN firmware.

## Layout

- `slcan\linux_slcan_example.py` - direct SLCAN serial example for Linux
- `slcan\windows_slcan_example.py` - direct SLCAN serial example for Windows
- `gs_can\linux_gs_can_example.py` - Linux SocketCAN example for the `gs_usb` firmware
- `gs_can\windows_gs_can_example.py` - Windows `gs_usb` example

## Dependencies

### SLCAN

```bash
pip install python-can pyserial
```

### GS CAN on Linux

```bash
pip install python-can
```

Bring the Linux CAN interface up before running the script, for example:

```bash
sudo ip link set can0 up type can bitrate 500000
```

### GS CAN on Windows

```powershell
pip install "python-can[gs-usb]"
```

On Windows, the GS USB interface also needs a libusb-compatible driver such as `libusbK`.

#### Zadig setup

1. Download and open Zadig: https://zadig.akeo.ie/
2. Plug in the MeatPi adapter and start the `gs_usb` firmware.
3. In Zadig, enable **Options -> List All Devices**.
4. Select the MeatPi USB CAN device from the device list.
5. Choose **libusbK** as the target driver.
6. Click **Replace Driver** or **Install Driver**.

After Zadig finishes, unplug and reconnect the adapter, then run the Windows GS CAN example.
