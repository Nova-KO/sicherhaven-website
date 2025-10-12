#!/usr/bin/env python3
"""
Sicherhaven Template Refactoring Script
Extracts header and footer into common components and updates all HTML pages
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import glob

# Define the base directory
BASE_DIR = Path(__file__).parent

def extract_header(html_content):
    """Extract header section from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the header wrapper (typically starts at beginning of body and ends before main content)
    # Looking for common patterns in the template
    header_end_markers = [
        'class="section hero',
        'class="page-wrapper"',
        '<section',
    ]
    
    # Extract everything from body start to first section
    body_tag = soup.find('body')
    if not body_tag:
        return None
    
    # Get the page-wrapper div which contains header
    page_wrapper = soup.find('div', class_='page-wrapper')
    if page_wrapper:
        # Extract header-wrapper-absolute or header element
        header_section = page_wrapper.find('div', class_='header-wrapper-absolute')
        if not header_section:
            header_section = page_wrapper.find('div', class_='hero-wrapper')
        
        if header_section:
            # Find just the header part (before hero content)
            header = header_section.find('div', class_='header-wrapper-absolute')
            if header:
                return str(header)
    
    # Fallback: extract by regex
    match = re.search(r'(<div[^>]*class="[^"]*header-wrapper[^"]*"[^>]*>.*?</div>)', html_content, re.DOTALL)
    if match:
        return match.group(1)
    
    return None

def extract_footer(html_content):
    """Extract footer section from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find footer container
    footer = soup.find('div', class_='footer-container')
    if footer:
        return str(footer)
    
    # Fallback: extract by regex
    match = re.search(r'(<div[^>]*class="[^"]*footer-container[^"]*"[^>]*>.*?</div></div></div>)', html_content, re.DOTALL)
    if match:
        return match.group(1)
    
    return None

def create_sicherhaven_footer():
    """Create a custom Sicherhaven-specific footer"""
    return '''<div class="footer-container">
    <div data-w-id="f1ff1ac2-5ccd-56f8-612a-0570791caa19" class="footer-main-section">
        <div class="w-layout-blockcontainer container-default w-container">
            <div class="footer-top v1">
                <div class="inner-container _556px center">
                    <h2 class="display-9 text-light">Building innovative solutions for community events and financial wellness</h2>
                    <div class="mg-top-2x-extra-small">
                        <div class="inner-container _620px center">
                            <p class="text-paragraph-light">Join us in building the future of community events and financial wellness. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances.</p>
                        </div>
                    </div>
                    <div class="mg-top-2x-extra-small">
                        <div class="buttons-row wrap">
                            <a id="w-node-_99805214-dd54-e7f3-2549-05c0df1040fb-df1040fb" data-wf--primary-button--variant="base" data-w-id="99805214-dd54-e7f3-2549-05c0df1040fb" href="Contact.html" class="primary-button w-inline-block">
                                <div class="button-content-flex gap-0">
                                    <div>Get started</div>
                                    <div class="button-icon-wrapper">
                                        <div class="button-icon">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="14px" viewBox="0 0 16 15" fill="none" class="button-arrow">
                                                <path d="M7.8589 0.996826L14.1772 7.02789M14.1772 7.02789L7.8589 13.059M14.1772 7.02789L1.87854 7.02789" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                            </svg>
                                        </div>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-layout-grid footer-middle">
                <div id="w-node-f1ff1ac2-5ccd-56f8-612a-0570791caa49-791caa18">
                    <h3 class="footer-pages-title">Our Products</h3>
                    <div class="grid-1-column footer-pages-grid">
                        <a href="index.html#eventify" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">Eventify</div>
                            <div class="link-animation-text-absolute">Eventify</div>
                        </a>
                        <a href="coming soon.html" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">WealthWise</div>
                            <div class="link-animation-text-absolute">WealthWise</div>
                        </a>
                    </div>
                </div>
                <div id="w-node-f1ff1ac2-5ccd-56f8-612a-0570791caa7f-791caa18">
                    <h3 class="footer-pages-title">Company</h3>
                    <div class="grid-1-column footer-pages-grid">
                        <a href="index.html" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">About</div>
                            <div class="link-animation-text-absolute">About</div>
                        </a>
                        <a href="Contact.html" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">Contact</div>
                            <div class="link-animation-text-absolute">Contact</div>
                        </a>
                        <a href="BLOG.html" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">Blog</div>
                            <div class="link-animation-text-absolute">Blog</div>
                        </a>
                    </div>
                </div>
                <div id="w-node-_32480fc1-bfca-a1c5-00f4-a04a3808812d-791caa18">
                    <h3 class="footer-pages-title">Connect</h3>
                    <div class="grid-1-column footer-pages-grid">
                        <a href="https://twitter.com/sicherhaven" target="_blank" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">Twitter</div>
                            <div class="link-animation-text-absolute">Twitter</div>
                        </a>
                        <a href="https://linkedin.com/company/sicherhaven" target="_blank" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">LinkedIn</div>
                            <div class="link-animation-text-absolute">LinkedIn</div>
                        </a>
                        <a href="https://github.com/sicherhaven" target="_blank" class="link-animation-wrapper w-inline-block">
                            <div class="link-animation-text">GitHub</div>
                            <div class="link-animation-text-absolute">GitHub</div>
                        </a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>Copyright © 2024 Sicherhaven | Building the future of community events and financial wellness</p>
            </div>
        </div>
    </div>
</div>'''

def update_html_file(file_path, footer_html):
    """Update an HTML file with the new footer"""
    print(f"Processing: {file_path.name}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Use BeautifulSoup for more reliable parsing
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find and replace footer
        footer_container = soup.find('div', class_='footer-container')
        
        if footer_container:
            # Parse new footer HTML
            new_footer_soup = BeautifulSoup(footer_html, 'html.parser')
            new_footer = new_footer_soup.find('div', class_='footer-container')
            
            # Replace the old footer with new one
            footer_container.replace_with(new_footer)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print(f"  ✓ Updated footer")
            return True
        else:
            print(f"  ⚠ No footer found, skipping")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def fix_server_404():
    """Fix the server.py 404 handling issue"""
    server_path = BASE_DIR / 'server.py'
    
    if not server_path.exists():
        print("server.py not found, skipping server fix")
        return
    
    with open(server_path, 'r') as f:
        content = f.read()
    
    # The server.py already looks correct, but let's ensure the working directory is set
    fixed_content = content.replace(
        'def run_server(port=8000):',
        '''def run_server(port=8000):
    """Run the custom HTTP server"""
    # Change to script directory to ensure relative paths work
    os.chdir(os.path.dirname(os.path.abspath(__file__)))'''
    )
    
    # Only write if changed
    if fixed_content != content:
        with open(server_path, 'w') as f:
            f.write(fixed_content)
        print("✓ Fixed server.py to handle 404 errors correctly")
    else:
        print("✓ server.py already configured correctly")

def main():
    print("=" * 60)
    print("Sicherhaven Template Refactoring Script")
    print("=" * 60)
    print()
    
    # Get all HTML files
    html_files = list(Path(BASE_DIR).glob('*.html'))
    
    if not html_files:
        print("No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files")
    print()
    
    # Create Sicherhaven-specific footer
    print("Creating Sicherhaven-specific footer...")
    footer_html = create_sicherhaven_footer()
    print("✓ Footer component created")
    print()
    
    # Save components to separate files for reference
    components_dir = BASE_DIR / 'components'
    components_dir.mkdir(exist_ok=True)
    
    with open(components_dir / 'footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_html)
    print(f"✓ Saved footer component to {components_dir / 'footer.html'}")
    print()
    
    # Update all HTML files
    print("Updating all HTML files with new footer...")
    print("-" * 60)
    
    success_count = 0
    for html_file in html_files:
        if html_file.name.startswith('.'):
            continue  # Skip hidden files
        
        if update_html_file(html_file, footer_html):
            success_count += 1
    
    print("-" * 60)
    print(f"Successfully updated {success_count}/{len(html_files)} files")
    print()
    
    # Fix server 404 handling
    print("Fixing server 404 handling...")
    fix_server_404()
    print()
    
    print("=" * 60)
    print("✓ Refactoring complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Start the server: ./start-server.sh")
    print("2. Visit http://localhost:8000/")
    print("3. Test 404 page: http://localhost:8000/nonexistent-page")
    print()

if __name__ == '__main__':
    main()

