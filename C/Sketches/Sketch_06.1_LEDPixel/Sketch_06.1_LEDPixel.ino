/**********************************************************************
  Filename    : NeoPixel
  Description : Basic usage of LEDPixel, 
                Make the strip light up in different colors gradually.
  Auther      : www.freenove.com
  Modification: 2022/05/10
**********************************************************************/
#include <Adafruit_NeoPixel.h>
#define PIN       2 
// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS 8 // Popular NeoPixel ring size
// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 500 // Time (in milliseconds) to pause between pixels
int m_color[5][3] = { {255, 0, 0}, {0, 255, 0}, {0, 0, 255}, {255, 255, 255}, {0, 0, 0} };
int delayval = 100;
void setup(){
    pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
    pixels.setBrightness(10);// set the brightness.
}
void loop(){
    pixels.clear(); // Set all pixel colors to 'off'
    // The first NeoPixel in a strand is #0, second is 1, all the way up
    // to the count of pixels minus one.
    for (int j = 0; j < 5; j++) {
        for(int i=0; i<NUMPIXELS; i++){ // For each pixel...
        // pixels.Color() takes RGB values, from 0,0,0 up to 255,255,255
            pixels.setPixelColor(i, m_color[j][0], m_color[j][1], m_color[j][2]);// Set color data.
            pixels.show();   // Send the updated pixel colors to the hardware.
            delay(DELAYVAL); // Pause before next pass through loop
        }
        delay(500);       // Interval time of each group of colors.
    }
}
