#!/usr/bin/env python3
"""
Script to remove the Syncell card with Lorem ipsum text from HTML files
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def remove_syncell_card():
    """Remove the Syncell card containing the Lorem ipsum text"""
    
    print("🔍 Searching for Syncell card with Lorem ipsum text...")
    
    # Files to check
    html_files = [
        "index.html",
        "PORTFOLIO.html", 
        "INVESTORS.html",
        "Contact.html",
        "BLOG.html",
        "coming soon.html",
        "INVESTORS SINGLE.html",
        "BLOG POST.html"
    ]
    
    removed_count = 0
    
    for file_name in html_files:
        file_path = Path(file_name)
        if not file_path.exists():
            print(f"⚠️  {file_name} not found, skipping...")
            continue
            
        print(f"🔍 Checking {file_name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_length = len(content)
            
            # Look for the specific Lorem ipsum text pattern
            lorem_pattern = r'Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus\.'
            
            # Find the context around this text to identify the card structure
            matches = list(re.finditer(lorem_pattern, content, re.IGNORECASE))
            
            if matches:
                print(f"✅ Found Lorem ipsum text in {file_name}")
                
                # Parse with BeautifulSoup to better handle the HTML structure
                soup = BeautifulSoup(content, 'html.parser')
                
                # Find elements containing the Lorem ipsum text
                elements_with_lorem = soup.find_all(text=re.compile(lorem_pattern, re.IGNORECASE))
                
                for element in elements_with_lorem:
                    # Find the parent card/container element
                    parent = element.parent
                    while parent:
                        # Look for common card container classes
                        if parent.get('class') and any('card' in cls.lower() or 'portfolio' in cls.lower() or 'item' in cls.lower() for cls in parent.get('class')):
                            # Check if this card also contains "Syncell"
                            if 'syncell' in str(parent).lower():
                                print(f"🗑️  Removing Syncell card containing Lorem ipsum text...")
                                parent.decompose()
                                removed_count += 1
                                break
                        parent = parent.parent
                
                # Write the updated content back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                new_length = len(str(soup))
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
        "index.html",
        "PORTFOLIO.html", 
        "INVESTORS.html",
        "Contact.html",
        "BLOG.html",
        "coming soon.html",
        "INVESTORS SINGLE.html",
        "BLOG POST.html"
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
    print("🧹 SYNCELl CARD REMOVAL SCRIPT")
    print("=" * 60)
    
    removed_count = remove_syncell_card()
    verify_removal()
    
    print("\n" + "=" * 60)
    if removed_count > 0:
        print(f"✅ SUCCESS! Removed {removed_count} Syncell card(s) with Lorem ipsum text")
    else:
        print("ℹ️  No Syncell cards with Lorem ipsum text were found")
    print("=" * 60)
