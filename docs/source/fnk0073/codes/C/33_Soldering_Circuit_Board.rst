##############################################################################
Chapter 33 Soldering Circuit Board
##############################################################################

Project 33.1 Soldering a Buzzer
***************************************

We have tried to use a buzzer in a previous chapter, and now we will solder a circuit that when the button is pressed, the buzzer sounds.

This circuit does not need programming and can work when it is powered on. And when the button is not pressed, there is no power consumption.

You can install it on your bike, bedroom door or any other places where it is needed.

Component List
===============================

.. table::
    :width: 80%
    :align: center
    :class: table-line
    
    +----------------------+----------------+------------------+------------------+----------------+
    | Pin header x2        | LED x1         | Resistor 220Ω x1 | Active buzzer x1 | Push button x1 |
    |                      |                |                  |                  |                |
    | |Chapter33_00|       | |Chapter33_01| | |Chapter33_02|   | |Chapter33_03|   | |Chapter33_04| |
    +----------------------+----------------+------------------+------------------+----------------+
    | AA Battery Holder x1                                                                         |
    |                                                                                              |
    | |Chapter33_05|                                                                               |
    +----------------------------------------------------------------------------------------------+

.. |Chapter33_00| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_00.png
.. |Chapter33_01| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_01.png
.. |Chapter33_02| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_02.png
.. |Chapter33_03| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_03.png
.. |Chapter33_04| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_04.png
.. |Chapter33_05| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_05.png

Circuit
===============================

We will solder the following circuit on the main board.

.. list-table:: 
   :align: center
   :class: table-line
   :header-rows: 1

   * -  Schematic diagram
     -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   * -  |Chapter33_06|
     -  |Chapter33_07|

.. |Chapter33_06| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_06.png
.. |Chapter33_07| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_07.png

Soldering the Circuit 
================================

Insert the components on the main board and solder the circuit on its back.

.. image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_08.png
    :align: center

rendering after soldering:

.. list-table:: 
   :width: 80%
   :align: center
   :class: table-line

   * -  Front
     -  Back
   * -  |Chapter33_09|
     -  |Chapter33_10|

.. |Chapter33_09| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_09.png
.. |Chapter33_10| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_10.png

Testing circuit
==============================

Connect the circuit board to power supply (3~5V). You can use ESP8266 board or battery box as the power supply.

.. image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_11.png
    :align: center

Press the push button after connecting the power, and then the buzzer will make a sound.

Project 33.2 Soldering a Flowing Water Light
******************************************************

From previous chapter, we have learned to make a flowing water light with LED. Now, we will solder a circuit board, and use the improved code to make a more interesting flowing water light.

Component List
===============================

.. list-table:: 
   :width: 80%
   :align: center
   :class: table-line

   * -  Pin header x5
     -  Resistor 220Ω x8
     -  LED x1 
     -  74HC595 x1
   
   * -  |Chapter33_12|
     -  |Chapter33_13|
     -  |Chapter33_14|
     -  |Chapter33_15|

.. |Chapter33_12| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_12.png
.. |Chapter33_13| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_13.png
.. |Chapter33_14| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_14.png
.. |Chapter33_15| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_15.png

Circuit
============================

Solder the following circuit on the main board.

.. list-table:: 
   :align: center
   :class: table-line
   :header-rows: 1

   * -  Schematic diagram
     -  Hardware connection
    
        If you need any support, please feel free to contact us via: support@freenove.com
   * -  |Chapter33_16|
     -  |Chapter33_17|

.. |Chapter33_16| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_16.png
.. |Chapter33_17| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_17.png

Soldering the Circuit 
===============================

Insert the components on the main board and solder the circuit on its back.

.. image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_18.png
    :align: center

Rendering after soldering:

.. list-table:: 
   :align: center
   :class: table-line

   * -  Front
     -  Back
   * -  |Chapter33_19|
     -  |Chapter33_20|

.. |Chapter33_19| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_19.png
.. |Chapter33_20| image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_20.png

Connecting the Circuit
============================

Connect the board to ESP8266 with Jumper wire in the following way.

.. image:: ../_static/imgs/33_Soldering_Circuit_Board/Chapter33_21.png
    :align: center

Sketch
==========================

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_13.1_FlowingLight02/Sketch_13.1_FlowingLight02.ino
    :linenos: 
    :language: c
    :lines: 1-44
    :dedent:

In fact, this code is copied from chapter 13. If you have any questions for the code, please click ":ref:`Chapter 13 74HC595 & LED Bar Graph <Led_bar>`" to return to Chapter 13 to study again.