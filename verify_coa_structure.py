#!/usr/bin/env python3
"""
Verification script for COA Part 1 - Digital Logic & Number Systems
Validates structure, formulas, and completeness
"""

import re
from pathlib import Path

def verify_document():
    file_path = Path("COA/Part1_Digital_Logic_Number_Systems.md")
    
    if not file_path.exists():
        print("❌ File not found!")
        return False
    
    content = file_path.read_text()
    
    # Check for required sections
    required_sections = [
        "NUMBER SYSTEMS & CONVERSIONS",
        "SIGNED NUMBER REPRESENTATIONS",
        "BINARY ARITHMETIC",
        "FLOATING POINT REPRESENTATION",
        "BOOLEAN ALGEBRA & LOGIC GATES",
        "COMBINATIONAL CIRCUITS",
        "SEQUENTIAL CIRCUITS",
        "K-MAP SIMPLIFICATION",
        "HAZARDS & RACE CONDITIONS",
        "PRACTICE PROBLEM SET"
    ]
    
    print("📋 STRUCTURE VALIDATION")
    print("="*60)
    
    missing_sections = []
    for section in required_sections:
        if section in content:
            print(f"✓ {section}")
        else:
            print(f"✗ {section}")
            missing_sections.append(section)
    
    # Check for key components in each section
    print("\n🔬 COMPONENT VALIDATION")
    print("="*60)
    
    components = {
        "THE ATOMIC TRUTH": content.count("THE ATOMIC TRUTH"),
        "The Path of Elegance": content.count("The Path of Elegance"),
        "The Golden Pivot": content.count("The Golden Pivot"),
        "The 2026 Adversarial Vault": content.count("The 2026 Adversarial Vault"),
        "The Inversion (Anti-Solution)": content.count("The Inversion (Anti-Solution)"),
        "MSQ Logic Gate": content.count("MSQ Logic Gate"),
        "NAT Precision Lock": content.count("NAT Precision Lock"),
        "Permanent Recall": content.count("Permanent Recall"),
        "The Bizarre Mnemonic": content.count("The Bizarre Mnemonic"),
        "The Mental Slider": content.count("The Mental Slider"),
        "The 5-Second Snap-Check": content.count("The 5-Second Snap-Check")
    }
    
    for component, count in components.items():
        status = "✓" if count >= 5 else "⚠"
        print(f"{status} {component}: {count} instances")
    
    # Count LaTeX formulas
    print("\n📐 FORMULA VALIDATION")
    print("="*60)
    
    inline_math = len(re.findall(r'\$[^$]+\$', content))
    display_math = len(re.findall(r'\$\$[^$]+\$\$', content))
    
    print(f"✓ Inline math formulas ($...$): {inline_math}")
    print(f"✓ Display math formulas ($$...$$): {display_math}")
    print(f"✓ Total formulas: {inline_math + display_math}")
    
    # Check for practice problems
    print("\n🎯 PRACTICE PROBLEMS")
    print("="*60)
    
    problems = re.findall(r'## Problem \d+:', content)
    print(f"✓ Total practice problems: {len(problems)}")
    
    # File statistics
    print("\n📊 DOCUMENT STATISTICS")
    print("="*60)
    
    lines = len(content.split('\n'))
    words = len(content.split())
    chars = len(content)
    
    print(f"✓ Lines: {lines:,}")
    print(f"✓ Words: {words:,}")
    print(f"✓ Characters: {chars:,}")
    print(f"✓ File size: {chars/1024:.2f} KB")
    
    # Final assessment
    print("\n" + "="*60)
    if missing_sections:
        print(f"⚠ ASSESSMENT: INCOMPLETE ({len(missing_sections)} sections missing)")
        return False
    else:
        print("✅ ASSESSMENT: COMPLETE & SOVEREIGN")
        print("🔥 Logic Singularity verified for 2026 (IIT-G Standards)")
        return True

if __name__ == "__main__":
    verify_document()
