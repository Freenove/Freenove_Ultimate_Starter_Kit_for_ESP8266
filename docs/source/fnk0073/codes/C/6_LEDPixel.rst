##############################################################################
Chapter 6 LEDPixel
##############################################################################

This chapter will help you learn to use a more convenient RGB LED lamp, which requires only one GPIO control and can be connected in infinite series in theory. Each LED can be controlled independently.

Project 6.1 LEDPixel
***************************

Learn the basic usage of LEDPixel and use it to flash red, green, blue and white.

Component List
=========================

.. table::
    :width: 80%
    :align: center
    :class: table-line
    
    +----------------------------------+---------------------+
    | ESP8266 x1                       | USB cable           |
    |                                  |                     |
    | |Chapter01_00|                   | |Chapter01_01|      |
    +----------------------------------+---------------------+
    | Breadboard x1                                          |
    |                                                        |
    | |Chapter01_02|                                         |
    +----------------------------------+---------------------+
    | Freenove 8 RGB LED Module x1     | Jumper wire F/M x4  |
    |                                  |                     |
    | |Chapter06_00|                   | |Chapter06_01|      |
    +----------------------------------+---------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter06_00| image:: ../_static/imgs/6_LEDPixel/Chapter06_00.png
.. |Chapter06_01| image:: ../_static/imgs/6_LEDPixel/Chapter06_01.png

Related knowledge
============================

Freenove 8 RGB LED Module
-------------------------------

The Freenove 8 RGB LED Module is as below. 

It consists of 8 WS2812, each of which requires only one pin to control and supports cascade. Each WS212 has integrated 3 LEDs, red, green and blue respectively, and each of them supports 256-level brightness adjustment, which means that each WS2812 can emit 2^24=16,777,216 different colors.

You can use only one data pin to control eight LEDs on the module. As shown below:

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_02.png
    :align: center

And you can also control many modules at the same time. Just connect OUT pin of one module to IN pin of another module. In this way, you can use one data pin to control 8, 16, 32 … LEDs.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_03.png
    :align: center

:orange:`Pin description:` 

.. table::
    :align: center
    :class: zebra text-center
    
    +---------------------------------------+---------------------------------------+
    |                 (IN)                  | (OUT)                                 |
    +========+==============================+========+==============================+
    | symbol | Function                     | symbol | Function                     |
    +--------+------------------------------+--------+------------------------------+
    | S      | Input control signal         | S      | Output control signal        |
    +--------+------------------------------+--------+------------------------------+
    | V      | Power supply pin, +3.5V~5.5V | V      | Power supply pin, +3.5V~5.5V |
    +--------+------------------------------+--------+------------------------------+
    | G      | GND                          | G      | GND                          |
    +--------+------------------------------+--------+------------------------------+

Circuit
===========================

This circuit is the same as the one in engineering Blink.

.. list-table:: 
   :width: 80%
   :align: center
   :class: table-line

   * -  Schematic diagram
   * -  |Chapter06_04|
   * -  Hardware connection 
     
        :combo:`red font-bolder:If you need any support, please feel free to contact us via:` support@freenove.com

   * -  |Chapter06_05|

.. |Chapter06_04| image:: ../_static/imgs/6_LEDPixel/Chapter06_04.png
.. |Chapter06_05| image:: ../_static/imgs/6_LEDPixel/Chapter06_05.png

Sketch
============================

This code uses a library named "Adafruit_NeoPixel", if you have not installed it, please do so first.

Library is an important feature of the open source world, and we know that Arduino is an open source platform that everyone can contribute to. Libraries are generally licensed under the LGPL, which means you can use them for free to apply to your creations.

How to install the library
--------------------------------

There are two ways to add libraries.

The first way, open the Arduino IDE, click Tools **->** Manager Libraries.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_06.png
    :align: center

In the pop-up window, Library Manager, search for the name of the Library, "Adafruit_NeoPixel". Then click Install.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_07.png
    :align: center

