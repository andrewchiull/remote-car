#include <Servo.h>

#define motorA_F 5
#define motorA_B 6
#define motorB_F 11
#define motorB_B 10

#define pinServo 3

#define THRESHOLD 400

#define FORWARD_TIME 1000
#define BACKWARD_TIME 500
#define SPEED_A 255
#define SPEED_B 255
Servo ServoMotor;

int Speed = 150;

void ForwardCar(){
   Serial.println("Forward");
   analogWrite(motorA_F, SPEED_A);
   analogWrite(motorA_B, 0);
   analogWrite(motorB_F, SPEED_B);
   analogWrite(motorB_B, 0);
   delay(FORWARD_TIME);
   StopCar();
}

void StopCar(){
   //Stop motor
   analogWrite(motorA_F, 0);
   analogWrite(motorA_B, 0);
   analogWrite(motorB_F, 0);
   analogWrite(motorB_B, 0);
}

void BackwardCar(){
   Serial.println("Forward");
   analogWrite(motorA_F, 0);
   analogWrite(motorA_B, SPEED_A);
   analogWrite(motorB_F, 0);
   analogWrite(motorB_B, SPEED_B);
   delay(BACKWARD_TIME);
   StopCar();


}

void setup()
{
  Serial.begin(9600);

  // For motor
  pinMode(motorA_F,OUTPUT);
  pinMode(motorA_B,OUTPUT);
  pinMode(motorB_F,OUTPUT);
  pinMode(motorB_B,OUTPUT);

  //For Servo
  ServoMotor.attach(pinServo);
  ServoMotor.write(75);
}



void loop()
{
  ForwardCar();
  BackwardCar();
}
