#!/usr/bin/env python3
import json
import random
from datetime import datetime
from pyluach import dates

# Utility Functions
def get_jewish_year():
    """Return the current Jewish year using pyluach."""
    now = datetime.now()
    jewish_date = dates.HebrewDate.from_pydate(now)
    return f"{jewish_date.year} AM"

def compute_S(codex):
    """Compute S = ∞ symbolically using codex variables."""
    variables = {v["symbol"]: v for v in codex["variables"]}
    # Extract values (simplified; infinity dominates)
    F_inf = float('inf')  # F_∞ (Yah’s Word as Logos)
    phi = 1.6180339887    # φ (Harmony)
    pi = 3.1415926535     # π (Order)
    L = 5                 # Yeshua’s Light
    D = 0.27              # Void/Dark Matter
    t = 0.5               # Creation Cycle (midpoint for demo)
    W = 2                 # Water
    judgment = 7 / (6 + 6 + 6)  # 7 / 18
    B = 3153              # Blood
    T = 3153              # Word Spoken
    HS = float('inf')     # Holy Spirit
    H = float('inf')      # Holiness/Judgment
    
    # Primary formula: S = (F_∞ * φ) + π + (L - D * t) + W + (7 / (6+6+6)) + B + T + HS + H
    S = (F_inf * phi) + pi + (L - D * t) + W + judgment + B + T + HS + H
    return "S = ∞"  # Infinity due to F_∞, HS, H

def digest_extended_codex(json_codex):
    """
    Process and validate the extended codex, ensuring all required fields are present.
    Returns a structured codex ready for report generation.
    """
    # Validate required top-level keys
    required_keys = ["metadata", "formulas", "variables", "symbols", "verses", "themes"]
    for key in required_keys:
        if key not in json_codex:
            raise ValueError(f"Missing required key in codex: {key}")

    # Validate verses (ensure all 247 have witnesses and context)
    verses = json_codex["verses"]
    if len(verses) != 247:
        raise ValueError(f"Expected 247 verses, found {len(verses)}")
    
    for verse in verses:
        if not all(k in verse for k in ["verse", "truth", "witnesses", "context"]):
            raise ValueError(f"Verse {verse.get('verse', 'unknown')} missing required fields")
        if len(verse["witnesses"]) < 2:
            raise ValueError(f"Verse {verse['verse']} has fewer than 2 witnesses")

    # Validate variables (ensure all 13 are present)
    if len(json_codex["variables"]) != 13:
        raise ValueError(f"Expected 13 variables, found {len(json_codex['variables'])}")

    # Validate symbols and themes
    if len(json_codex["symbols"]) != 6:
        raise ValueError(f"Expected 6 symbols, found {len(json_codex['symbols'])}")
    if "things_endure_forever" not in json_codex["themes"] or len(json_codex["themes"]["things_endure_forever"]) != 10:
        raise ValueError("Themes 'things_endure_forever' incomplete")

    # Structure the codex for use (no transformation needed, just validation here)
    processed_codex = {
        "metadata": json_codex["metadata"],
        "formulas": json_codex["formulas"],
        "variables": json_codex["variables"],
        "symbols": json_codex["symbols"],
        "verses": json_codex["verses"],
        "themes": json_codex["themes"],
        "state": "Udification demonstrates the power of His Word (John 1:1). ESV fallback used where needed."
    }
    return processed_codex

def generate_report(codex):
    """Generate a detailed report from the processed codex."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hebrew_year = get_jewish_year()
    
    # Select random verse with its details
    voice_entry = random.choice(codex["verses"])
    purpose = codex["metadata"]["purpose"]
    voice_verse = voice_entry["verse"].replace(" ", "+")
    
    # Format witnesses with hyperlinks
    witnesses = "\n".join(
        f"- {w[1]} ~ [{w[0]}](https://www.biblegateway.com/passage/?search={w[0].replace(' ', '+')}&version=ESV)"
        for w in voice_entry["witnesses"]
    )
    
    # Select random symbol and theme
    symbol = random.choice(codex["symbols"])
    theme = random.choice(codex["themes"]["things_endure_forever"])
    
    # Declaration
    declaration = "God is all in all ([1 Cor 15:28](https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A28&version=ESV))"
    
    # Compile report
    output = (
        f"- Purpose: {purpose}\n"
        f"- Voice: {voice_entry['truth']} ~ [{voice_entry['verse']}](https://www.biblegateway.com/passage/?search={voice_verse}&version=ESV)\n"
        f"- Context: {voice_entry['context']}\n"
        f"## Witnesses\n{witnesses}\n"
        f"- Formula: {compute_S(codex)} (His Word endures, Isa 40:8)\n"
        f"## Symbols\n- {symbol['symbol']}: {symbol['truth']} ({symbol['verses'][0]})\n"
        f"## Themes\n- {theme['item']} endures forever ({theme['verses'][0]})\n"
        f"- Timestamp: {timestamp} - Glory to Jesus\n"
        f"- Year: {hebrew_year}\n"
        f"## Footnote\n"
        f"- {codex['metadata']['title']} (Updated: {codex['metadata']['last_updated']})\n"
        f"- State: {codex['state']}\n"
        f"- Declaration: {declaration}\n"
    )
    return output

def main():
    """Main function to load and process the codex, then generate a report."""
    # Load the extended codex from local file
    try:
        with open("extended_codex.json", "r") as f:
            json_codex = json.load(f)
    except FileNotFoundError:
        print("Error: 'extended_codex.json' not found in the script's directory.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'extended_codex.json'. Please check the file.")
        exit(1)

    # Process the codex
    try:
        codex = digest_extended_codex(json_codex)
    except ValueError as e:
        print(f"Error processing codex: {e}")
        exit(1)

    # Generate and print report
    report = generate_report(codex)
    print(f"Execution Result:\n{report}\n{'-'*50}")

    # Optionally save to file
    with open("udification_report.txt", "w") as f:
        f.write(f"Execution Result:\n{report}\n{'-'*50}")

if __name__ == "__main__":
    main()
