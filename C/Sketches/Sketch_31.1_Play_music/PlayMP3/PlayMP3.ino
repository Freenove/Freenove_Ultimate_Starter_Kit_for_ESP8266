/**********************************************************************
* Filename    : Play music
* Description : Play music.
* Auther      : www.freenove.com
* Modification: 2022/05/11
**********************************************************************/
#include <Arduino.h>
#include "AudioFileSourceSPIFFS.h"
#include "AudioGeneratorMP3.h"
#include "AudioOutputI2SNoDAC.h"
#include <ESP8266WiFi.h>
#include "AudioFileSourceID3.h"
#include "AudioOutputI2S.h"

#define PIN_BUTTON 5

AudioGeneratorMP3 *mp3;
AudioFileSourceSPIFFS *file;
AudioOutputI2SNoDAC *out;

void setup()
{
  Serial.begin(115200);
  delay(1000);
  SPIFFS.begin();
  file = new AudioFileSourceSPIFFS("/1.mp3");
  out = new AudioOutputI2SNoDAC();
  out->SetGain(2);//Volume Setup 
  mp3 = new AudioGeneratorMP3();
  mp3->begin(file, out);
  pinMode(PIN_BUTTON, INPUT);
}

void loop()
{ 
  if (mp3->isRunning()) { 
    if (!mp3->loop()){    
      mp3->stop();      
      delete file;
      delete mp3;
      mp3 = new AudioGeneratorMP3();
    }
  } else {
    if (digitalRead(PIN_BUTTON) == LOW){  
      file = new AudioFileSourceSPIFFS("/1.mp3"); 
      Serial.printf("MP3 done\n");
      delay(1000);
      mp3->begin(file, out); 
    }
  }
}
