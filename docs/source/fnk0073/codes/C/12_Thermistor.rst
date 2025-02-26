##############################################################################
Chapter Thermistor
##############################################################################

In this chapter, we will learn about thermistors which are another kind of resistor

Project Thermometer
*******************************

A thermistor is a type of resistor whose resistance value is dependent on temperature and changes in temperature. Therefore, we can take advantage of this characteristic to make a thermometer.

Component List
==================================

+-------------------------+------------------------------+
| ESP8266 x1              | USB cable                    |
|                         |                              |
| |Chapter01_00|          | |Chapter01_01|               |
+-------------------------+------------------------------+
| Breadboard x1                                          |
|                                                        |
| |Chapter01_02|                                         |
+----------------+------------------+--------------------+
| Thermistor x1  | Resistor 10kΩ x1 | Jumper wire M/M x4 |
|                |                  |                    |
| |Chapter12_00| | |Chapter12_01|   | |Chapter01_05|     |
+----------------+------------------+--------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter12_00| image:: ../_static/imgs/12_Thermistor/Chapter12_00.png
.. |Chapter12_01| image:: ../_static/imgs/12_Thermistor/Chapter12_01.png

Component knowledge
=============================

Thermistor
-----------------------------

A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the resistance of the thermistor will change. We can take advantage of this characteristic by using a thermistor to detect temperature intensity. A thermistor and its electronic symbol are shown below.

.. image:: ../_static/imgs/12_Thermistor/Chapter12_02.png
    :align: center

The relationship between resistance value and temperature of a thermistor is:

.. image:: ../_static/imgs/12_Thermistor/Chapter12_03.png
    :align: center

**Where:**

    Rt is the thermistor resistance under T2 temperature;

    **R** is the nominal resistance of thermistor under T1 temperature;

    **EXP[n]** is nth power of E;

    **B** is for thermal index;

    T1, T2 is Kelvin temperature (absolute temperature). Kelvin temperature=273.15 + Celsius temperature. 

For the parameters of the thermistor, we use: B=3950, R=10k, T1=25.

The circuit connection method of the thermistor is similar to photoresistor, as the following:

.. image:: ../_static/imgs/12_Thermistor/Chapter12_04.png
    :align: center

Circuit
=================================

The circuit of this project is similar to the one in the last chapter. The only difference is that the photoresistor is replaced by the thermistor.

Circuit
============================

The circuit of this project is similar to project Soft Light. The only difference is that the input signal is changed from a potentiometer to a combination of a photoresistor and a resistor.

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter12_05|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter12_06|

.. |Chapter12_05| image:: ../_static/imgs/12_Thermistor/Chapter12_05.png
.. |Chapter12_06| image:: ../_static/imgs/12_Thermistor/Chapter12_06.png

Sketch
===========================

Sketch_Thermometer
---------------------------

.. image:: ../_static/imgs/12_Thermistor/Chapter12_07.png
    :align: center

Download the code to ESP8266, the terminal window will display the current ADC value, voltage value and temperature value. Try to "pinch" the thermistor (without touching the leads) with your index finger and thumb for a brief time, you should see that the temperature value increases.

:red:`If you have any concerns, please contact us via:` support@freenove.com

.. image:: ../_static/imgs/12_Thermistor/Chapter12_08.png
    :align: center

The following is the code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_12.1_Thermometer/Sketch_12.1_Thermometer.ino
    :linenos: 
    :language: c
    :lines: 1-20
    :dedent:

In the code, the ADC value of ADC module A0 port is read, and then calculates the voltage and the resistance of thermistor according to Ohms Law. Finally, it calculates the temperature sensed by the thermistor, according to the formula. 