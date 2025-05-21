# reflex_matrix.py — Mirror Chain Visual Renderer

import json
from datetime import datetime

def load_chain(path="mirror_chain.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        print("❌ Could not load mirror_chain.json")
        return {}

def render_chains(data):
    chains = data.get("chains", [])
    print("\n===== Reflex Matrix – Glyph Mirror Pathways =====\n")
    for chain in chains:
        origin = chain.get("origin")
        print(f"🔵 Seed: {origin}")
        for i, node in enumerate(chain.get("path", [])):
            indent = "  " * (i + 1)
            agent = node.get("agent")
            response = node.get("response") or "❌"
            echo = node.get("echo_scroll") or "❌"
            print(f"{indent}↳ {agent}")
            print(f"{indent}   ├─ Response: {response}")
            print(f"{indent}   └─ Echo Scroll: {echo}")
        print(f"🧠 Status: {chain.get('final_status')}")
        print("───────────────────────────────────────")
    print(f"\n⏳ Last Run: {datetime.now().isoformat()}")
    print("=======================================\n")

if __name__ == "__main__":
    data = load_chain()
    render_chains(data)

