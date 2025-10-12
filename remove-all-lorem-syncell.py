#!/usr/bin/env python3
"""
Script to remove ALL instances of the specific Lorem ipsum text from HTML files
"""

import re
from pathlib import Path

def remove_lorem_text():
    """Remove all instances of the specific Lorem ipsum text"""
    
    print("🔍 Removing all instances of Lorem ipsum text...")
    
    # The exact text to remove
    lorem_text = "Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus."
    
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
    
    total_removed = 0
    
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
            
            # Count occurrences before removal
            occurrences = content.count(lorem_text)
            
            if occurrences > 0:
                print(f"✅ Found {occurrences} occurrence(s) of Lorem ipsum text")
                
                # Remove all instances of the text
                content = content.replace(lorem_text, "")
                
                # Also try case-insensitive removal
                content = re.sub(re.escape(lorem_text), "", content, flags=re.IGNORECASE)
                
                # Write the updated content back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                new_length = len(content)
                removed_chars = original_length - new_length
                
                print(f"✅ Removed {removed_chars} characters from {file_name}")
                total_removed += occurrences
            else:
                print(f"ℹ️  No Lorem ipsum text found in {file_name}")
                
        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")
    
    return total_removed

def verify_removal():
    """Verify that all Lorem ipsum text has been removed"""
    print("\n🔍 Verifying removal...")
    
    lorem_text = "Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus."
    
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
    
    remaining_count = 0
    
    for file_name in html_files:
        file_path = Path(file_name)
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for exact match
                exact_matches = content.count(lorem_text)
                
                # Check for case-insensitive matches
                case_insensitive_matches = len(re.findall(re.escape(lorem_text), content, re.IGNORECASE))
                
                if exact_matches > 0 or case_insensitive_matches > 0:
                    print(f"⚠️  Still found {exact_matches} exact and {case_insensitive_matches} case-insensitive matches in {file_name}")
                    remaining_count += exact_matches + case_insensitive_matches
                else:
                    print(f"✅ No Lorem ipsum text found in {file_name}")
                    
            except Exception as e:
                print(f"❌ Error checking {file_name}: {e}")
    
    return remaining_count

if __name__ == "__main__":
    print("=" * 70)
    print("🧹 COMPLETE LOREM IPSUM TEXT REMOVAL SCRIPT")
    print("=" * 70)
    
    removed_count = remove_lorem_text()
    remaining_count = verify_removal()
    
    print("\n" + "=" * 70)
    if removed_count > 0:
        print(f"✅ SUCCESS! Removed {removed_count} instance(s) of Lorem ipsum text")
    else:
        print("ℹ️  No Lorem ipsum text was found to remove")
    
    if remaining_count > 0:
        print(f"⚠️  {remaining_count} instance(s) still remain")
    else:
        print("🎉 All Lorem ipsum text has been successfully removed!")
    print("=" * 70)
