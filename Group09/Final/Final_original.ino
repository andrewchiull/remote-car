//#include <Servo.h> 
//
//
//#define pinIRa A0   
//      
//#define motorA_1A 5 // A_1A控制A馬達的前進（HIGH）、後退（LOW）
//#define motorA_1B 6 // A_1B控制A馬達的速度 0~255 ，LOW表示停止
//
//#define pinServo 3
//
//#define THRESHOLD 400
//
//#define FORWARD_TIME 1500
//#define STOP_TIME 150
//#define BACKWARD_TIME 1200
//#define SPEED 150
//Servo ServoMotor; 
//
//int IRvalueA = 0;
//int IRvalueD = 0;
//
//int Speed = 150;
//int LastForwardDegree = 75;
//
//void ForwardCar(){
//    Serial.println("Forward");
//    digitalWrite(motorA_1A, HIGH);
//    analogWrite(motorA_1B, 255-SPEED);
//    delay(FORWARD_TIME);
//    StopCar(true);
//    LastForwardDegree = ServoMotor.read();
//}
//void StopCar(int is_Forward){
////    digitalWrite(motorA_1A, LOW);  
////    analogWrite(motorA_1B, 200);  
////    delay(100)
//    if(is_Forward){
//        digitalWrite(motorA_1A, LOW);  
//        analogWrite(motorA_1B, 128);      
//    }else{
//        digitalWrite(motorA_1A, HIGH);  
//        analogWrite(motorA_1B, 128);      
//    }
//    delay(STOP_TIME);
//
//    //Stop motor
//    digitalWrite(motorA_1A, HIGH);  
//    analogWrite(motorA_1B, 255);  
//}
//
//void BackwardCar(){
//    Serial.println("Backward");
//    ServoMotor.write(LastForwardDegree);
//    delay(1000);
//    digitalWrite(motorA_1A, LOW);
//    analogWrite(motorA_1B, SPEED);
//    delay(BACKWARD_TIME);
//    StopCar(false);
// 
//  
//}
//
//int ChangeDirection(){
//    int IRvalueA; 
//    int degree = 0;
//    for(degree = 20 ; degree <= 140; degree+=10){
//        delay(500);
//        Serial.print("degree \t");
//        Serial.print(IRvalueA);
//        Serial.print("\t");
//        Serial.println(degree);
//        ServoMotor.write(degree);
//        IRvalueA = analogRead(pinIRa);
//        if(IRvalueA > THRESHOLD){ //Find the black
//            ForwardCar();
//            return 1;       
//        }
//    }
//    return 0;
//   
//  
//}
//
//
//void setup()
//{
//  Serial.begin(9600);
//  // For IR sensor
//  pinMode(pinIRa,INPUT);
//
//  
//  // For motor
//  pinMode(motorA_1A,OUTPUT);
//  pinMode(motorA_1B,OUTPUT);
//
//  //For Servo 
//  ServoMotor.attach(pinServo);
//  ServoMotor.write(75);
//  ForwardCar();
//}
//
//
//
//void loop()
//{
//  
//  Serial.print("Analog Reading=");
//  Serial.println(IRvalueA);
//  IRvalueA = analogRead(pinIRa);
//  // test
//  
//  //ServoMotor.write(IRvalueA/5);
//  //delay(5000);
//  // test
//  
//  if(IRvalueA > THRESHOLD){ // Black area
//      ForwardCar();
//      delay(1000);
//  }else{ // white area
//      int findBlackArea = 0;
//      while(!findBlackArea){
//          
//          findBlackArea = ChangeDirection();
//
//          if(!findBlackArea){
//              BackwardCar();
//             
//          }
//      }
//  }
//  delay(1000);
//
//}
