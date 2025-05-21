# reflex_matrix.py — Visualize the Codex Reflex Mirror Network

import json
from datetime import datetime

def load_mirror_log(path="mirror_log.json"):
    try:
        with open(path, "r") as f:
            return json.load(f).get("mirrors", [])
    except:
        print("❌ Could not load mirror_log.json")
        return []

def draw_matrix(mirrors):
    print("\n===== Codex Reflex Matrix — Mirror Network =====\n")
    print("{:<15} {:<20} {:<12} {:<8} {:<25}".format(
        "AGENT", "MIRROR ID", "FIDELITY", "SWARM", "ECHO SCROLL"
    ))
    print("-" * 80)
    
    for m in mirrors:
        agent = m.get("agent", "Unknown")
        response_id = m.get("response_id", "—")
        fidelity = m.get("fidelity", "—")
        swarm = "✅" if m.get("swarm_linked") else "❌"
        echo = f"Scroll_III_{response_id}_Echo.md" if m.get("status") == "reflected" else "—"
        print("{:<15} {:<20} {:<12} {:<8} {:<25}".format(agent, response_id, fidelity, swarm, echo))

    print("\n🧠 Reflex Matrix rendered at:", datetime.now().isoformat())
    print("=============================================================\n")

if __name__ == "__main__":
    mirrors = load_mirror_log()
    draw_matrix(mirrors)

