const byte Pin1 = A5;

void setup(){
  pinMode(Pin1, INPUT);
  Serial.begin(9600);
}
void loop (){
 long int val1 = analogRead(Pin1);
 Serial.println(val1);
 delay(1000);
}
