#!/usr/bin/env python
# coding: utf-8

# In[4]:


#define BLYNK_PRINT Serial #include <ESP8266WiFi.h> #include <BlynkSimpleEsp8266.h> int pirPin = 14;
int relayPin=5;
int pirValue;
(/unsigned, long, int, tm;)
(/unsigned, long, int, prev=0;, unsigned, long, int, req;)

char auth[] = "jxUw4vvyg-f7RROJ_9feTbE7zSdS93Z-"; char ssid[] = "Sayan S8";
char pass[] = "1122334450";
void setup()
{
Serial.begin(115200); Blynk.begin(auth, ssid, pass); pinMode(pirPin, INPUT); pinMode(relayPin, OUTPUT); pinMode(15,OUTPUT); pinMode(13,OUTPUT);
}

void pirSensor()
{
pirValue = digitalRead(pirPin); Blynk.virtualWrite(V0, pirValue);
}

void loop()
{
Blynk.run(); pirSensor();
if (pirValue == HIGH)
{

digitalWrite(relayPin, LOW); req=(millis()%3000)+200;
//req=tm-prev;
//prev=tm; Serial.println(req); delay(req); digitalWrite(relayPin,HIGH); delay(200); digitalWrite(15,HIGH); delay(req); digitalWrite(15,LOW); delay(200); digitalWrite(13,HIGH); delay(req); digitalWrite(13,LOW); delay(200);
pirValue=LOW;
}

else

digitalWrite(relayPin, HIGH);



}


# In[ ]:




