#!/usr/bin/env python3
import re

# Define rules (add more later)
RULES = [
    {"id": "r001", "name": "Failed login attempt", "pattern": r"failed password"},
    {"id": "r002", "name": "Possible sudo/root command", "pattern": r"\bsudo\b"},
    {"id": "r003", "name": "Error message detected", "pattern": r"\berror\b"},
]

def detect_alerts(log):
    alerts = []
    for rule in RULES:
        if re.search(rule["pattern"], log, re.IGNORECASE):
            alerts.append({"rule_id": rule["id"], "name": rule["name"], "log": log})
    return alerts
