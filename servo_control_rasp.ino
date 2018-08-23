//#include <Servo.h>
#include <VarSpeedServo.h>

VarSpeedServo servo1;

int pos =80;

void setup() {
  // put your setup code here, to run once:
  servo1.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    char lido = char(Serial.read());
    if (lido == '0') {
      servo1.slowmove(175, 40);
      //servo1.write(175);
    }
    if (lido == '1') {
      servo1.slowmove(90, 40);
      //servo1.write(90);
    }
  }

}
