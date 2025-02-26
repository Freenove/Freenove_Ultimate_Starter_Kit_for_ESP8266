##############################################################################
Chapter Analog & PWM
##############################################################################

In previous study, we have known that one button has two states: pressed and released, and LED has light-on/off state, then how to enter a middle state? How to output an intermediate state to let LED "semi bright"?  That's what we're going to learn.

First, let's learn how to control the brightness of a LED.

Project Breathing LED
************************************

Breathing light, that is, LED is turned from off to on gradually, and gradually from on to off, just like "breathing". So, how to control the brightness of a LED?  We will use PWM to achieve this target.

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
| LED x1         | Resistor 220Ω x1 | Jumper wire M/M x3 |
|                |                  |                    |
| |Chapter01_03| | |Chapter01_04|   | |Chapter01_05|     |
+----------------+------------------+--------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_03| image:: ../_static/imgs/1_LED/Chapter01_03.png
.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png

Related knowledge
=============================

Analog & Digital
-------------------------

An analog signal is a continuous signal in both time and value. On the contrary, a digital signal or discrete-time signal is a time series consisting of a sequence of quantities. Most signals in life are analog signals. A familiar example of an analog signal would be how the temperature throughout the day is continuously changing and could not suddenly change instantaneously from 0℃ to 10℃. However, digital signals can instantaneously change in value. This change is expressed in numbers as 1 and 0 (the basis of binary code). 

Their differences can more easily be seen when compared when graphed as below.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_00.png
    :align: center

In practical application, we often use binary as the digital signal, that is a series of 0’s and 1’s. Since a binary signal only has two values (0 or 1), it has great stability and reliability. Lastly, both analog and digital signals can be converted into the other.

PWM
--------------------------------------------

PWM, Pulse-Width Modulation, is a very effective method for using digital signals to control analog circuits. Common processors cannot directly output analog signals. PWM technology makes it very convenient to achieve this conversion (translation of digital to analog signals)

PWM technology uses digital pins to send certain frequencies of square waves, that is, the output of high levels and low levels, which alternately last for a while. The total time for each set of high levels and low levels is generally fixed, which is called the period (Note: the reciprocal of the period is frequency). The time of high level outputs are generally called "pulse width", and the duty cycle is the percentage of the ratio of pulse duration, or pulse width (PW) to the total period (T) of the waveform.

The longer the outputs of high levels last, the longer the duty cycle and the higher the corresponding voltage in the analog signal will be. The following figures show how the analog signal voltages vary between 0V-5V (high level is 5V) corresponding to the pulse width 0%-100%:

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_01.png
    :align: center

ESP8266 and PWM 
------------------------------------

The ESP8266 PWM controller has 8 independent channels, each of which can independently control frequency, duty cycle, and even accuracy. Unlike traditional PWM pins, the PWM output pins of ESP8266 are configurable and they can be configured to PWM.

The ESP8266 supports PWM pins as follows:

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_02.png
    :align: center

The longer the PWM duty cycle is, the higher the output power will be. Now that we understand this

relationship, we can use PWM to control the brightness of an LED or the speed of DC motor and so on.

Circuit
===========================

This circuit is the same as the one in engineering Blink.

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter04_03|
   * -  Hardware connection 
     
        If you need any support, please feel free to contact us via: support@freenove.com

   * -  |Chapter04_04|

.. |Chapter04_03| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_03.png
.. |Chapter04_04| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_04.png

Code
============================

This project is designed to make PWM output GPIO4 with pulse width increasing from 0% to 100%, and then reducing from 100% to 0% gradually.

Move the program folder " **Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes** " to disk(D) in advance with the path of "D:/Micropython_Codes".

Open "Thonny", click"This computer" -> "D:" -> "Micropython_Codes" -> "04.1_BreatheLight" and double click "BreatheLight.py". 

04.1_BreatheLight
------------------------------

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_11.png
    :align: center

Click "Run current script", and you'll see that LED is turned from ON to OFF and then back from OFF to ON gradually like breathing.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_12.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.1_BreatheLight/BreatheLight.py
    :linenos: 
    :language: python
    :lines: 1-15
    :dedent:

The way that the ESP8266 PWM pins output is different from traditionally controllers. It can change frequency and duty cycle by configuring PWM's parameters at the initialization stage. Define GPIO4’s output frequency as 1000Hz, and assign them to PWM.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.1_BreatheLight/BreatheLight.py
    :linenos: 
    :language: python
    :lines: 4-4
    :dedent:

The range of duty cycle is 0-1023, so we use the first for loop to control PWM to change the duty cycle value, making PWM output 0% -100%; Use the second for loop to make PWM output 100%-0%.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.1_BreatheLight/BreatheLight.py
    :linenos: 
    :language: python
    :lines: 7-13
    :dedent:

