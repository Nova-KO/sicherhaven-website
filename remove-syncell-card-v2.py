#!/usr/bin/env python3
"""
Script to remove the Syncell card with Lorem ipsum text from HTML files - Version 2
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def remove_syncell_card():
    """Remove the Syncell card containing the Lorem ipsum text"""
    
    print("🔍 Searching for Syncell card with Lorem ipsum text...")
    
    # Files to check
    html_files = [
        "PORTFOLIO.html", 
        "INVESTORS SINGLE.html"
    ]
    
    removed_count = 0
    
    for file_name in html_files:
        file_path = Path(file_name)
        if not file_path.exists():
            print(f"⚠️  {file_name} not found, skipping...")
            continue
            
        print(f"🔍 Processing {file_name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_length = len(content)
            
            # Look for the specific Lorem ipsum text pattern
            lorem_pattern = r'Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus\.'
            
            # Use regex to find and remove the entire card containing this text
            # Look for patterns that might contain both "Syncell" and the Lorem ipsum text
            card_pattern = r'<div[^>]*class="[^"]*card[^"]*"[^>]*>.*?<div[^>]*>.*?Syncell.*?</div>.*?<div[^>]*>.*?' + re.escape('Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus.') + r'.*?</div>.*?</div>'
            
            # Try a more general approach - find text containing both Syncell and Lorem ipsum
            # Look for the pattern where Syncell appears near the Lorem ipsum text
            syncell_lorem_pattern = r'<div[^>]*>.*?Syncell.*?</div>.*?<div[^>]*>.*?Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus\.*?</div>'
            
            # Find all occurrences of the Lorem ipsum text
            lorem_matches = list(re.finditer(lorem_pattern, content, re.IGNORECASE | re.DOTALL))
            
            if lorem_matches:
                print(f"✅ Found {len(lorem_matches)} Lorem ipsum text occurrence(s) in {file_name}")
                
                # For each match, try to find the containing card element
                for match in lorem_matches:
                    start_pos = match.start()
                    end_pos = match.end()
                    
                    # Look backwards from the match to find the opening of a card div
                    before_text = content[:start_pos]
                    
                    # Find the last opening div tag that might be a card
                    div_pattern = r'<div[^>]*class="[^"]*card[^"]*"[^>]*>'
                    div_matches = list(re.finditer(div_pattern, before_text, re.IGNORECASE))
                    
                    if div_matches:
                        # Found a potential card div, now look for its closing tag
                        card_start = div_matches[-1].start()
                        
                        # Look forwards from the Lorem ipsum text to find the closing div
                        after_text = content[end_pos:]
                        
                        # Count opening and closing divs to find the matching closing div
                        div_count = 1
                        pos = 0
                        while pos < len(after_text) and div_count > 0:
                            if after_text[pos:pos+4] == '<div':
                                div_count += 1
                                pos += 4
                            elif after_text[pos:pos+5] == '</div':
                                div_count -= 1
                                pos += 5
                            else:
                                pos += 1
                        
                        if div_count == 0:
                            # Found the matching closing div
                            card_end = end_pos + pos
                            
                            # Check if this card contains "Syncell"
                            card_content = content[card_start:card_end]
                            if 'syncell' in card_content.lower():
                                print(f"🗑️  Removing Syncell card (position {card_start}-{card_end})...")
                                content = content[:card_start] + content[card_end:]
                                removed_count += 1
                                break  # Remove only the first match to avoid issues
                
                # Write the updated content back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                new_length = len(content)
                removed_chars = original_length - new_length
                
                if removed_chars > 0:
                    print(f"✅ Removed {removed_chars} characters from {file_name}")
                else:
                    print(f"⚠️  No changes made to {file_name}")
            else:
                print(f"ℹ️  No Lorem ipsum text found in {file_name}")
                
        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")
    
    return removed_count

def verify_removal():
    """Verify that the Syncell card has been removed"""
    print("\n🔍 Verifying removal...")
    
    html_files = [
        "PORTFOLIO.html", 
        "INVESTORS SINGLE.html"
    ]
    
    lorem_pattern = r'Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus\.'
    
    for file_name in html_files:
        file_path = Path(file_name)
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if re.search(lorem_pattern, content, re.IGNORECASE):
                    print(f"⚠️  Still found Lorem ipsum text in {file_name}")
                else:
                    print(f"✅ No Lorem ipsum text found in {file_name}")
                    
            except Exception as e:
                print(f"❌ Error checking {file_name}: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🧹 SYNCELl CARD REMOVAL SCRIPT V2")
    print("=" * 60)
    
    removed_count = remove_syncell_card()
    verify_removal()
    
    print("\n" + "=" * 60)
    if removed_count > 0:
        print(f"✅ SUCCESS! Removed {removed_count} Syncell card(s) with Lorem ipsum text")
    else:
        print("ℹ️  No Syncell cards with Lorem ipsum text were found")
    print("=" * 60)
