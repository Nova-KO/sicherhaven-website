#!/usr/bin/env python3
"""
Script to remove the Syncell logo from the logo strip section in index.html
"""

import re
from pathlib import Path

def remove_syncell_logo():
    """Remove the Syncell logo from the logo strip section"""
    
    index_file = Path("index.html")
    if not index_file.exists():
        print("❌ index.html not found!")
        return False
    
    print("🧹 Removing Syncell logo from logo strip section...")
    
    try:
        # Read the file
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Remove the Syncell logo img tag from the logo strip
        # This pattern matches the img tag with syncell-logo in the src
        syncell_logo_pattern = r'<img[^>]*syncell-logo[^>]*/>'
        content = re.sub(syncell_logo_pattern, '', content, flags=re.IGNORECASE)
        
        # Also remove any img tags that contain "Syncell Logo" in the alt text
        syncell_alt_pattern = r'<img[^>]*alt="[^"]*Syncell[^"]*"[^>]*/>'
        content = re.sub(syncell_alt_pattern, '', content, flags=re.IGNORECASE)
        
        # Clean up any extra whitespace or empty lines
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Write the cleaned content back
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        new_length = len(content)
        removed_chars = original_length - new_length
        
        print(f"✅ Successfully removed Syncell logo from logo strip!")
        print(f"   • Removed {removed_chars:,} characters")
        print(f"   • File size reduced from {original_length:,} to {new_length:,} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error removing Syncell logo: {e}")
        return False

def verify_removal():
    """Verify that the Syncell logo has been removed"""
    print("\n🔍 Verifying Syncell logo removal...")
    
    index_file = Path("index.html")
    if not index_file.exists():
        print("❌ index.html not found for verification!")
        return False
    
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for remaining Syncell references
        remaining_references = []
        
        if 'syncell-logo' in content.lower():
            remaining_references.append('syncell-logo')
        
        if 'syncell logo' in content.lower():
            remaining_references.append('Syncell Logo')
            
        if 'syncell' in content.lower() and 'logo' in content.lower():
            remaining_references.append('syncell logo reference')
        
        if remaining_references:
            print(f"⚠️  Warning: Found remaining Syncell references: {', '.join(remaining_references)}")
            return False
        else:
            print("✅ Verification successful - all Syncell logo references removed!")
            return True
            
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🧹 SYNCELl LOGO REMOVAL SCRIPT")
    print("=" * 60)
    
    success = remove_syncell_logo()
    
    if success:
        verify_removal()
        print("\n" + "=" * 60)
        print("✅ SYNCELl LOGO REMOVAL COMPLETE!")
        print("=" * 60)
        print("\nWhat was removed:")
        print("• Syncell logo from logo strip section")
        print("• All Syncell logo image references")
        print("• Associated alt text and attributes")
        print("\nYour homepage logo strip is now clean of Syncell!")
        print("\n🚀 Test your site:")
        print("   http://localhost:3000/")
    else:
        print("\n❌ Removal failed. Please check the error messages above.")
