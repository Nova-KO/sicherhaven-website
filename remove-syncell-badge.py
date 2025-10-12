#!/usr/bin/env python3
"""
Script to remove the syncell/more-templates promotional badge from index.html
"""

import re
from pathlib import Path

def remove_syncell_badge():
    """Remove the more-templates-badge-wrapper element and its CSS from index.html"""
    
    index_file = Path("index.html")
    if not index_file.exists():
        print("❌ index.html not found!")
        return False
    
    print("🧹 Removing syncell/more-templates promotional badge from index.html...")
    
    try:
        # Read the file
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Remove the HTML element (the promotional badge)
        # This regex matches the entire <a> tag with the more-templates-badge-wrapper class
        badge_pattern = r'<a[^>]*class="more-templates-badge-wrapper[^"]*"[^>]*>.*?</a>'
        content = re.sub(badge_pattern, '', content, flags=re.DOTALL)
        
        # Remove CSS for more-templates-badge-wrapper
        css_patterns = [
            # Remove CSS blocks for more-templates-badge-wrapper
            r'\.more-templates-badge-wrapper[^{]*\{[^}]*\}',
            # Remove CSS for related classes
            r'\.more-templates-logo[^{]*\{[^}]*\}',
            r'\.more-templates-p[^{]*\{[^}]*\}',
            r'\.more-webflow-templates-sub[^{]*\{[^}]*\}',
            r'\.more-templates-logo-wrapper[^{]*\{[^}]*\}',
        ]
        
        for pattern in css_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Remove any remaining CSS rules that might be related
        # Look for CSS rules that contain "more-templates" or "more-webflow"
        remaining_pattern = r'[^{]*more-templates[^{]*\{[^}]*\}'
        content = re.sub(remaining_pattern, '', content, flags=re.DOTALL)
        
        remaining_pattern2 = r'[^{]*more-webflow[^{]*\{[^}]*\}'
        content = re.sub(remaining_pattern2, '', content, flags=re.DOTALL)
        
        # Clean up any extra whitespace or empty lines
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Write the cleaned content back
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        new_length = len(content)
        removed_chars = original_length - new_length
        
        print(f"✅ Successfully removed syncell promotional badge!")
        print(f"   • Removed {removed_chars:,} characters")
        print(f"   • File size reduced from {original_length:,} to {new_length:,} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing syncell badge: {e}")
        return False

def verify_removal():
    """Verify that the syncell badge has been removed"""
    print("\n🔍 Verifying removal...")
    
    index_file = Path("index.html")
    if not index_file.exists():
        print("❌ index.html not found for verification!")
        return False
    
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for remaining references
        remaining_references = []
        
        if 'more-templates-badge-wrapper' in content:
            remaining_references.append('more-templates-badge-wrapper')
        
        if 'more-templates-logo' in content:
            remaining_references.append('more-templates-logo')
            
        if 'more-webflow-templates-sub' in content:
            remaining_references.append('more-webflow-templates-sub')
        
        if remaining_references:
            print(f"⚠️  Warning: Found remaining references: {', '.join(remaining_references)}")
            return False
        else:
            print("✅ Verification successful - all syncell references removed!")
            return True
            
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🧹 SYNCELl BADGE REMOVAL SCRIPT")
    print("=" * 60)
    
    success = remove_syncell_badge()
    
    if success:
        verify_removal()
        print("\n" + "=" * 60)
        print("✅ SYNCELl BADGE REMOVAL COMPLETE!")
        print("=" * 60)
        print("\nWhat was removed:")
        print("• More-templates promotional badge HTML element")
        print("• Associated CSS styling")
        print("• All related promotional content")
        print("\nYour homepage is now clean of syncell promotional content!")
        print("\n🚀 Test your site:")
        print("   http://localhost:3000/")
    else:
        print("\n❌ Removal failed. Please check the error messages above.")
