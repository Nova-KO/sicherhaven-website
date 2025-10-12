#!/usr/bin/env python3
"""
Aggressive cleanup script to remove all remaining template elements
"""

import re
from pathlib import Path

def aggressive_cleanup():
    """Aggressively remove all template elements"""
    
    print("🔥 Aggressive template cleanup...")
    
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
    
    for file_name in html_files:
        file_path = Path(file_name)
        if not file_path.exists():
            continue
            
        print(f"🔥 Aggressively cleaning {file_name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove ALL promotional content
            content = re.sub(r'<div[^>]*class="[^"]*brix[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<a[^>]*class="[^"]*brix[^"]*"[^>]*>.*?</a>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<div[^>]*class="[^"]*more-templates[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<a[^>]*class="[^"]*more-templates[^"]*"[^>]*>.*?</a>', '', content, flags=re.DOTALL | re.IGNORECASE)
            
            # Remove ALL Syncell references
            content = re.sub(r'<img[^>]*syncell[^>]*/>', '', content, flags=re.IGNORECASE)
            content = re.sub(r'<img[^>]*alt="[^"]*syncell[^"]*"[^>]*/>', '', content, flags=re.IGNORECASE)
            
            # Remove template promotional text
            content = re.sub(r'Explore our collection of 200\+.*?Premium Webflow Templates.*?</p>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'Need to customize this template\?.*?Hire our Webflow team.*?</p>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'More Webflow Templates', '', content, flags=re.IGNORECASE)
            
            # Remove template links in footer
            content = re.sub(r'<a[^>]*href="https://www\.brixtemplates\.com[^"]*"[^>]*>.*?</a>', '', content, flags=re.DOTALL | re.IGNORECASE)
            
            # Clean up any remaining empty divs or sections
            content = re.sub(r'<div[^>]*class="[^"]*brix[^"]*"[^>]*>\s*</div>', '', content, flags=re.IGNORECASE)
            content = re.sub(r'<div[^>]*class="[^"]*more-templates[^"]*"[^>]*>\s*</div>', '', content, flags=re.IGNORECASE)
            
            # Write the cleaned content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Aggressively cleaned {file_name}")
                
        except Exception as e:
            print(f"❌ Error cleaning {file_name}: {e}")

def final_verification():
    """Final verification of cleanup"""
    print("\n🔍 Final verification...")
    
    try:
        with open("index.html", 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count remaining template elements
        syncell_count = len(re.findall(r'syncell', content, re.IGNORECASE))
        brix_count = len(re.findall(r'brix', content, re.IGNORECASE))
        templates_count = len(re.findall(r'more-templates', content, re.IGNORECASE))
        
        print(f"📊 Final verification results:")
        print(f"  • Syncell references: {syncell_count}")
        print(f"  • Brix references: {brix_count}")
        print(f"  • More templates references: {templates_count}")
        
        if syncell_count == 0 and brix_count == 0 and templates_count == 0:
            print("🎉 ALL TEMPLATE CONTENT REMOVED!")
        else:
            print("⚠️  Some template content may still remain")
            
        # Check for Sicherhaven content
        sicherhaven_count = len(re.findall(r'sicherhaven', content, re.IGNORECASE))
        eventify_count = len(re.findall(r'eventify', content, re.IGNORECASE))
        wealthwise_count = len(re.findall(r'wealthwise', content, re.IGNORECASE))
        
        print(f"📊 Sicherhaven content verification:")
        print(f"  • Sicherhaven references: {sicherhaven_count}")
        print(f"  • Eventify references: {eventify_count}")
        print(f"  • WealthWise references: {wealthwise_count}")
        
    except Exception as e:
        print(f"❌ Error in final verification: {e}")

if __name__ == "__main__":
    print("=" * 70)
    print("🔥 AGGRESSIVE TEMPLATE CLEANUP")
    print("=" * 70)
    
    aggressive_cleanup()
    final_verification()
    
    print("\n" + "=" * 70)
    print("🎉 AGGRESSIVE CLEANUP COMPLETE!")
    print("=" * 70)
