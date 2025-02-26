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

Sketch
============================

In this section, the 74HC595 is used in the same way as in the previous section, but with different values transferred. We can learn how to master the digital display by sending the coded value of "0" - "F".

Sketch_1_Dight_7-Segment_Display
----------------------------------------

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_05.png
    :align: center

Verify and upload the code, and you'll see a 1-bit, 7-segment display displaying 0-f in a loop.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_06.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.1_1_Digit_7-Segment_Display/Sketch_14.1_1_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 1-39
    :dedent:

First, put encoding of "0"- "F" into the array.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.1_1_Digit_7-Segment_Display/Sketch_14.1_1_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 10-14
    :dedent:

Then, in the loop, we transfer the member of the "num" to 74HC595 by calling the writeData function, so that the digital tube displays what we want. After each display, "0xff" is used to eliminate the previous effect and prepare for the next display.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.1_1_Digit_7-Segment_Display/Sketch_14.1_1_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 23-30
    :dedent:

In the shiftOut() function, whether to use LSBFIRST or MSBFIRST as the parameter depends on the physical situation.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.1_1_Digit_7-Segment_Display/Sketch_14.1_1_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 32-39
    :dedent:

If you want to display the decimal point, make the highest bit of each array become 0, which can be implemented easily by num[i]&0x7f.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.1_1_Digit_7-Segment_Display/Sketch_14.1_1_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 36-36
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

Sketch
============================

In this code, we use the 74HC595 IC chip to control the 4-digit 7-segment display, and use the dynamic scanning method to show the changing number characters.

Sketch_4_Dight_7-Segment_Display
------------------------------------------

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_12.png
    :align: center

Compile and upload code to ESP8266, then the digital tube displays as shown.

.. image:: ../_static/imgs/14_74HC595_&_7-Segment_Display/Chapter14_13.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 1-54
    :dedent:

First, define the pin of 74HC595 and 7-segment display common end, character encoding.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 7-14
    :dedent:

Second, initialize all the pins to output mode.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 16-24
    :dedent:

Then, since there are four digital tubes, we need to write a subfunction to control it to turn ON any digital tube. In order not to affect a new display, each time we want to turn ON a digital tube, we need to set the other digital tube OFF.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 38-45
    :dedent:

The usage of the writeData function is the same as in the previous two sections, so it won't be covered again here. 

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 47-54
    :dedent:

In the loop function, because there are four digital tubes, a "for loop" is used to display the values of each one in turn. For example, when i =0, turn ON the first digital tube to display the first value, then turn ON the second digital tube to display the second value, until all four digital tubes display their own values. Because the displaying time from the first number to the fourth number is so short, it may display many times in one second, but our eyes can't keep up with the speed of the digital tube, so we look as if the digital tube is displaying different Numbers at the same time.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 26-36
    :dedent:

If you want to display the decimal point, make the highest bit of each array become 0, which can be implemented easily by num[i]&0x7f.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_14.2_4_Digit_7-Segment_Display/Sketch_14.2_4_Digit_7-Segment_Display.ino
    :linenos: 
    :language: c
    :lines: 51-51
    :dedent: