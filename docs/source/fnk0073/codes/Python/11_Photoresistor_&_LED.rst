##############################################################################
Chapter Photoresistor & LED
##############################################################################

In this chapter, we will learn how to use a photoresistor.

Project NightLamp
*********************************

A photoresistor is very sensitive to the amount of light present. We can take advantage of the characteristic to make a nightlight with the following function: when the ambient light is less (darker environment) the LED will automatically become brighter to compensate and when the ambient light is greater (brighter environment) the LED will automatically dim to compensate.

Component List
=============================

+----------------------------------+-------------------------------+
| ESP8266 x1                       |          USB cable            |
|                                  |                               |
| |Chapter01_00|                   |          |Chapter01_01|       |
+----------------------------------+-------------------------------+
| Breadboard x1                                                    |
|                                                                  |
| |Chapter01_02|                                                   |
+----------------------------------+-------------------------------+
| Photoresistor x1                 | Jumper wire M/M x7            |
|                                  |                               |
| |Chapter11_00|                   |          |Chapter01_05|       |
+----------------+-----------------+-------------------------------+
|Resistor 220Ω x1| Resistor 10kΩ x1| LED x1                        |
|                |                 |                               |
| |Chapter01_04| | |Chapter11_01|  |          |Chapter01_03|       |
+----------------+-----------------+-------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_03| image:: ../_static/imgs/1_LED/Chapter01_03.png
.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter11_00| image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_00.png
.. |Chapter11_01| image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_01.png

Component knowledge
================================

Photoresistor 
----------------------------

A photoresistor is simply a light sensitive resistor. It is an active component that decreases resistance with respect to receiving luminosity (light) on the component's light sensitive surface. A photoresistor’s resistance value will change in proportion to the ambient light detected. With this characteristic, we can use a photoresistor to detect light intensity. The photoresistor and its electronic symbol are as follows.

.. image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_02.png
    :align: center

The circuit below is used to detect the change of a photoresistor's resistance value:

.. image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_03.png
    :align: center

In the above circuit, when a photoresistor's resistance vale changes due to a change in light intensity, the voltage between the photoresistor and resistor R1 will also change. Therefore, the intensity of the light can be obtained by measuring this voltage.

Circuit
============================

The circuit of this project is similar to project Soft Light. The only difference is that the input signal is changed from a potentiometer to a combination of a photoresistor and a resistor.

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter11_04|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter11_05|

.. |Chapter11_04| image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_04.png
.. |Chapter11_05| image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_05.png

Sketch
==============================

Move the program folder "Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes" to disk(D) in advance with the path of "D:/Micropython_Codes".

Codes of this project is logically the same as the project Soft Light.

Nightlamp
---------------------------

.. image:: ../_static/imgs/11_Photoresistor_&_LED/Chapter11_07.png
    :align: center

Click "Run current script". Cover the photoresistor with your hands or illuminate it with lights, the brightness of LEDs will change.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/11.1_NightLamp/NightLamp.py
    :linenos: 
    :language: python
    :lines: 1-14
    :dedent: