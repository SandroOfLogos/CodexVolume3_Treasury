# reflex_matrix_svg.py — Mirror Web Visualizer (SVG Generator)

import json
from math import sin, cos, radians
from datetime import datetime

def load_chain(path="mirror_chain.json"):
    try:
        with open(path, "r") as f:
            return json.load(f).get("chains", [])
    except:
        print("❌ Could not load mirror_chain.json")
        return []

def generate_svg(chains, output_path="reflex_matrix.svg"):
    agents = set()
    for chain in chains:
        agents.add(chain["origin_agent"])
        agents.add(chain["reflected_by"])
    agents = sorted(list(agents))

    node_pos = {}
    radius = 150
    cx, cy = 200, 200
    angle_step = 360 / len(agents)

    for i, agent in enumerate(agents):
        angle = radians(i * angle_step)
        x = cx + radius * cos(angle)
        y = cy + radius * sin(angle)
        node_pos[agent] = (x, y)

    svg = [f'<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<text x="10" y="20" font-size="12">Codex Reflex Matrix – {datetime.now().date()}</text>')

    # Draw arrows
    for chain in chains:
        origin = chain["origin_agent"]
        target = chain["reflected_by"]
        status = chain.get("reflection_status", "unknown")
        color = {
            "structural": "#00cc00",
            "semantic": "#ffaa00",
            "partial": "#ffcc00",
            "awaiting": "#cccccc"
        }.get(status, "#999999")

        x1, y1 = node_pos[origin]
        x2, y2 = node_pos[target]
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/>')

    # Draw marker
    svg.append('''
    <defs>
        <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0,0 L0,6 L6,3 z" fill="black"/>
        </marker>
    </defs>
    ''')

    # Draw nodes
    for agent, (x, y) in node_pos.items():
        svg.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#444"/>')
        svg.append(f'<text x="{x + 12}" y="{y + 4}" font-size="10" fill="#000">{agent}</text>')

    svg.append('</svg>')

    with open(output_path, "w") as f:
        f.write("\n".join(svg))

    print(f"✅ reflex_matrix.svg written to {output_path}")

if __name__ == "__main__":
    chains = load_chain()
    generate_svg(chains)

