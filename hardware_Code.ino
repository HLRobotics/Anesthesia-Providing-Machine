//Project Name:ANESTHESIA PROVIDING MACHINE
#include <Servo.h>
Servo VALVE_CONTROLLER;
String action;
int MSG_RXD0,MSG_RXD1=0;
int MSG_RXD=0;
int PROCESSED_MSG=0;

void setup()
{
    VALVE_CONTROLLER.attach(6);
    Serial.begin(9600);
    Serial.println("[ ANESTHESIA PROVIDING MACHINE HARDWARE SOFTWARE ]");
}

void loop()
{
if(Serial.available()>0)
    {
        action=Serial.readString();
        action.trim();
        Serial.print(action);
        MSG_RXD0=action[0]-48;
        MSG_RXD1=action[0]-48;
        MSG_RXD=MSG_RXD0*10+MSG_RXD1;
        PROCESSED_MSG=((MSG_RXD/90)*100);
        Serial.println(PROCESSED_MSG);
        VALVE_CONTROLLER.write(PROCESSED_MSG);

    }
}
