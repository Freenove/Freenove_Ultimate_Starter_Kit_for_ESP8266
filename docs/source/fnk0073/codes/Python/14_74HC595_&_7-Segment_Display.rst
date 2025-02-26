##############################################################################
Chapter 74HC595 & 7-Segment Display
##############################################################################

In this chapter, we will introduce the 7-Segment Display.

Project 1-Digit 7-Segment Display.
************************************************

We will use 74HC595 to control 7-segment display and make it display hexadecimal character "0-F".

Component List
============================

+----------------------------------+---------------------------------------+
| ESP8266 x1                       |          USB cable                    |
|                                  |                                       |
| |Chapter01_00|                   |          |Chapter01_01|               |
+----------------------------------+---------------------------------------+
| Breadboard x1                                                            |
|                                                                          |
| |Chapter01_02|                                                           |
+----------------------------------+---------------------------------------+
| 7-segment display x1             | Jumper wire M/M x17                   |
|                                  |                                       |
| |Chapter14_00|                   |  |Chapter01_05|                       |
+----------------------------------+---------------------------------------+
| 74HC595 x1                       | Resistor 220Ω x8                      |
|                                  |                                       |
| |Chapter13_00|                   |  |Chapter01_04|                       |
+----------------------------------+---------------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter13_00| image:: ../_static/imgs/13_74HC595_&_LED_Bar_Graph/Chapter13_00.png
.. |Chapter14_00| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_00.png

Component knowledge
============================

7-segment display
-----------------------------

A 7-segment display is a digital electronic display device. There is a figure "8" and a decimal point represented, which consists of 8 LEDs. The LEDs have a common anode and individual cathodes. Its internal structure and pin designation diagram is shown below:

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_01.png
    :align: center

As we can see in the above circuit diagram, we can control the state of each LED separately. Also, by combining LEDs with different states of ON and OFF, we can display different characters (Numbers and Letters). For example, to display a "0": we need to turn ON LED segments A, B, C, D, E and F, and turn OFF LED segments G and DP.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_02.png
    :align: center

In this project, we will use a 7-Segment Display with a common anode. Therefore, when there is an input low level to a LED segment the LED will turn ON. Defining segment "A" as the lowest level and segment "DP" as the highest level, from high to low would look like this: "DP", "G", "F", "E", "D", "C", "B", "A". Character "0" corresponds to the code: 1100 0000b=0xc0.

For detailed code values, please refer to the following table (common anode). 

+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| CHAR | DP  |  G  |  F  |  E  |  D  |  C  |  B  |  A  | Hex  |   ASCII   |
+======+=====+=====+=====+=====+=====+=====+=====+=====+======+===========+
| 0    | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0xc0 | 1100 0000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 1    | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 0xf9 | 1111 1001 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 2    | 1   | 0   | 1   | 0   | 0   | 1   | 0   | 0   | 0xa4 | 1010 0100 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 3    | 1   | 0   | 1   | 1   | 0   | 0   | 0   | 0   | 0xb0 | 1011 0000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 4    | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 0x99 | 1001 1001 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 5    | 1   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | 0x92 | 1001 0010 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 6    | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0x82 | 1000 0010 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 7    | 1   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0xf8 | 1111 1000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 8    | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0x80 | 1000 0000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| 9    | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0x90 | 1001 0000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| A    | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0x88 | 1000 1000 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| B    | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0x83 | 1000 0011 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| C    | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0xc6 | 1100 0110 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| D    | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0xa1 | 1010 0001 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| E    | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0x86 | 1000 0110 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+
| F    | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 0x8e | 1000 1110 |
+------+-----+-----+-----+-----+-----+-----+-----+-----+------+-----------+

Circuit
===========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter14_03|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter14_04|

.. |Chapter14_03| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_03.png
.. |Chapter14_04| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_04.png

Code
============================

In this section, the 74HC595 is used in the same way as in the previous section, but with different values transferred. We can learn how to master the digital display by sending the code value of "0" - "F".

Move the program folder " **Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes** " to disk(D) in advance with the path of "D:/Micropython_Codes".

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "14.1_74HC595_and_7_segment_display". 

Select "my74HC595.py", right click your mouse to select "Upload to /", wait for "my74HC595.py" to be uploaded to ESP8266 and then double click"74HC595_and_7_segment_display.py". 

74HC595_and_7_segment_display
-------------------------------------------

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_14.png
    :align: center

Click "Run current script", and you'll see a 1-bit, 7-segment display displaying 0-f in a loop.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_15.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.1_74HC595_and_7_segment_display/74HC595_and_7_segment_display.py
    :linenos: 
    :language: python
    :lines: 1-14
    :dedent:

