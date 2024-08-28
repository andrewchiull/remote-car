#include<Servo.h>

// Ultrasonic pins
#define ECHO 12
#define TRIG 13

// Motor pins
#define L_F 11 // Left Forward
#define L_B 10
#define R_F 5
#define R_B 6 // Right Backward
#define L_MAX L_MAX // Left Forward MAX
#define R_MAX 225 // Right Forward MAX

// Claw
#define MID 90 // Initial angle
#define RANGE 30 // Grabbing angle

Servo servoL;
Servo servoR;

void setup() {
  // put your setup code here, to run once:


  pinMode(L_F,OUTPUT);
  pinMode(L_B,OUTPUT);
  pinMode(R_F,OUTPUT);
  pinMode(R_B,OUTPUT);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  servoL.attach(9);
  servoR.attach(3);

  Serial.begin(9600);

}

void up(){
  analogWrite(L_F,L_MAX);
  analogWrite(L_B,0);
  analogWrite(R_F,R_MAX);
  analogWrite(R_B,0);
}

void L(){
  analogWrite(L_F,0);
  analogWrite(L_B,L_MAX);
  analogWrite(R_F,R_MAX);
  analogWrite(R_B,0);
}

void R(){
  analogWrite(L_F,L_MAX);
  analogWrite(L_B,0);
  analogWrite(R_F,0);
  analogWrite(R_B,R_MAX);
}

void down(){
  analogWrite(L_F,0);
  analogWrite(L_B,L_MAX);
  analogWrite(R_F,0);
  analogWrite(R_B,R_MAX);
}

void readUltra(){
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  // Sets the TRIG on HIGH state for 10 micro seconds
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  // Reads the ECHO, returns the sound wave travel time in microseconds
  double duration = pulseIn(ECHO, HIGH);
  // Calculating the distance
  double distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
}

void open(){
  for (int i = 0; i <= RANGE; i += 1) {
    servoL.write(MID + i);
    servoR.write(MID - i);
    delay(50);
  }
}

void close(){
  for (int i = 0; i <= RANGE; i += 1) {
    servoL.write(MID + RANGE - i);
    servoR.write(MID - RANGE + i);
    delay(50);
  }
}
void loop() {
  String data = "";
  if (Serial.available() > 0) {
    data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
  }
  open();
  close();


}
