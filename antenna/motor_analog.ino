#include <Servo.h>

#include <Servo.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x04


int state = 0;
Servo myservoAz; // Azimuth
Servo myservoEl; // Elevation


byte number = 0;
byte numAz = 0;
byte numEl = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); 
  Wire.begin(SLAVE_ADDRESS);

  Wire.onReceive(receiveData);

  myservoAz.attach(9);
  myservoEl.attach(10);

  calbration();
}

void calbration() {
  // initialize Antenna
  myservoAz.write(0);
  delay(1000);
  myservoAz.write(90);
  delay(1000);
  myservoAz.write(180);
  delay(1000);
  myservoAz.write(0);
  delay(1000);
  
  myservoEl.write(0);
  delay(1000);
  myservoEl.write(90);
  delay(1000);
  myservoEl.write(180);
  delay(1000);
  myservoEl.write(0);    
}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){

  while(Wire.available()) {
    number = Wire.read();
    Serial.println(99);
    Serial.println(number);
    
    if(number == 0x01){
        numAz = byte(Wire.read());  
        numEl = byte(Wire.read());              
        myservoAz.write(numAz);
        myservoEl.write(numEl);  

    }else if(number == 0x02){
          myservoAz.write(0);
          delay(2000);
          myservoAz.write(90);
          delay(2000);
          myservoAz.write(180);
          delay(4000);
          myservoAz.write(0);
  
          delay(2000);
          myservoEl.write(0);
          delay(2000);
          myservoEl.write(90);
          delay(2000);
          myservoEl.write(180);
          delay(4000);
          myservoEl.write(0);  
    
    }
  
  }
}
