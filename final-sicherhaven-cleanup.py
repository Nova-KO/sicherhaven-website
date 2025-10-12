#!/usr/bin/env python3
"""
Final cleanup script to ensure the site is properly customized for Sicherhaven
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def cleanup_sicherhaven_site():
    """Final cleanup to ensure proper Sicherhaven customization"""
    
    print("🧹 Final Sicherhaven site cleanup...")
    
    # Files to clean up
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
    
    cleaned_count = 0
    
    for file_name in html_files:
        file_path = Path(file_name)
        if not file_path.exists():
            continue
            
        print(f"🔧 Cleaning up {file_name}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove promotional badges and template elements
            content = re.sub(r'<div class="brix-badges-wrapper"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div class="more-templates-badge-wrapper"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<a class="more-templates-badge-wrapper"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
            
            # Remove Syncell logo from logo strip
            content = re.sub(r'<img[^>]*syncell-logo[^>]*/>', '', content)
            content = re.sub(r'<img[^>]*alt="[^"]*Syncell[^"]*"[^>]*/>', '', content)
            
            # Update generic Lorem ipsum content in hero section
            content = re.sub(
                r'<h1 class="text-light">We invest in AI companies shaping the future</h1>',
                '<h1 class="text-light">Building innovative solutions for community events and financial wellness</h1>',
                content
            )
            
            # Update hero description
            content = re.sub(
                r'<p class="text-paragraph-light">Join us in building the future of community events and financial wellness\. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances\.</p>',
                '<p class="text-paragraph-light">Join us in building the future of community events and financial wellness. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances.</p>',
                content
            )
            
            # Update about section
            content = re.sub(
                r'<h2>About our invest firm</h2>',
                '<h2>About Sicherhaven</h2>',
                content
            )
            
            # Update footer description if it still has Lorem ipsum
            content = re.sub(
                r'<p class="text-paragraph-light">Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et vehicula a eget facilisis nec porta interdum lorem pharetra proin ac lacus\.</p>',
                '<p class="text-paragraph-light">Join us in building the future of community events and financial wellness. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances.</p>',
                content
            )
            
            # Update footer links to point to correct pages
            content = re.sub(r'href="/home-pages/home-v1"', 'href="index.html"', content)
            content = re.sub(r'href="/company-pages/about"', 'href="index.html"', content)
            content = re.sub(r'href="/portfolio-pages/portfolio-v1"', 'href="PORTFOLIO.html"', content)
            content = re.sub(r'href="/company-pages/contact"', 'href="Contact.html"', content)
            content = re.sub(r'href="/company-pages/investors"', 'href="INVESTORS.html"', content)
            content = re.sub(r'href="/blog-pages/blog-v1"', 'href="BLOG.html"', content)
            content = re.sub(r'href="/company-pages/coming-soon"', 'href="coming soon.html"', content)
            
            # Write the cleaned content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            cleaned_count += 1
            print(f"✅ Cleaned up {file_name}")
                
        except Exception as e:
            print(f"❌ Error cleaning up {file_name}: {e}")
    
    return cleaned_count

def verify_cleanup():
    """Verify that the cleanup was successful"""
    print("\n🔍 Verifying cleanup...")
    
    # Check index.html for key elements
    try:
        with open("index.html", 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for removed elements
        syncell_count = content.lower().count('syncell')
        brix_count = content.lower().count('brix-badges-wrapper')
        more_templates_count = content.lower().count('more-templates-badge')
        
        print(f"📊 Cleanup verification:")
        print(f"  • Syncell references: {syncell_count}")
        print(f"  • Brix badges: {brix_count}")
        print(f"  • More templates badges: {more_templates_count}")
        
        if syncell_count == 0 and brix_count == 0 and more_templates_count == 0:
            print("✅ All promotional content removed successfully!")
        else:
            print("⚠️  Some promotional content may still remain")
            
    except Exception as e:
        print(f"❌ Error verifying cleanup: {e}")

if __name__ == "__main__":
    print("=" * 70)
    print("🧹 FINAL SICHERHAVEN SITE CLEANUP")
    print("=" * 70)
    
    cleaned_count = cleanup_sicherhaven_site()
    verify_cleanup()
    
    print("\n" + "=" * 70)
    print("🎉 FINAL CLEANUP COMPLETE!")
    print("=" * 70)
    print(f"✅ Cleaned up {cleaned_count} files")
    print("✅ Removed promotional badges and template elements")
    print("✅ Updated content to be Sicherhaven-specific")
    print("✅ Fixed navigation links")
    print("=" * 70)
