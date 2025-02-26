##############################################################################
Preface
##############################################################################

ESP8266 is a micro control unit with integrated Wi-Fi launched by Espressif, which features strong properties and integrates rich peripherals. It can be designed and studied as an ordinary Single Chip Micyoco(SCM) chip, or connected to the Internet and used as an Internet of Things device.

ESP8266 can be developed using the Arduino platform, which will definitely make it easier for people who have learned arduino to master. Moreover, the code of ESP8266 is completely open-source, so beginners can quickly learn how to develop and design IOT smart household products including smart curtains, fans, lamps and clocks.

Generally, ESP8266 projects consist of code and circuits. Don't worry even if you've never learned code and circuits, because we will gradually introduce the basic knowledge of C programming language and electronic circuits, from easy to difficult. Our products contain all the electronic components and modules needed to complete these projects. It's especially suitable for beginners.

We divide each project into four parts, namely Component List, Component Knowledge, Circuit and Code. Component List helps you to prepare material for the experiment more quickly. Component Knowledge allows you to quickly understand new electronic modules or components, while Circuit helps you understand the operating principle of the circuit. And Code allows you to easily master the use of ESP8266 and accessory kit. After finishing all the projects in this tutorial, you can also use these components and modules to make products such as smart household, smart cars and robots to transform your creative ideas into prototypes and new and innovative products.

In addition, if you have any difficulties or questions with this tutorial or toolkit, feel free to ask for our quick and free technical support through support@freenove.com 

ESP8266
**************************************

ESP8266 has PCB on-board antenna. The PCB on-board antenna is an integrated antenna in the chip module itself, so it is convenient to carry and design.

PCB on-board antenna

.. image:: ../_static/imgs/Preface/Preface00.png
    :align: center

In this tutorial, the ESP8266 development board is designed based on the PCB on-board antenna-packaged ESP8266 module. The following tutorials will be based on the ESP8266 development board.

ESP8266 development board

.. image:: ../_static/imgs/Preface/Preface01.png
    :align: center

The hardware interfaces of ESP8266 are distributed as follows:

.. image:: ../_static/imgs/Preface/Preface02.png
    :align: center

Compare the left and right images. We've boxed off the resources on the ESP8266 in different colors to facilitate your understanding of the ESP8266 development board.

.. list-table:: 
   :width: 100%
   :align: center

   * -  Box color 
     -  Corresponding resources introduction
   
   * -  |Preface03|
     -  **GPIO pin**
   
   * -  |Preface04|
     -  **LED indicator**
   
   * -  |Preface05|
     -  **Reset button, Boot mode selection button**
   
   * -  |Preface06|
     -  **USB port**

.. |Preface03| image:: ../_static/imgs/Preface/Preface03.png
.. |Preface04| image:: ../_static/imgs/Preface/Preface04.png
.. |Preface05| image:: ../_static/imgs/Preface/Preface05.png
.. |Preface06| image:: ../_static/imgs/Preface/Preface06.png

+-----+----------+-----------------------------------------------------------------------+
| NO. | Pin Name | Functional Description                                                |
+-----+----------+-----------------------------------------------------------------------+
| 1   | RST      | Reset Pin, Active Low                                                 |
+-----+----------+-----------------------------------------------------------------------+
| 2   | ADC      | AD conversion, Input voltage range 0~3.3V, the value range is 0~1024. |
+-----+----------+-----------------------------------------------------------------------+
| 3   | EN       | Chip Enabled Pin, Active High                                         |
+-----+----------+-----------------------------------------------------------------------+
| 4   | IO16     | Connect with RST pin to wake up Deep Slee                             |
+-----+----------+-----------------------------------------------------------------------+
| 5   | IO14     | GPIO14; HSPI_CLK                                                      |
+-----+----------+-----------------------------------------------------------------------+
| 6   | IO12     | GPIO12; HSPI_MISO                                                     |
+-----+----------+-----------------------------------------------------------------------+
| 7   | IO13     | GPIO13; HSPI_MOSI; UART0_CTS                                          |
+-----+----------+-----------------------------------------------------------------------+
| 8   | VCC      | Module power supply pin, Voltage 3.0V ~ 3.6V                          |
+-----+----------+-----------------------------------------------------------------------+
| 9   | GND      | GND                                                                   |
+-----+----------+-----------------------------------------------------------------------+
| 10  | IO15     | GPIO15; MTDO; HSPICS; UART0                                           |
+-----+----------+-----------------------------------------------------------------------+
| 11  | IO2      | GPIO2; UART1_TXD                                                      |
+-----+----------+-----------------------------------------------------------------------+
| 12  | IO0      | GPIO0; UART1_RXD                                                      |
+-----+----------+-----------------------------------------------------------------------+
| 13  | IO4      | GPIO4                                                                 |
+-----+----------+-----------------------------------------------------------------------+
| 14  | IO5      | GPIO5;IR_R                                                            |
+-----+----------+-----------------------------------------------------------------------+
| 15  | RXD      | UART0_RXD; GPIO3                                                      |
+-----+----------+-----------------------------------------------------------------------+
| 16  | TXD      | UART0_TXD; GPIO1                                                      |
+-----+----------+-----------------------------------------------------------------------+

Description of the ESP8266 series module boot mode:

+---------------+-----------+------+--------+-------+-------+------+
| Mode          | CH_PD(EN) | RST  | GPIO15 | GPIO0 | GPIO2 | TXD0 |
+---------------+-----------+------+--------+-------+-------+------+
| Download mode | high      | high | low    | low   | high  | high |
+---------------+-----------+------+--------+-------+-------+------+
| Running mode  | high      | high | low    | high  | high  | high |
+---------------+-----------+------+--------+-------+-------+------+

Notes: Some of the pins inside the module have been pulled or pulled down.

For more information, please visit: 

https://docs.ai-thinker.com/_media/esp8266/docs/esp-12s_product_specification_en.pdf