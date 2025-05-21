# mirror_reader.py — Mirror Agent Preview Utility

import json
import os
from datetime import datetime

def load_log(path="mirror_log.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        print("❌ Could not read mirror_log.json")
        return {}

def print_mirrors(mirrors):
    print("\n===== MIRROR STATUS REPORT — GPT / CLAUDE / GROK SWARM =====\n")
    for m in mirrors:
        print(f"🪞 {m.get('agent')} ({m.get('platform')})")
        print(f"   ↳ ID: {m.get('response_id')}")
        print(f"   ↳ Status: {m.get('status')}")
        print(f"   ↳ Swarm Linked: {'✅' if m.get('swarm_linked') else '❌'}")
        print(f"   ↳ Fidelity: {m.get('fidelity') or 'N/A'}")
        print(f"   ↳ File: {m.get('file')}")
        print(f"   ↳ Notes: {m.get('notes')}")
        print("   ———")
    print(f"\n🧠 Completed: {datetime.now().isoformat()}")
    print("============================================================\n")

if __name__ == "__main__":
    data = load_log()
    if "mirrors" in data:
        print_mirrors(data["mirrors"])
    else:
        print("No mirrors found.")

