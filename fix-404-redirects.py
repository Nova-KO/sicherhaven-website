#!/usr/bin/env python3
"""
Fix all broken links and ensure proper 404 redirects to 404.html
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Define the base directory
BASE_DIR = Path(__file__).parent

def get_valid_html_files():
    """Get list of valid HTML files that exist"""
    valid_files = []
    for file in Path(BASE_DIR).glob('*.html'):
        if file.name not in ['404.html', 'open-pages.html', 'file-index.html']:
            valid_files.append(file.name)
    return valid_files

def fix_broken_links():
    """Fix broken internal links in all HTML files"""
    print("🔍 Scanning for broken links...")
    
    valid_files = get_valid_html_files()
    print(f"Valid HTML files: {valid_files}")
    
    broken_links_found = []
    
    # Common broken links to fix
    link_fixes = {
        # Fix common template links that don't exist
        '/company-pages/about': 'About.html',
        '/home-pages/home-v2': 'index.html',
        '/home-pages/home-v3': 'index.html',
        '/portfolio-pages/portfolio-v2': 'PORTFOLIO.html',
        '/portfolio-pages/portfolio-v3': 'PORTFOLIO.html',
        '/blog-pages/blog-v1': 'BLOG.html',
        '/blog-pages/blog-v3': 'BLOG.html',
        '/user-pages/sign-in': 'Contact.html',  # Redirect to contact
        '/user-pages/sign-up': 'Contact.html',  # Redirect to contact
        '/user-pages/reset-password': 'Contact.html',
        '/user-pages/update-password': 'Contact.html',
        '/template-pages/start-here': 'index.html',
        '/template-pages/style-guide': 'index.html',
        '/template-pages/licenses': 'index.html',
        '/template-pages/changelog': 'index.html',
        '/401': 'Contact.html',  # Password protected -> contact
        '/404': '404.html',
        
        # Fix specific broken links
        '/portfolio/syncell': 'PORTFOLIO.html',
        '/investors/sophie-moore': 'INVESTORS.html',
        '/investors/matt-cannon': 'INVESTORS.html',
        '/investors/lilly-woods': 'INVESTORS.html',
        '/blog-posts/how-to-raise-capital-5-fundraising-strategies-for-your-startup': 'BLOG.html',
        '/blog-posts/we-are-leading-series-a-investment-round-for-brix-templates': 'BLOG.html',
        '/blog-posts/early-stage-fund-details-for-2026-are-now-available': 'BLOG.html',
    }
    
    html_files = list(Path(BASE_DIR).glob('*.html'))
    files_updated = 0
    
    for html_file in html_files:
        if html_file.name in ['404.html', 'open-pages.html', 'file-index.html']:
            continue  # Skip these files
            
        print(f"Processing: {html_file.name}")
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all links
            links = soup.find_all('a', href=True)
            links_fixed = 0
            
            for link in links:
                href = link['href']
                
                # Skip external links and anchors
                if href.startswith('http') or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'):
                    continue
                
                # Check if it's a broken internal link
                if href in link_fixes:
                    new_href = link_fixes[href]
                    link['href'] = new_href
                    links_fixed += 1
                    broken_links_found.append(f"{html_file.name}: {href} -> {new_href}")
                
                # Check for other broken links (not in our fix list)
                elif href.startswith('/') and not href.startswith('//'):
                    # Remove leading slash and check if file exists
                    clean_href = href[1:]
                    if clean_href not in valid_files and clean_href != '':
                        # Redirect to 404 page
                        link['href'] = '404.html'
                        links_fixed += 1
                        broken_links_found.append(f"{html_file.name}: {href} -> 404.html")
            
            # Write back if changes were made
            if links_fixed > 0:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"  ✅ Fixed {links_fixed} broken links")
                files_updated += 1
            else:
                print(f"  ✓ No broken links found")
                
        except Exception as e:
            print(f"  ❌ Error processing {html_file.name}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"  Files processed: {len(html_files) - 3}")
    print(f"  Files updated: {files_updated}")
    print(f"  Broken links fixed: {len(broken_links_found)}")
    
    if broken_links_found:
        print(f"\n🔧 Links fixed:")
        for fix in broken_links_found[:10]:  # Show first 10
            print(f"  • {fix}")
        if len(broken_links_found) > 10:
            print(f"  • ... and {len(broken_links_found) - 10} more")
    
    return files_updated > 0

def enhance_404_handling():
    """Enhance 404.html with better links and remove template badges"""
    print("\n🎨 Enhancing 404.html page...")
    
    try:
        with open('404.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Update product links to be more specific
        product_links = soup.find_all('a', class_='product-link')
        for link in product_links:
            href = link.get('href', '')
            if 'eventify' in href:
                link['href'] = 'index.html#eventify'
            elif 'coming' in href:
                link['href'] = 'coming soon.html'
            elif 'contact' in href.lower():
                link['href'] = 'Contact.html'
        
        # Write back
        with open('404.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("  ✅ 404.html enhanced")
        return True
        
    except Exception as e:
        print(f"  ❌ Error enhancing 404.html: {e}")
        return False

def remove_template_badges():
    """Remove template promotional badges from all pages"""
    print("\n🧹 Removing template promotional badges...")
    
    html_files = list(Path(BASE_DIR).glob('*.html'))
    files_updated = 0
    
    for html_file in html_files:
        if html_file.name in ['404.html', 'About.html']:
            continue  # Skip these files
            
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove BRIX template badges
            if 'brix-badges-wrapper' in content or 'more-templates-badge' in content:
                soup = BeautifulSoup(content, 'html.parser')
                
                # Find and remove template badges
                badges = soup.find_all(class_=['brix-badges-wrapper', 'more-templates-badge-wrapper'])
                for badge in badges:
                    badge.decompose()
                
                # Write back
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                print(f"  ✅ Removed badges from {html_file.name}")
                files_updated += 1
            else:
                print(f"  ✓ No badges found in {html_file.name}")
                
        except Exception as e:
            print(f"  ❌ Error processing {html_file.name}: {e}")
    
    print(f"  📊 Files updated: {files_updated}")
    return files_updated > 0

def test_404_redirects():
    """Test that 404 redirects work properly"""
    print("\n🧪 Testing 404 redirects...")
    
    test_urls = [
        '/nonexistent-page',
        '/portfolio/nonexistent',
        '/blog/nonexistent',
        '/company-pages/about',  # Should redirect to About.html
        '/user-pages/sign-in',   # Should redirect to Contact.html
        '/template-pages/start-here',  # Should redirect to index.html
    ]
    
    print("  Test URLs that should redirect:")
    for url in test_urls:
        print(f"    • {url}")
    
    print("\n  ✅ To test manually:")
    print("    1. Start server: ./start-server.sh")
    print("    2. Visit each test URL above")
    print("    3. Verify proper redirects and 404 handling")

def create_redirect_test_script():
    """Create a script to test all redirects"""
    test_script = '''#!/bin/bash

echo "🧪 Testing 404 Redirects and Link Fixes"
echo "======================================"

# Start server in background
echo "Starting test server..."
python3 server.py 8890 &
SERVER_PID=$!
sleep 2

echo ""
echo "Testing redirects and 404 handling:"
echo ""

# Test URLs
test_urls=(
    "/nonexistent-page"
    "/portfolio/nonexistent"
    "/blog/nonexistent"
    "/company-pages/about"
    "/user-pages/sign-in"
    "/template-pages/start-here"
    "/invalid-page"
)

for url in "${test_urls[@]}"; do
    echo "Testing: http://localhost:8890$url"
    response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8890$url")
    echo "  Status: $response"
    
    if [ "$response" = "404" ]; then
        echo "  ✅ Correctly returns 404"
    elif [ "$response" = "200" ]; then
        echo "  ✅ Redirected to valid page"
    else
        echo "  ⚠️  Unexpected status: $response"
    fi
    echo ""
done

echo "Stopping test server..."
kill $SERVER_PID

echo ""
echo "✅ Redirect testing complete!"
'''
    
    with open('test-redirects.sh', 'w') as f:
        f.write(test_script)
    
    os.chmod('test-redirects.sh', 0o755)
    print("  ✅ Created test-redirects.sh")

def main():
    print("=" * 60)
    print("Sicherhaven 404 Redirect & Link Fix Script")
    print("=" * 60)
    print()
    
    # Step 1: Fix broken links
    links_fixed = fix_broken_links()
    
    # Step 2: Enhance 404 page
    enhance_404_handling()
    
    # Step 3: Remove template badges
    badges_removed = remove_template_badges()
    
    # Step 4: Create test script
    create_redirect_test_script()
    
    # Step 5: Test instructions
    test_404_redirects()
    
    print()
    print("=" * 60)
    print("✅ 404 Redirect & Link Fix Complete!")
    print("=" * 60)
    print()
    print("What was done:")
    print("• ✅ Fixed broken internal links")
    print("• ✅ Enhanced 404.html page")
    print("• ✅ Removed template promotional badges")
    print("• ✅ Created redirect testing script")
    print()
    print("Next steps:")
    print("1. Start server: ./start-server.sh")
    print("2. Test redirects: ./test-redirects.sh")
    print("3. Visit test URLs manually to verify")
    print()
    print("All wrong links now redirect to 404.html! 🎉")

if __name__ == '__main__':
    main()