The second way, open Arduino IDE, click Sketch **->** Include Library **->** Add .ZIP Library, In the pop-up window, find the file named "./Libraries/Adafruit_NeoPixel.Zip" which locates in this directory, and click OPEN.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_08.png
    :align: center

Upload following sketch:

**Freenove_Ultimate_Starter_Kit_for_ESP8266\\C\\Sketches\\Sketch_06.1_LEDPixel**

Sketch_06.1_LEDPixel
-------------------------------

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_09.png
    :align: center

Download the code to ESP8266 and RGB LED begins to light up in red, green, blue, white and black.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_10.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 1-37
    :dedent:

To use some libraries, first you need to include the library's header file.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 8-8
    :dedent:

Define the pins connected to the ring and the number of LEDs on the ring.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 9-11
    :dedent:

Use the above parameters to create a LEDPixel object strip.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 16-16
    :dedent:

Define the color values to be used, as red, green, blue, white, and black.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 18-18
    :dedent:

Define a time interval for each LED to light up.The smaller the value is, the faster it will light up.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 17-17
    :dedent:

Initialize strip() in setup() and set the brightness.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 21-22
    :dedent:

In the loop(), there are two "for" loops, the internal for loop to light the LED one by one, and the external for loop to switch colors. pixels.setPixelColor() is used to set the color, but it does not change immediately. Only when pixels.show() is called will the color data be sent to the LED to change the color.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.1_LEDPixel/Sketch_06.1_LEDPixel.ino
    :linenos: 
    :language: c
    :lines: 28-36
    :dedent:

Reference
--------------------------

.. py:function:: pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);	
    
    Constructor to create a LEDPixel object.
    
    Before each use of the constructor, please add "#include <Adafruit_NeoPixel.h>"
    
    Parameters
    
    NUMPIXELS: The number of led.
    
    PIN: A pin connected to an led.
    
    NEO_GRB: 
    
    NEO_GRB: The sequence of LEDPixel module loading color is green, red and blue.

.. py:function:: void begin(void);	
    
    Initialize the LEDPixel object

.. py:function:: void setLedColorData (u8 index, u8 r, u8 g, u8 b);
.. py:function:: void setLedColorData (u8 index, u32 rgb);
.. py:function:: void setLedColor (u8 index, u8 r, u8 g, u8 b);
.. py:function:: void setLedColor (u8 index, u32 rgb);	
    
    Set the color of led with order number n.

.. py:function:: void show(void);	
    
    Send the color data to the led and display the set color immediately.

.. py:function:: void setBrightness(uint8_t);	
    
    Set the brightness of the LED.

.. _c_rainbow:

Project 6.2 Rainbow Light
*********************************

In the previous project, we have mastered the use of LEDPixel. This project will realize a slightly complicated rainbow light. The component list and the circuit are exactly the same as the project fashionable light.

Sketch
==========================

Continue to use the following color model to equalize the color distribution of the 8 LEDs and gradually change.  

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_06.png
    :align: center

Upload following sketch:

**Freenove_Ultimate_Starter_Kit_for_ESP8266\\C\\Sketches\\Sketch_06.2_RainbowLight**

Sketch_06.2_RainbowLight
------------------------------

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_11.png
    :align: center

Download the code to ESP8266, and the Freenove 8 RGB LED Strip displays different colors and the color changes gradually.

.. image:: ../_static/imgs/6_LEDPixel/Chapter06_12.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.2_RainbowLight/Sketch_06.2_RainbowLight.ino
    :linenos: 
    :language: c
    :lines: 1-35
    :dedent:

In the loop(), two "for" loops are used, the internal "for" loop(for-j) is used to set the color of each LED, and the external "for" loop(for-i) is used to change the color, in which the self-increment value in i+=1 can be changed to change the color step distance. Changing the delay parameter changes the speed of the color change. Wheel(i * 256 / LEDS_COUNT + j) & 255) will take color from the color model at equal intervals starting from i.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_06.2_RainbowLight/Sketch_06.2_RainbowLight.ino
    :linenos: 
    :language: c
    :lines: 16-22
    :dedent: