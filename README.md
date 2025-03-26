<img width="130" align="right" alt="SHU Logo 2020 White (PNG)" src="https://github.com/user-attachments/assets/cd92fa07-8bc7-4f2f-bf84-a638a6b43400" />

# SmartPulse Hackathon: Sample Project Code & Guides #
## For SmartPulse Event at Sheffield Hallam University 2025 ##

------------------------------------------------------------------------

Event Registration: https://cloudeventhallam.azurewebsites.net

### Documentation and Instructions

#### Contents ####
- [Main Guide](#main-guide)
	- [Development Environment Setup Guide](#ide)
	- [General Components Guide](#components)
- [Sensor Data: Instructions](#sensors)
- [Connectivity & Telemetry: Instructions](#connectivity)
- [AI & Quantum AI: Instructions](#ai)

<hr>

<a name="main-guide"></a>
## Main Guide ## 

<img alt="Raspberry Pi" src="https://github.com/user-attachments/assets/d00dedce-6144-4f70-97ba-37ff5d37f02c" width="160"  align="right" title="Raspberry Pi">

> **Main Guide and Information: [Click Here](https://docs.google.com/document/d/1h2tSAFmBCm0hM_lOdg1HRMtnkMllKK4zkzNJHammD90/edit?usp=sharing)**

#### Getting Started with the Raspberry Pi: Development Environment Setup #### 
<a name="ide"></a>
> Development Environment Setup Guide: [Click Here](https://docs.google.com/document/d/1jmaNj-k2K4R65ugP0UThR2z19vqf1rHVt7KjEG5m96I/edit?usp=sharing)

<img alt="Components" src="https://github.com/user-attachments/assets/f163dacd-8877-4642-9828-9d23181afba6" width="160"  align="right" title="Components">

#### Getting Started with Components: LEDs, Buttons and Buzzers #### 
<a name="components"></a>	
> General Components Guide: [Click Here](https://docs.google.com/document/d/1bQy9SwE5os6BgZdQBHF2C5bPazwguYxDTPrudjNQedw/edit?usp=sharing)
> - Code:
>   - [led.py](https://github.com/jzasjam/SmartPulse/blob/main/led.py)
>   - [leds.py](https://github.com/jzasjam/SmartPulse/blob/main/leds.py)
>   - [button.py](https://github.com/jzasjam/SmartPulse/blob/main/button.py)
>   - [buzzer.py](https://github.com/jzasjam/SmartPulse/blob/main/buzzer.py)
	
						
#### Additional Guides ####						
> Prerequiste: Enable I2C: [Click Here](https://docs.google.com/document/d/1JRxyUlNvq2x4ubRcfUsW9In6IapMQ2u75k20n_KrV7U/edit?usp=sharing)

<hr>

<a name="sensors"></a>						
## Sensor Data: Instructions ##		

### Smartphone Sensors ###
<hr />
<img alt="IoT Plug and Play App" src="https://github.com/user-attachments/assets/4ba6e5b3-0218-486d-b800-0d326f00fd3f" width="100" height="100" align="right" title="IoT Plug and Play App">	

> **Smartphone Sensors using IoT Plug and Play App with Azure IoT Central**:				
> - Guide: [Click Here](https://docs.google.com/document/d/1VvCn1_FQEbctKMBPlPAQlDBcCUF5senFn6JRook7AXY/edit?usp=sharing)

> **Smartphone Sensors using IoT Plug and Play App with Azure IoT Hub**:				
> - Guide: [Click Here](https://docs.google.com/document/d/1mOtLjyq3uH9ogB4_wfchXunXJzlT-LO3Lds4zGW32-s/edit?usp=sharing)

### Raspberry Pi Sensors ###
<hr />
<img alt="Raspberry Pi Sense HAT" src="https://github.com/user-attachments/assets/901aa1bf-4020-4f2a-827b-8dfe29b84fbf"  height="100" align="right" title="Raspberry Pi Sense HAT">

> **Raspberry Pi with Sense HAT (v1)**:				
> - Guide: [Click Here](https://docs.google.com/document/d/13ptuQTUtOxBacALn7Yy3yemlTiUr5nOWhpdBOQgNvVU/edit?usp=sharing)
> - Code:
>   - [sense-hat.py](https://github.com/jzasjam/SmartPulse/blob/main/sense-hat.py)
>   - [sense-hat-temperature.py](https://github.com/jzasjam/SmartPulse/blob/main/sense-hat-temperature.py)
>   - [sense-hat-movement.py](https://github.com/jzasjam/SmartPulse/blob/main/sense-hat-movement.py)
>   - [sense-hat-joystick.py](https://github.com/jzasjam/SmartPulse/blob/main/sense-hat-joystick.py)

<img alt="ADAHT20" src="https://github.com/user-attachments/assets/ab0d915f-3a7f-4725-a150-9a68cb0ebbbf" width="100" height="100" align="right" title="Adafruit Humidity and Temperature Sensor">

> **Raspberry Pi with Adafruit Humidity and Temperature Sensor (ADAHT20)**:
> - Guide: [Click Here](https://docs.google.com/document/d/1q9Mn6okB59EjFA-D6o8bpfACr_5ZRMQfcBKuUNrUeCo/edit?usp=sharing)
> - Code: [temperature-sensor.py](https://github.com/jzasjam/SmartPulse/blob/main/temperature-sensor.py)

<img alt="DHT11" src="https://github.com/user-attachments/assets/71300b8c-3b38-4367-bf6c-1758a5d258f1" width="100" height="100" align="right" title="SEEED Studio: Grove Humidity and Temperature Sensor">

> **Raspberry Pi with SEEED Studio: Grove Humidity and Temperature Sensor (DHT11)**:
> - Guide: [Click Here](https://docs.google.com/document/d/1KP89QAXnRT4FUmtGB9H-a_4nPYdvFMehES3DNc0jgts/edit?usp=sharing)
> - Code: [temperature-sensor-dht.py](https://github.com/jzasjam/SmartPulse/blob/main/temperature-sensor-dht.py)

<img alt="Passive Infrared Sensor (PIR)" src="https://github.com/user-attachments/assets/41dab954-82e5-413a-b6db-6f6d05ce12ea" width="100" height="100" align="right" title="Passive Infrared Sensor (PIR)">

> **Raspberry Pi with Passive Infrared Sensor (PIR)**:				
> - Guide: [Click Here](https://docs.google.com/document/d/12ccI9a_OaWbOzyINU06lQ8e-NfbL6guI5kzrAqWuGmY/edit?usp=sharing)
> - Code: [pir-sensor.py](https://github.com/jzasjam/SmartPulse/blob/main/pir-sensor.py)		

<img alt="Ultrasonic Sensor" src="https://github.com/user-attachments/assets/d50f8246-ac79-4360-b7f8-842d411eb55e" width="100" height="100" align="right" title="Ultrasonic Sensor">

> **Raspberry Pi with Ultrasonic Sensor**:				
> - Guide: [Click Here](https://docs.google.com/document/d/1LFmeR4MW0x95G2gXib5MCCFvxkdLgvzbtz5cIqTLBBU/edit?usp=sharing)
> - Code:		
>   - [ultrasonic-sensor.py](https://github.com/jzasjam/SmartPulse/blob/main/ultrasonic-sensor.py)
>   - [ultrasonic-range.py](https://github.com/jzasjam/SmartPulse/blob/main/ultrasonic-range.py)

<img alt="Light Dependent Resistor (LDR)" src="https://github.com/user-attachments/assets/13880517-6d10-4de9-8f53-69d2a401b8a5" width="100" height="100" align="right" title="Light Dependent Resistor (LDR)">

> **Raspberry Pi with Light Dependent Resistor (LDR)**:
> - Guide: [Click Here](https://docs.google.com/document/d/1BZ9h3itdNL1fafVchF0Yqr2M9nRScyOUUsq_iEsDIg8/edit?usp=sharing)
> - Code:
>   - [ldr-sensor.py](https://github.com/jzasjam/SmartPulse/blob/main/ldr-sensor.py)	
>   - [ldr-detect.py](https://github.com/jzasjam/SmartPulse/blob/main/ldr-detect.py)	

<img alt="ArduCam Camera Module" src="https://github.com/user-attachments/assets/6f1cb431-70cb-46f0-96c8-d6e2ce1f9ac5" width="100" height="100" align="right" title="ArduCam Camera Module">

> **Raspberry Pi with ArduCam Camera Module (IMX519)**:
> - Guide: [Click Here](https://docs.google.com/document/d/19jREjWQucDR-Hfd1bmhLBKL5-f6aVjP2qORzBUASdYg/edit?usp=sharing)
> - Code: [camera.py](https://github.com/jzasjam/SmartPulse/blob/main/camera.py)		

<img alt="Raspberry Pi Camera Module 2" src="https://github.com/user-attachments/assets/9e6a2c97-3ac7-4b58-8b49-28ade104e3a6" width="100" height="100" align="right" title="Raspberry Pi Camera Module 2">

> **Raspberry Pi with Raspberry Pi Camera Module 2**: 		 				
> - Guide: [Click Here](https://docs.google.com/document/d/1Lh6dk54YybdQqOixGRdndgKgeBCrPigRjAdf0qV1sVA/edit?usp=sharing)
> - Code: [pi-camera.py](https://github.com/jzasjam/SmartPulse/blob/main/pi-camera.py)

<img name="microbit" alt="BBC micro:bit" src="https://github.com/user-attachments/assets/55c8aec2-16e5-47d3-abc2-64e100d81a0c" width="100" height="100" align="right" title="BBC micro:bit">	

> **Raspberry Pi with BBC micro:bits**:
> - Guide: [Click Here](https://docs.google.com/document/d/1DOTJJ8Ztku1zXKStiMSjb6GC3Nsa7z47r-OVNEnim-Y/edit?usp=sharing)
> - Code:
>   - [pi-microbit.py](https://github.com/jzasjam/SmartPulse/blob/main/pi-microbit.py)
>   - [pi-microbit-leds.py](https://github.com/jzasjam/SmartPulse/blob/main/pi-microbit-leds.py)
>   - [microbit-pi.py](https://github.com/jzasjam/SmartPulse/blob/main/microbit-pi.py)
>   - [microbit-microbit.py](https://github.com/jzasjam/SmartPulse/blob/main/microbit-microbit.py)

<hr>
				

<a name="connectivity"></a>
## Connectivity & Telemetry: Instructions ##		

> **Send Raspberry Pi Sensor Data to Azure IoT Hub**:				
> - Guide: [Click Here](https://docs.google.com/document/d/1-7GcfvMf7TattVU4k1VQWgt8_OgCBw0K0rvVugQgUp4/edit?usp=sharing) [DOCS UNDER CONSTRUCTION]
> - Code: **COMING SOON!!!**

> **Send Raspberry Pi Sensor Data to Azure IoT Central**:	
> - Guide: [Click Here](https://docs.google.com/document/d/1SXGpHs6pJBztK406Afxh9otCrv8vcIZBztuNE_M1XKY/edit?usp=sharing)
> - Code: [sense-hat-iotc.py](https://github.com/jzasjam/SmartPulse/blob/main/sense-hat-iotc.py)		

> **Send Raspberry Pi Simulator Data to Azure IoT Hub**:
> - Guide: **COMING SOON!!!**
> - Code: **COMING SOON!!!**	

<hr>		
		
<a name="ai"></a>				
## AI & Quantum AI: Instructions ##		

> **AI Image Recognition with Raspberry Pi**:					
> - Guide: [Click Here](https://docs.google.com/document/d/18lxfKNw0muigpo9Zrlt7ftIjcAVM_QId8fccoZ-JewQ/edit?usp=sharing)
> - Code:
>   - [camera-ai.py](https://github.com/jzasjam/SmartPulse/blob/main/camera-ai.py)
>   - [camera-ai-leds.py](https://github.com/jzasjam/SmartPulse/blob/main/camera-ai-leds.py)


> **AI Motion Recognition with micro:bits and Raspberry Pi**:
> - Guide: [Click Here](https://docs.google.com/document/d/1DOTJJ8Ztku1zXKStiMSjb6GC3Nsa7z47r-OVNEnim-Y/edit?usp=sharing)
> - Code: [Click Here](#microbit)	

> **Qiskit with Raspberry Pi**:					
> Note: This only works with Raspbian v12 Bookworm			
> - Guide: [Click Here](https://docs.google.com/document/d/1qPg0w-bKS8jj-LoZmW2UQyQBSruR_vP8OgudmfjIrR4/edit?usp=sharing) [DOCS UNDER CONSTRUCTION]
> - Code: [qiskit-pi](https://github.com/jzasjam/SmartPulse/tree/main/qiskit-pi)


------------------------------------------------------------------------------------------

*Documentation and examples prepared by Jonathan Zasada-James at Sheffield Hallam University (2025)*
