//// ****** THIS FILE IS AUTOGENERATED ******
////
////          >>>> PLEASE ADAPT IT TO YOUR NEEDS <<<<
////
/// 
///  Filename; C:\Users\realm.DESKTOP-DQ0IJ8Q\Documents\GitHub\instrumentacion2\20190604\examples-master\arduino-qt-toogle-led\run.py
///  Source class: LEDDriver
///  Generation timestamp: 2019-06-04T14:53:50.915664
///  Class code hash: 8647375a3d456c77a25af7a8712a5951c71a1594
///
/////////////////////////////////////////////////////////////



#include "inodriver_user.h"

void user_setup() {
    pinmode(13,OUTPUT);
}

void user_loop() {
}
// COMMAND: LED, FEAT: led
int get_LED(int value) {
  return 0;
};


int set_LED(int value) {
   if (value>0)
      digitalWrite(13, HIGH);
   else
      digitalWrite(13, LOW);
   return 0;
};

