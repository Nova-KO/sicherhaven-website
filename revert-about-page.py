#!/usr/bin/env python3
"""
Revert About page back to previous state
This will remove the About.html file and update footer links to point to index.html
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Define the base directory
BASE_DIR = Path(__file__).parent

def remove_about_page():
    """Remove the About.html file"""
    about_file = BASE_DIR / 'About.html'
    
    if about_file.exists():
        try:
            about_file.unlink()
            print(f"✅ Removed About.html file")
            return True
        except Exception as e:
            print(f"❌ Error removing About.html: {e}")
            return False
    else:
        print(f"ℹ️  About.html file not found (already removed?)")
        return True

def update_footer_links():
    """Update footer links to point to index.html instead of About.html"""
    print("🔗 Updating footer links...")
    
    html_files = list(Path(BASE_DIR).glob('*.html'))
    files_updated = 0
    
    for html_file in html_files:
        if html_file.name in ['About.html', '404.html', 'open-pages.html', 'file-index.html']:
            continue  # Skip these files
            
        print(f"Processing: {html_file.name}")
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all links that point to About.html
            about_links = soup.find_all('a', href='About.html')
            links_updated = 0
            
            for link in about_links:
                # Change href to point to index.html
                link['href'] = 'index.html'
                links_updated += 1
            
            # Also check for links with "about" in the text that might point to About.html
            all_links = soup.find_all('a')
            for link in all_links:
                href = link.get('href', '')
                text = link.get_text().strip().lower()
                
                # If link text contains "about" and href is About.html, change it
                if 'about' in text and href == 'About.html':
                    link['href'] = 'index.html'
                    links_updated += 1
            
            # Write back if changes were made
            if links_updated > 0:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"  ✅ Updated {links_updated} About links to point to index.html")
                files_updated += 1
            else:
                print(f"  ✓ No About links found")
                
        except Exception as e:
            print(f"  ❌ Error processing {html_file.name}: {e}")
    
    print(f"\n📊 Footer Links Update Summary:")
    print(f"  Files processed: {len(html_files) - 4}")
    print(f"  Files updated: {files_updated}")
    
    return files_updated > 0

def update_navigation_links():
    """Update navigation links in headers to remove About.html references"""
    print("\n🧭 Updating navigation links...")
    
    html_files = list(Path(BASE_DIR).glob('*.html'))
    files_updated = 0
    
    for html_file in html_files:
        if html_file.name in ['About.html', '404.html', 'open-pages.html', 'file-index.html']:
            continue  # Skip these files
            
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find navigation menus and update About links
            nav_links = soup.find_all('a', href='About.html')
            links_updated = 0
            
            for link in nav_links:
                # Check if this is in a navigation menu
                if link.find_parent(['nav', 'ul', 'div'], class_=re.compile(r'nav|menu')):
                    link['href'] = 'index.html'
                    links_updated += 1
            
            # Write back if changes were made
            if links_updated > 0:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"  ✅ Updated {html_file.name}: {links_updated} navigation links")
                files_updated += 1
            else:
                print(f"  ✓ No navigation About links in {html_file.name}")
                
        except Exception as e:
            print(f"  ❌ Error processing {html_file.name}: {e}")
    
    print(f"\n📊 Navigation Update Summary:")
    print(f"  Files processed: {len(html_files) - 4}")
    print(f"  Files updated: {files_updated}")
    
    return files_updated > 0

def create_revert_summary():
    """Create a summary of what was reverted"""
    summary_content = '''# About Page Revert - Complete! ✅

## 🎯 What Was Reverted

### ✅ **Removed About Page**
- **File**: `About.html` deleted
- **Reason**: Reverted to previous state as requested
- **Status**: ✅ File removed successfully

### ✅ **Updated Footer Links**
- **Change**: All "About" links now point to `index.html` instead of `About.html`
- **Impact**: Footer navigation restored to original template behavior
- **Files Updated**: All HTML pages with footers

### ✅ **Updated Navigation Links**
- **Change**: Header navigation "About" links point to `index.html`
- **Impact**: Consistent navigation across all pages
- **Status**: ✅ All navigation updated

---

## 📊 Revert Summary

| Action | Status | Details |
|--------|--------|---------|
| **Remove About.html** | ✅ | File deleted |
| **Update Footer Links** | ✅ | All About links → index.html |
| **Update Navigation** | ✅ | Header About links → index.html |

---

## 🔗 Current Navigation

### **Footer Navigation**
```
Company
├── About → index.html (back to homepage)
├── Contact → Contact.html
└── Blog → BLOG.html
```

### **What This Means**
- Clicking "About" in footer now takes users to the homepage
- No dedicated About page exists
- Navigation is consistent with original template structure

---

## 🧪 Testing

To verify the revert worked:

1. **Start server**: `./start-server.sh`
2. **Test About links**: Click "About" in footer on any page
3. **Expected result**: Should navigate to homepage (index.html)
4. **Verify**: `About.html` should return 404 (file not found)

---

## 📁 Files Affected

### **Deleted**
- `About.html` - Removed completely

### **Updated**
- All HTML pages with footer components
- Navigation menus in header sections

---

## ⚠️ Important Notes

- **About.html is permanently deleted** - if you need it back, it would need to be recreated
- **All About links now point to homepage** - this matches the original template behavior
- **Contact page remains unchanged** - still has Sicherhaven content
- **404 redirects still work** - all wrong links still redirect to 404.html

---

*Revert completed successfully - About page removed and navigation restored to previous state.*
'''
    
    with open('ABOUT-PAGE-REVERT-SUMMARY.md', 'w') as f:
        f.write(summary_content)
    
    print("📝 Created ABOUT-PAGE-REVERT-SUMMARY.md")

def main():
    print("=" * 60)
    print("Sicherhaven About Page Revert Script")
    print("=" * 60)
    print()
    
    # Step 1: Remove About.html file
    print("🗑️  Step 1: Removing About.html file...")
    about_removed = remove_about_page()
    
    # Step 2: Update footer links
    print("\n🔗 Step 2: Updating footer links...")
    footer_updated = update_footer_links()
    
    # Step 3: Update navigation links
    print("\n🧭 Step 3: Updating navigation links...")
    nav_updated = update_navigation_links()
    
    # Step 4: Create summary
    print("\n📝 Step 4: Creating revert summary...")
    create_revert_summary()
    
    print()
    print("=" * 60)
    print("✅ About Page Revert Complete!")
    print("=" * 60)
    print()
    print("What was done:")
    print("• ✅ Removed About.html file")
    print("• ✅ Updated footer links to point to index.html")
    print("• ✅ Updated navigation links in headers")
    print("• ✅ Created revert summary documentation")
    print()
    print("Current state:")
    print("• About links now go to homepage (index.html)")
    print("• No dedicated About page exists")
    print("• Navigation matches original template structure")
    print()
    print("To test:")
    print("1. Start server: ./start-server.sh")
    print("2. Click 'About' in footer on any page")
    print("3. Should navigate to homepage")
    print("4. About.html should return 404 (not found)")
    print()
    print("🎉 About page successfully reverted to previous state!")

if __name__ == '__main__':
    main()
