##############################################################################
Chapter Serial Communication
##############################################################################

Serial Communication is a means of communication between different devices/devices. This section describes ESP8266's Serial Communication.

Project Serial Print
***********************************

This project uses ESP8266's serial communicator to send data to the computer and print it on the serial monitor.

Component List
==========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  ESP8266 x1
     -  USB cable
   
   * -  |Chapter00_00|
     -  |Chapter00_01| 

.. |Chapter00_00| image:: ../_static/imgs/0_LED/Chapter00_00.png
.. |Chapter00_01| image:: ../_static/imgs/0_LED/Chapter00_01.png

Related knowledge
=============================

Serial communication
------------------------------

Serial communication generally refers to the Universal Asynchronous Receiver/Transmitter (UART), which is commonly used in electronic circuit communication. It has two communication lines, one is responsible for sending data (TX line) and the other for receiving data (RX line). The serial communication connections of two devices is as follows:

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_00.png
    :align: center

Before serial communication starts, the baud rate of both sides must be the same. Communication between devices can work only if the same baud rate is used. The baud rates commonly used is 9600 and 115200.

Serial port on ESP8266
------------------------------

Freenove ESP8266 has integrated USB to serial transfer, so it could communicate with computer connecting to USB cable.

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_01.png
    :align: center

Arduino Software also uploads code to Freenove ESP8266 through the serial connection.

Your computer identifies serial devices connecting to it as COMx. We can use the Serial Monitor window of Arduino Software to communicate with Freenove ESP8266, connect Freenove ESP8266 to computer through the USB cable, choose the correct device, and then click the Serial Monitor icon to open the Serial Monitor window. 

Interface of serial monitor window is as follows. If you can't open it, make sure Freenove ESP8266 has been connected to the computer, and choose the right serial port in the menu bar "Tools".

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_02.png
    :align: center

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_03.png
    :align: center

When the ESP8266 is powered on, the default baud rate is 74880. The default communication and serial port in the ESP8266 firmware is 115200. So if you set the serial port to 74880, this time can be displayed normally.

If the baud rate is not 74880, some garbled characters will appear. Please do not worry.

Here, we use The Arduino IDE serial port tool for output and display. The details are as follows: 

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_04.png
    :align: center

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_05.png
    :align: center
    
Garbled characters are displayed when you set the baud rate to another value as follows: 

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_06.png
    :align: center

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_07.png
    :align: center

Circuit
==========================

Connect Freenove ESP8266 to the computer with USB cable.

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_08.png
    :align: center

Sketch
===========================

Sketch_SerialPrinter
----------------------------

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_09.png
    :align: center

Download the code to ESP8266, open the serial port monitor, set the baud rate to 74880, and press the reset button. As shown in the following figure:

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_10.png
    :align: center

As shown in the image above, "ESP8266 initialization completed! " The previous is the printing message when the system is started, it uses the baud rate of 120,000, which is incorrect, so the garbled code is displayed. The user program is then printed at a baud rate of 74880.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_08.1_SerialPrinter/Sketch_08.1_SerialPrinter.ino
    :linenos: 
    :language: c
    :lines: 1-16
    :dedent:

Reference
-------------------------------

.. py:function:: void begin(unsigned long baud, uint32_t config=SERIAL_8N1, int8_t rxPin=-1, int8_t txPin=-1, bool invert=false, unsigned long timeout_ms = 20000UL);	
    
    Initializes the serial port. Parameter baud is baud rate, other parameters generally use the default value.

.. py:function:: size_t println( arg );	
    
    Print to the serial port and wrap. The parameter arg can be a number, a character, a string, an array of characters, etc.

.. py:function:: size_t printf(const char * format, ...)  __attribute__ ((format (printf, 2, 3)));	
    
    Print formatted content to the serial port in the same way as print in standard C.

.. py:function:: unsigned long millis();	

    Returns the number of milliseconds since the current system was booted.

Project Serial Read and Write
**************************************

From last section, we use serial port on Freenove ESP8266 to send data to a computer, now we will use that to receive data from computer.

Component and circuit are the same as in the previous project.

Sketch
=================================

Sketch_SerialRW
-----------------------------

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_11.png
    :align: center

Download the code to ESP8266, open the serial monitor, and set the bottom to Newline, 74880. As shown in the following figure:

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_12.png
    :align: center

Then type characters like 'ABCDEG' into the data sent at the top and click the Send button to print out the data ESP8266 receives.  

.. image:: ../_static/imgs/8_Serial_Communication/Chapter08_13.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_08.1_SerialPrinter/Sketch_08.1_SerialPrinter.ino
    :linenos: 
    :language: c
    :lines: 1-30
    :dedent:

In loop(), determine whether the serial port has data, if so, read and save the data, and if the newline character is read, print out all the data that has been read.

Reference
---------------------------

.. py:function:: String();	
    
    Constructs an instance of the String class.
    
    For more information, please visit
    
    https://www.arduino.cc/reference/en/language/variables/data-types/stringobject/

.. py:function:: int available(void);	
    
    Get the number of bytes (characters) available for reading from the serial port. This is data that’s already arrived and stored in the serial receive buffer.
    
.. py:function:: Serial.read();	
    
    Reads incoming serial data.