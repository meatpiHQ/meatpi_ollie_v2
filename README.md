<img src="https://github.com/slimelec/ollie-hw/blob/master/images/mpi_logo.png" width=300>

[www.meatpi.com](https://www.meatpi.com)
---
## MeatPi [Discord server](https://discord.gg/WXy8KQCE7V)
## Back this project on [**Crowd Supply!**](https://www.crowdsupply.com/meatpi-electronics/ollie-v2)

<br/><br/>

---

![image](https://github.com/meatpiHQ/meatpi_ollie_v2/assets/94690098/50aeb7da-0b82-41b8-ae74-c0a40db11433)


- [Pinout](#1-pinout)
- [Drivers](#2-drivers)
  - [Windows](#windows)
  - [Linux](#linux)
- [CAN](#3-can)
  - [CAN on Windows](#can-on-windows)
  - [CAN on Linux](#can-on-windows)


# 1. Pinout
![image](https://github.com/meatpiHQ/meatpi_ollie_v2/assets/94690098/30aeeb6b-d68a-4a25-8dac-d5ee201695c7)

### Note: If the switch is set to VT then UARTA/B voltage must be set by target board. Otherwise VT pins will follow the voltage level set by the swtich.

# 2. Drivers

## Windows

[**Download**](https://github.com/meatpiHQ/meatpi_ollie_v2/files/12430011/ollie_v2_drivers_win.zip) and extract the ZIP file. After extraction, go to serial folder and run the SETUP.EXE file and click on the "Install" button. Then open the CAN folder right click on MEATPI_CAN.inf and click install.

If the installation is successful, the names of COM ports will change, each corresponding to its function.

![image](https://github.com/meatpiHQ/meatpi_ollie_v2/assets/94690098/a8f38e15-4dae-4767-9b1c-77b2b322bf29)


## Linux

[**Download**](https://github.com/meatpiHQ/meatpi_ollie_v2/files/12430130/ollie_v2_drivers_linux.zip) and follow the instructions below.

```
sudo chmod +x ollie_v2.sh
sudo ./ollie_v2.sh     # This will create /dev/MEATPI-CAN0 /dev/MEATPI-RS232 /dev/MEATPI-RS485 /dev/MEATPI-UARTA /dev/MEATPI-UARTB
sudo slcand -o -s6 /dev/MEATPI-CAN0 can0;
sudo ifconfig can0 txqueuelen 1000
sudo ifconfig can0 up
```
![image](https://github.com/meatpiHQ/meatpi_ollie_v2/assets/94690098/69572d6c-7aaf-45c8-9560-8890385540b1)


**Speed commands:**
```
s1: 20 KBit
s2: 50 KBit
s3: 100 KBit
s4: 125 KBit
s5: 250 KBit
s6: 500 KBit
s7: 800 KBit
s8: 1 MBit
```

# 3. CAN

## CAN on Windows

You can use BUSMaster for CAN Bus monitoring. Please download this version of BUSMaster provided in the [**Link**](https://drive.google.com/drive/folders/1ZuAvOhjXHvq5TKOJofSgyZFOzkQ3mTIc) above. Here is how to setup the hardware. 
1. Select VSCom CAN-API by clicking on 'Driver Selection -> VSCom CAN-API"
2. Then Click on 'Channel Configuration -> Advanced' 
3. Click on 'Search for Devices on COM-Ports', the device should appear in the drop downlist or fill the right COM port number
4. Check the 'Hardware Timestamps' check box.
5. Choose the Baudrate.
6. Click 'OK', then Click the Connect button on the top left corner.

![image](https://user-images.githubusercontent.com/94690098/152467965-3bc36968-4de3-470f-bf0e-b39237e86d7f.png)

<img width="1616" alt="image" src="https://github.com/meatpiHQ/meatpi_ollie_v2/assets/94690098/6f051221-9399-4506-aaf2-fc3cd611fe5f">

## CAN on Linux

SocketCAN is a Linux-based socket interface for CAN bus communication. It provides a standardized API for accessing CAN hardware and a set of utilities for working with CAN devices. SocketCAN supports multiple CAN controllers and can handle different types of CAN buses, such as CAN 2.0A and CAN 2.0B.

Follow the [instructions](#linux) to bring up the CAN interface.

**To send a single frame, use the cansend utility:**
```
cansend can0 123#1122334455667788
```

**To display in real-time the list of messages received on the bus, use the candump utility:**
```
candump can0

# can0  123   [8] 11 22 33 44 55 66 77 88
```

