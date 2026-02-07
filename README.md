# MAX86140 SPI Data Acquisition

This repository demonstrates a **basic implementation for reading data from the MAX86140 sensor using the SPI protocol**. The project focuses on understanding how to configure the sensor, establish SPI communication, and retrieve raw measurement data for further processing.

---

## 📌 Overview

The **MAX86140** is an ultra-low-power, integrated optical sensor designed for **photoplethysmography (PPG)** applications such as heart rate and SpO₂ monitoring. It integrates photodiodes, analog front-end (AFE), and LED drivers in a compact form factor.

This project provides a minimal example of:
- Initializing the MAX86140
- Communicating with the sensor over **SPI**
- Reading raw sensor data frames
- Preparing data for higher-level signal processing

---

## 🛠️ Key Features

- SPI-based register read/write operations
- Sensor configuration via control registers
- Continuous data acquisition from the FIFO
- Hardware-oriented, low-level implementation

---

## 🔌 Communication Protocol

- **Protocol:** SPI  
- **Mode:** Configurable (per MAX86140 datasheet)  
- **Data Type:** Raw PPG samples  

The implementation follows the timing and framing requirements specified in the MAX86140 datasheet.

---

## 🎯 Purpose

This repository is intended for:
- Embedded systems developers
- Students learning sensor interfacing
- Engineers working with biomedical optical sensors


