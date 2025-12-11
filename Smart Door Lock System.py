import network
import time
from machine import Pin, PWM
from umqtt.simple import MQTTClient

# ---------------- WiFi Setup ----------------
WIFI_SSID = "your_wifi_name"
WIFI_PASS = "your_wifi_password"

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)

while not wifi.isconnected():
    time.sleep(0.5)
    print("Connecting...")

print("Connected!")
print(wifi.ifconfig())

# ---------------- Servo Setup ----------------
servo = PWM(Pin(15), freq=50)  # GPIO 15

def lock_door():
    servo.duty(40)      # Servo angle for lock
    print("Door Locked")

def unlock_door():
    servo.duty(115)     # Servo angle for unlock
    print("Door Unlocked")

# ---------------- MQTT Setup ----------------
MQTT_BROKER = "broker.hivemq.com"
CLIENT_ID = "SmartDoor123"
TOPIC = b"home/door/lock"     # Subscribe topic

def mqtt_callback(topic, msg):
    print("Message received:", msg)

    if msg == b"LOCK":
        lock_door()
    elif msg == b"UNLOCK":
        unlock_door()

client = MQTTClient(CLIENT_ID, MQTT_BROKER)
client.set_callback(mqtt_callback)
client.connect()
client.subscribe(TOPIC)

print("Smart Door Lock Ready!")
print("Send MQTT messages: LOCK / UNLOCK")

# ---------------- Main Loop ----------------
while True:
    client.check_msg()   # Wait for MQTT commands
    time.sleep(0.1)