Each time PWM is used, the hardware Timer will be turned ON to cooperate it. Therefore, after each use of PWM, deinit() needs to be called to turned OFF the timer. Otherwise, the PWM may fail to work next time.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.1_BreatheLight/BreatheLight.py
    :linenos: 
    :language: python
    :lines: 15-15
    :dedent:

.. note::
    
    PWM can be enabled on all pins except pin (16).  All channels have a frequency that ranges from 1 to 1000 (measured in Hz).  Duty cycle is between 0 and 1023 inclusive.

Reference
---------------------------

.. py:function:: Class PWM(pin, freq)	
    
    Before each use of PWM module, please add the statement " **from machine import PWM** " to the top of the python file.

    **pin:** PWM can be enabled on all pins except pin (16), such as Pin(0)、Pin(2)….
    
    **freq:** Output frequency, with the range of 0-1000 Hz
    
    **duty:** Duty cycle, with the range of 0-1023.
    
    **PWM.init(freq, duty):** Initialize PWM, parameters are the same as above.
    
    **PWM.freq([freq_val]):** When there is no parameter, the function obtains and returns PWM frequency; When parameters are set, the function is used to set PWM frequency and returns nothing.
    
    **PWM.duty([duty_val]):** When there is no parameter, the function obtains and returns PWM duty cycle; When parameters are set, the function is used to set PWM duty cycle.
    
    **PWM.deinit():** Turn OFF PWM.

Project 4.2 Meteor Flowing Light
****************************************

After learning about PWM, we can use it to control LED Bar Graph and realize a cooler Flowing Light.

Component List
===============================

+-------------------------+------------------------------+
| ESP8266 x1              | USB cable                    |
|                         |                              |
| |Chapter01_00|          | |Chapter01_01|               |
+-------------------------+------------------------------+
| Breadboard x1                                          |
|                                                        |
| |Chapter01_02|                                         |
+----------------+------------------+--------------------+
|LED bar graph x1| Resistor 220Ω x8 | Jumper wire M/M x9 |
|                |                  |                    |
| |Chapter03_00| | |Chapter01_04|   | |Chapter01_05|     |
+----------------+------------------+--------------------+

.. |Chapter03_00| image:: ../_static/imgs/3_LED_Bar/Chapter03_00.png

Circuit
===========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter04_13|
   * -  Hardware connection 
     
        If you need any support, please feel free to contact us via: support@freenove.com

   * -  |Chapter04_14|

.. |Chapter04_13| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_13.png
.. |Chapter04_14| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_14.png

:red:`If LEDbar doesn't work, try to rotate LEDbar for 180°. The label is random.`

Code
===========================

Flowing Light with tail was implemented with PWM.

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "04.2_FlowingLight". Select"pwm.py", right click to select "Upload to /", wait for "pwm.py" to be uploaded to ESP8266 and then double click "FlowingLight.py" 

04.2_FlowingLight
------------------------------

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_15.png
    :align: center

Click "Run current script", and LED Bar Graph will gradually light up and out from left to right, then light up and out from right to left.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.2_FlowingLight/FlowingLight.py
    :linenos: 
    :language: python
    :lines: 1-19
    :dedent:

Import the object myPWM from pwm.py and set corresponding pins for PWM channel.

.. code-block:: python

    from machine import Pin,PWM

    pins=[13, 12, 14, 5, 4, 0, 2, 15]

First we defined 8 GPIO, 8 PWM channels, and 24 pulse width values.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.2_FlowingLight/FlowingLight.py
    :linenos: 
    :language: python
    :lines: 3-4
    :dedent:

Set the PWM pin[j] and duty cycle [I +j].

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.2_FlowingLight/FlowingLight.py
    :linenos: 
    :language: python
    :lines: 15-16
    :dedent:

In the code, a nesting of two for loops are used to achieve this effect. 

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/04.2_FlowingLight/FlowingLight.py
    :linenos: 
    :language: python
    :lines: 8-17
    :dedent:

In the main function, a nested for loop is used to control the pulse width of the PWM. Every time i in the first for loop increases by 1, the LED Bar Graph will move one grid, and gradually change according to the value in the array dutys. As shown in the following table, the value in the second row is the value of the array dutys, and the 8 green grids in each row below represent the 8 LEDs on the LED Bar Graph. Each time i increases by 1, the value of the LED Bar Graph will move to the right by one grid, and when it reaches the end, it will move from the end to the starting point, achieving the desired effect.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_16.png
    :align: center

How to import a custom python module
------------------------------------------

Each Python file, as long as it's stored on the file system of ESP8266, is a module. To import a custom module, the module file needs to be located in the MicroPython environment variable path or in the same path as the currently running program.

First, customize a python module "custom.py". Create a new py file and name it "custom.py". Write code to it and save it to ESP8266.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_17.png
    :align: center

Second, import custom module "custom" to main.py

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_18.png
    :align: center