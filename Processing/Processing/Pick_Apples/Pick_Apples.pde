/*
 ******************************************************************************
 * Sketch  Pick Apples
 * Author  Zhentao Lin @ Freenove (http://www.freenove.com)
 * Date    2022/5/11
 ******************************************************************************
 * Brief
 *   This sketch is used to control a 2D ellipse through communicate to an 
 *   ESP8266 board or other micro controller.
 *   It will automatically detect and connect to a device (serial port) which 
 *   use the same trans format.
 ******************************************************************************
 * Copyright
 *   Copyright © Freenove (http://www.freenove.com)
 * License
 *   Creative Commons Attribution ShareAlike 3.0 
 *   (http://creativecommons.org/licenses/by-sa/3.0/legalcode)
 ******************************************************************************
 */

/* Includes ------------------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/

SerialDevice serialDevice = new SerialDevice(this);
int serial_flag=0;

void setup() {
  size(650,650);
  background(102);
  textAlign(CENTER, CENTER);
  textSize(64);
  text("Starting...", width / 2, (height - 40) / 2);
  textSize(16);
  text("www.freenove.com", width / 2, height - 20);
  
  gameUiInit();
}

void draw() {
  if (!serialDevice.active())
  {
    if (!serialDevice.start())
    {
      delay(1000);
      return;
    }
  }
  
   int digitalValue;
  digitalValue = serialDevice.requestDigital();
  if(digitalValue!=-1){
    dealData(digitalValue);
  }
  RunGame();
}

void dealData(int digital){
    if(digital == 1  &&  x != 0) {//左
      x -= 20;
    }
    if(digital == 2  &&  x != 600) {//右
        x += 20;
    }
    if(digital == 3  &&  y != 0) {//下
        y -= 20;
    }
    if(digital == 4  &&  y != 600) {//上
        y += 20;
    }
    if(y <= 60){
        y = 60;
    }
    if(y >= 560){
        y = 560;
    }
}
