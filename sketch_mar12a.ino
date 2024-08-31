void setup() {
  Serial.begin(9600);
  pinMode(5,OUTPUT);

}

void loop() {
  int x;
  if(Serial.available()>0){
    x = Serial.readString().toInt();
    analogWrite(5,x); 
  }

}