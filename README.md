
# 🛡️ AegisSOC

AegisSOC is an open-source SOC tool that collects syslog messages, detects suspicious activity, and prints alerts in real-time.

---

## Features
- Collects syslog over UDP (default port 5140)
- Real-time alert detection
- Easy to add custom rules

---

## Installation

1. Clone the repo:

git clone https://github.com/jaisonbthomas/AegisSOC.git
cd AegisSOC

2. Install dependencies:

pip3 install -r requirements.txt

3. Run the tool:

cd src
python3 main.py

---

## Testing

Send a test log:

echo "<13>Sep 14 21:00:00 testhost sshd: Failed password for user test" | nc -u 127.0.0.1 5140

You should see alerts printed in the terminal.

---

## Adding Rules

Edit src/detectors/rule_engine.py and add your custom rules.

---

## License

MIT License © 2025 Radweber / Developed By Jaison B Thomas