Import time and my74HC595 modules.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.1_74HC595_and_7_segment_display/74HC595_and_7_segment_display.py
    :linenos: 
    :language: python
    :lines: 1-2
    :dedent:

Put the encoding "0" - "F" into the list.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.1_74HC595_and_7_segment_display/74HC595_and_7_segment_display.py
    :linenos: 
    :language: python
    :lines: 4-5
    :dedent:

Define an object, whose pins applys default configuration, to drive 74HC595. 

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.1_74HC595_and_7_segment_display/74HC595_and_7_segment_display.py
    :linenos: 
    :language: python
    :lines: 7-7
    :dedent:

Send data of digital tube to 74HC595 chip.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.1_74HC595_and_7_segment_display/74HC595_and_7_segment_display.py
    :linenos: 
    :language: python
    :lines: 11-11
    :dedent:

Project 4-Digit 7-Segment Display
******************************************

Now, let's try to control more digit 7-segment display

Component List
===============================

+----------------------------------+---------------------------------------+
| ESP8266 x1                       |          USB cable                    |
|                                  |                                       |
| |Chapter01_00|                   |          |Chapter01_01|               |
+----------------------------------+---------------------------------------+
| Breadboard x1                                                            |
|                                                                          |
| |Chapter01_02|                                                           |
+----------------------------------+---------------------------------------+
| 7-segment display x1             | Jumper wire M/M x17                   |
|                                  |                                       |
| |Chapter14_07|                   |  |Chapter01_05|                       |
+----------------------------------+---------------------------------------+
| 74HC595 x1                       | Resistor 220Ω x8                      |
|                                  |                                       |
| |Chapter13_00|                   |  |Chapter01_04|                       |
+----------------------------------+---------------------------------------+

.. |Chapter14_07| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_07.png

Component knowledge
================================

4 Digit 7-Segment Display
------------------------------

A 4 Digit 7-segment display integrates four 7-segment displays into one module, therefore it can display more characters. All of the LEDs contained have a common anode and individual cathodes. Its internal structure and pin designation diagram is shown below:

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_08.png
    :align: center

The internal electronic circuit is shown below, and all 8 LED cathode pins of each 7-segment display are connected together.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_09.png
    :align: center

Display method of 4 digit 7-segment display is similar to 1 digit 7-segment display. The difference between them is that the 4-digit displays each Digit is visible in turn, one by one and not together. We need to first send high level to the common end of the first digit display, and send low level to the remaining three common ends, and then send content to 8 LED cathode pins of the first Digit Display. At this time, the first 7-segment display will show visible content and the remaining three will be OFF.

Similarly, the second, third and fourth 7-segment displays will show visible content in turn by scanning the display. Although the four number characters are displayed in turn separately, this process is so fast that it is imperceptible to the naked eye. This is due to the principle of optical afterglow effect and the vision persistence effect in human sight. This is how we can see all 4 number characters at the same time. However, if each number character is displayed for a longer period, you will be able to see that the number characters are displayed separately. 

Circuit
===========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter14_10|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter14_11|

.. |Chapter14_10| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_10.png
.. |Chapter14_11| image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_11.png

Code
============================

In this code, we use the 74HC595 IC Chip to control the 4-Digit 7-Segment Display, and use the dynamic scanning method to show the changing number characters.

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "14.2_4_Digit_7_Segment_Display". Select "my74HC595.py", right click your mouse to select "Upload to /", wait for "my74HC595.py" to be uploaded to ESP8266 and double click "4_Digit_7_Segment_Display.py". 

4_Digit_7_Segment_Display
------------------------------

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_16.png
    :align: center

Click "Run current script", and the Nixie tube display as shown in the image below.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_17.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.2_4_Digit_7_Segment_Display/4_Digit_7_Segment_Display.py
    :linenos: 
    :language: python
    :lines: 10-19
    :dedent:

Import time, my74HC595 and Pin modules.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.2_4_Digit_7_Segment_Display/4_Digit_7_Segment_Display.py
    :linenos: 
    :language: python
    :lines: 1-3
    :dedent:

Define common anode pins for digital tubes and request a list to put character encodings in it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.2_4_Digit_7_Segment_Display/4_Digit_7_Segment_Display.py
    :linenos: 
    :language: python
    :lines: 5-7
    :dedent:

Request an object to drive 74HC595 and associate pins with it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.2_4_Digit_7_Segment_Display/4_Digit_7_Segment_Display.py
    :linenos: 
    :language: python
    :lines: 18-18
    :dedent:

Make the digital tube display "0123".

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/14.2_4_Digit_7_Segment_Display/4_Digit_7_Segment_Display.py
    :linenos: 
    :language: python
    :lines: 9-15
    :dedent: