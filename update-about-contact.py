#!/usr/bin/env python3
"""
Update About and Contact pages with Sicherhaven-specific content
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Define the base directory
BASE_DIR = Path(__file__).parent

def create_about_page():
    """Create a dedicated About page with Sicherhaven content"""
    about_content = '''<!DOCTYPE html>
<html data-wf-domain="sicherhaven.com" data-wf-page="about" data-wf-site="sicherhaven" lang="en">
<head>
    <meta charset="utf-8"/>
    <title>About Us - Sicherhaven | Building the future of community events and financial wellness</title>
    <meta content="Learn about Sicherhaven's mission to create innovative solutions for community events and financial wellness through Eventify and WealthWise." name="description"/>
    <meta content="About Us - Sicherhaven" property="og:title"/>
    <meta content="Learn about Sicherhaven's mission to create innovative solutions for community events and financial wellness." property="og:description"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <style>
        /* Import the same styles from index.html */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #fff;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .section {
            padding: 4rem 0;
        }
        
        .section h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: #333;
            text-align: center;
        }
        
        .section h3 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: #667eea;
        }
        
        .section p {
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            color: #666;
        }
        
        .mission {
            background: #f8f9ff;
            padding: 3rem 0;
        }
        
        .mission-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
        }
        
        .mission-text {
            padding: 2rem;
        }
        
        .mission-image {
            text-align: center;
            font-size: 8rem;
            opacity: 0.7;
        }
        
        .values {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .value-card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .value-card:hover {
            transform: translateY(-5px);
        }
        
        .value-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .team {
            background: #f8f9ff;
        }
        
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .team-member {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .team-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: white;
        }
        
        .cta {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 4rem 0;
        }
        
        .cta h2 {
            color: white;
        }
        
        .cta p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        
        .btn {
            display: inline-block;
            background: white;
            color: #667eea;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .mission-content {
                grid-template-columns: 1fr;
            }
            
            .section h2 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>About Sicherhaven</h1>
            <p>Building innovative solutions for community events and financial wellness</p>
        </div>
        
        <div class="section">
            <h2>Our Mission</h2>
            <div class="mission-content">
                <div class="mission-text">
                    <p>At Sicherhaven, we believe in the power of community and the importance of financial wellness. Our mission is to create innovative technology solutions that connect people with local events and empower them to make better financial decisions.</p>
                    
                    <p>Founded with a vision to bridge the gap between community engagement and financial literacy, we're developing cutting-edge applications that make a real difference in people's lives.</p>
                    
                    <p>We're not just building software – we're building tools that strengthen communities and improve financial outcomes for everyone.</p>
                </div>
                <div class="mission-image">
                    🚀
                </div>
            </div>
        </div>
        
        <div class="section mission">
            <h2>Our Values</h2>
            <div class="values">
                <div class="value-card">
                    <div class="value-icon">🤝</div>
                    <h3>Community First</h3>
                    <p>We believe technology should bring people together, not drive them apart. Every feature we build is designed to strengthen community bonds and create meaningful connections.</p>
                </div>
                
                <div class="value-card">
                    <div class="value-icon">💰</div>
                    <h3>Financial Empowerment</h3>
                    <p>Financial literacy shouldn't be a luxury. We're democratizing access to financial knowledge and tools, helping everyone make informed decisions about their money.</p>
                </div>
                
                <div class="value-card">
                    <div class="value-icon">🎯</div>
                    <h3>User-Centric Design</h3>
                    <p>We put our users at the center of everything we do. Our products are designed to be intuitive, accessible, and genuinely helpful in solving real-world problems.</p>
                </div>
                
                <div class="value-card">
                    <div class="value-icon">🔮</div>
                    <h3>Innovation</h3>
                    <p>We embrace cutting-edge technology to solve age-old problems. From AI-powered financial insights to community-driven event discovery, we're pushing the boundaries of what's possible.</p>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>Our Products</h2>
            <div class="mission-content">
                <div class="mission-text">
                    <h3>Eventify</h3>
                    <p>Our community-powered event discovery platform helps people find local events and gives event organizers better exposure. Whether it's a neighborhood block party, a tech meetup, or a cultural festival, Eventify connects communities through shared experiences.</p>
                    
                    <h3>WealthWise</h3>
                    <p>An AI-powered financial wellness application that helps users understand their finances, track their credit history, optimize their spending, and identify opportunities to save money. We're making financial literacy accessible to everyone.</p>
                </div>
                <div class="mission-image">
                    💡
                </div>
            </div>
        </div>
        
        <div class="section team">
            <h2>Our Team</h2>
            <div class="team-grid">
                <div class="team-member">
                    <div class="team-avatar">👨‍💻</div>
                    <h3>Development Team</h3>
                    <p>Passionate engineers and designers working to build the future of community and financial technology.</p>
                </div>
                
                <div class="team-member">
                    <div class="team-avatar">🎯</div>
                    <h3>Product Team</h3>
                    <p>User experience experts ensuring our products solve real problems for real people.</p>
                </div>
                
                <div class="team-member">
                    <div class="team-avatar">🤝</div>
                    <h3>Community Team</h3>
                    <p>Building relationships with event organizers and financial educators to create meaningful partnerships.</p>
                </div>
            </div>
        </div>
        
        <div class="cta">
            <h2>Join Our Mission</h2>
            <p>Ready to be part of the future of community events and financial wellness?</p>
            <a href="Contact.html" class="btn">Get in Touch</a>
        </div>
    </div>
</body>
</html>'''
    
    return about_content

def update_contact_page():
    """Update the Contact page with Sicherhaven-specific content"""
    print("Updating Contact page...")
    
    try:
        with open('Contact.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Update page title and meta tags
        title_tag = soup.find('title')
        if title_tag:
            title_tag.string = 'Contact Us - Sicherhaven | Get in Touch'
        
        # Find and update meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc:
            meta_desc['content'] = 'Get in touch with Sicherhaven. We are building innovative solutions for community events and financial wellness. Contact us to learn more about Eventify and WealthWise.'
        
        # Update og:title
        og_title = soup.find('meta', {'property': 'og:title'})
        if og_title:
            og_title['content'] = 'Contact Us - Sicherhaven'
        
        # Update og:description
        og_desc = soup.find('meta', {'property': 'og:description'})
        if og_desc:
            og_desc['content'] = 'Get in touch with Sicherhaven. We are building innovative solutions for community events and financial wellness.'
        
        # Find main content sections and update them
        # Look for headings and replace content
        headings = soup.find_all(['h1', 'h2', 'h3'])
        
        for heading in headings:
            text = heading.get_text().strip().lower()
            if 'contact' in text and 'us' in text:
                heading.string = 'Contact Sicherhaven'
            elif 'get' in text and 'touch' in text:
                heading.string = 'Get in Touch'
            elif 'reach' in text and 'out' in text:
                heading.string = 'Reach Out to Us'
        
        # Find paragraphs and update with Sicherhaven content
        paragraphs = soup.find_all('p')
        for i, p in enumerate(paragraphs):
            text = p.get_text().strip()
            if len(text) > 50 and 'investment' in text.lower():
                p.string = "We would love to hear from you! Whether you are interested in learning more about Eventify for community event discovery, WealthWise for financial wellness, or have questions about our mission, we are here to help."
                break
            elif len(text) > 30 and 'lorem' in text.lower():
                p.string = "Ready to connect with our team? Send us a message and we will get back to you within 24 hours."
                break
        
        # Update form labels if they exist
        labels = soup.find_all('label')
        for label in labels:
            text = label.get_text().strip().lower()
            if 'company' in text:
                label.string = 'Company/Organization'
            elif 'message' in text:
                label.string = 'Tell us about your interest in Sicherhaven'
        
        # Write back the updated content
        with open('Contact.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("✓ Contact page updated with Sicherhaven content")
        return True
        
    except Exception as e:
        print(f"✗ Error updating Contact page: {e}")
        return False

def create_about_page_file():
    """Create the About.html page"""
    print("Creating About page...")
    
    try:
        about_content = create_about_page()
        
        with open('About.html', 'w', encoding='utf-8') as f:
            f.write(about_content)
        
        print("✓ About page created successfully")
        return True
        
    except Exception as e:
        print(f"✗ Error creating About page: {e}")
        return False

def update_footer_links():
    """Update footer links to point to About.html instead of index.html"""
    print("Updating footer links...")
    
    try:
        # Read the footer component
        with open('components/footer.html', 'r', encoding='utf-8') as f:
            footer_content = f.read()
        
        # Update the About link to point to About.html
        updated_footer = footer_content.replace('href="index.html"', 'href="About.html"')
        
        # Write back
        with open('components/footer.html', 'w', encoding='utf-8') as f:
            f.write(updated_footer)
        
        print("✓ Footer links updated")
        
        # Now update all HTML files with the new footer
        print("Updating all pages with new footer links...")
        from refactor_components import update_html_file, create_sicherhaven_footer
        
        # Read the updated footer
        with open('components/footer.html', 'r', encoding='utf-8') as f:
            new_footer = f.read()
        
        html_files = list(Path(BASE_DIR).glob('*.html'))
        success_count = 0
        
        for html_file in html_files:
            if html_file.name in ['About.html', '404.html', 'open-pages.html', 'file-index.html']:
                continue  # Skip these files
            
            if update_html_file(html_file, new_footer):
                success_count += 1
        
        print(f"✓ Updated {success_count} pages with new footer links")
        return True
        
    except Exception as e:
        print(f"✗ Error updating footer links: {e}")
        return False

def main():
    print("=" * 60)
    print("Sicherhaven About & Contact Pages Update")
    print("=" * 60)
    print()
    
    # Create About page
    if create_about_page_file():
        print("✅ About page created")
    else:
        print("❌ Failed to create About page")
        return
    
    # Update Contact page
    if update_contact_page():
        print("✅ Contact page updated")
    else:
        print("❌ Failed to update Contact page")
    
    # Update footer links
    if update_footer_links():
        print("✅ Footer links updated")
    else:
        print("❌ Failed to update footer links")
    
    print()
    print("=" * 60)
    print("✅ About & Contact pages update complete!")
    print("=" * 60)
    print()
    print("What was created/updated:")
    print("• ✅ About.html - New dedicated About page")
    print("• ✅ Contact.html - Updated with Sicherhaven content")
    print("• ✅ Footer links - Now point to About.html")
    print()
    print("Next steps:")
    print("1. Start server: ./start-server.sh")
    print("2. Visit About page: http://localhost:8000/About.html")
    print("3. Visit Contact page: http://localhost:8000/Contact.html")
    print()

if __name__ == '__main__':
    main()
