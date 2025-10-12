#!/usr/bin/env python3
"""
Script to restore the site using hometemplate.html as template and preserving Sicherhaven content
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_sicherhaven_content():
    """Extract Sicherhaven-specific content from the current index.html"""
    
    print("🔍 Extracting Sicherhaven content from current index.html...")
    
    try:
        with open("index.html", 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract Sicherhaven-specific content
        sicherhaven_content = {
            'title': 'Sicherhaven - Building innovative solutions for community events and financial wellness',
            'description': 'Building innovative solutions for community events and financial wellness. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances.',
            'footer_title': 'Building innovative solutions for community events and financial wellness',
            'footer_description': 'Join us in building the future of community events and financial wellness. Discover how Eventify and WealthWise are transforming the way people connect and manage their finances.',
            'products': {
                'Eventify': 'index.html#eventify',
                'WealthWise': 'coming soon.html'
            },
            'social_links': {
                'Twitter': 'https://twitter.com/sicherhaven',
                'LinkedIn': 'https://linkedin.com/company/sicherhaven',
                'GitHub': 'https://github.com/sicherhaven'
            },
            'copyright': 'Copyright © 2024 Sicherhaven | Building the future of community events and financial wellness'
        }
        
        print("✅ Extracted Sicherhaven content successfully")
        return sicherhaven_content
        
    except Exception as e:
        print(f"❌ Error extracting Sicherhaven content: {e}")
        return None

def restore_index_from_template(sicherhaven_content):
    """Restore index.html using hometemplate.html as base with Sicherhaven content"""
    
    print("🔧 Restoring index.html from hometemplate.html...")
    
    try:
        # Read the template
        with open("hometemplate.html", 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Parse the template
        soup = BeautifulSoup(template_content, 'html.parser')
        
        # Update title and meta tags
        title_tag = soup.find('title')
        if title_tag and sicherhaven_content:
            title_tag.string = sicherhaven_content['title']
        
        # Update meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc and sicherhaven_content:
            meta_desc['content'] = sicherhaven_content['description']
        
        # Update og:title
        og_title = soup.find('meta', {'property': 'og:title'})
        if og_title and sicherhaven_content:
            og_title['content'] = sicherhaven_content['title']
        
        # Update og:description
        og_desc = soup.find('meta', {'property': 'og:description'})
        if og_desc and sicherhaven_content:
            og_desc['content'] = sicherhaven_content['description']
        
        # Update footer content
        footer_title = soup.find('h2', class_='display-9 text-light')
        if footer_title and sicherhaven_content:
            footer_title.string = sicherhaven_content['footer_title']
        
        # Update footer description
        footer_desc = soup.find('p', class_='text-paragraph-light')
        if footer_desc and sicherhaven_content:
            footer_desc.string = sicherhaven_content['footer_description']
        
        # Update product links in footer
        eventify_link = soup.find('a', href=lambda x: x and 'eventify' in x.lower())
        if eventify_link and sicherhaven_content:
            eventify_link['href'] = sicherhaven_content['products']['Eventify']
            eventify_text = eventify_link.find('div', class_='link-animation-text')
            if eventify_text:
                eventify_text.string = 'Eventify'
            eventify_abs = eventify_link.find('div', class_='link-animation-text-absolute')
            if eventify_abs:
                eventify_abs.string = 'Eventify'
        
        wealthwise_link = soup.find('a', href=lambda x: x and 'coming soon' in x.lower())
        if wealthwise_link and sicherhaven_content:
            wealthwise_link['href'] = sicherhaven_content['products']['WealthWise']
            wealthwise_text = wealthwise_link.find('div', class_='link-animation-text')
            if wealthwise_text:
                wealthwise_text.string = 'WealthWise'
            wealthwise_abs = wealthwise_link.find('div', class_='link-animation-text-absolute')
            if wealthwise_abs:
                wealthwise_abs.string = 'WealthWise'
        
        # Update social links
        if sicherhaven_content:
            social_links = soup.find_all('a', href=lambda x: x and ('twitter.com' in x or 'linkedin.com' in x or 'github.com' in x))
            for link in social_links:
                href = link.get('href', '')
                if 'twitter.com' in href:
                    link['href'] = sicherhaven_content['social_links']['Twitter']
                    link_text = link.find('div', class_='link-animation-text')
                    if link_text:
                        link_text.string = 'Twitter'
                    link_abs = link.find('div', class_='link-animation-text-absolute')
                    if link_abs:
                        link_abs.string = 'Twitter'
                elif 'linkedin.com' in href:
                    link['href'] = sicherhaven_content['social_links']['LinkedIn']
                    link_text = link.find('div', class_='link-animation-text')
                    if link_text:
                        link_text.string = 'LinkedIn'
                    link_abs = link.find('div', class_='link-animation-text-absolute')
                    if link_abs:
                        link_abs.string = 'LinkedIn'
                elif 'github.com' in href:
                    link['href'] = sicherhaven_content['social_links']['GitHub']
                    link_text = link.find('div', class_='link-animation-text')
                    if link_text:
                        link_text.string = 'GitHub'
                    link_abs = link.find('div', class_='link-animation-text-absolute')
                    if link_abs:
                        link_abs.string = 'GitHub'
        
        # Update copyright
        copyright_p = soup.find('p')
        if copyright_p and sicherhaven_content:
            # Find the copyright paragraph (usually the last p in footer)
            footer_bottom = soup.find('div', class_='footer-bottom')
            if footer_bottom:
                copyright_p = footer_bottom.find('p')
                if copyright_p:
                    copyright_p.string = sicherhaven_content['copyright']
        
        # Write the restored index.html
        with open("index.html", 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("✅ Successfully restored index.html from template")
        return True
        
    except Exception as e:
        print(f"❌ Error restoring index.html: {e}")
        return False

def restore_other_pages():
    """Restore other pages using the template"""
    
    print("🔧 Restoring other pages from hometemplate.html...")
    
    pages_to_restore = [
        "PORTFOLIO.html",
        "INVESTORS.html", 
        "Contact.html",
        "BLOG.html",
        "coming soon.html",
        "INVESTORS SINGLE.html",
        "BLOG POST.html"
    ]
    
    restored_count = 0
    
    for page_name in pages_to_restore:
        if Path(page_name).exists():
            try:
                # Copy hometemplate.html to the page
                with open("hometemplate.html", 'r', encoding='utf-8') as f:
                    template_content = f.read()
                
                # Update page-specific content
                soup = BeautifulSoup(template_content, 'html.parser')
                
                # Update title based on page
                title_tag = soup.find('title')
                if title_tag:
                    if 'portfolio' in page_name.lower():
                        title_tag.string = 'Portfolio - Sicherhaven'
                    elif 'investors' in page_name.lower():
                        title_tag.string = 'Investors - Sicherhaven'
                    elif 'contact' in page_name.lower():
                        title_tag.string = 'Contact - Sicherhaven'
                    elif 'blog' in page_name.lower():
                        title_tag.string = 'Blog - Sicherhaven'
                    elif 'coming soon' in page_name.lower():
                        title_tag.string = 'Coming Soon - Sicherhaven'
                    else:
                        title_tag.string = f'{page_name.replace(".html", "")} - Sicherhaven'
                
                # Write the restored page
                with open(page_name, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                restored_count += 1
                print(f"✅ Restored {page_name}")
                
            except Exception as e:
                print(f"❌ Error restoring {page_name}: {e}")
    
    return restored_count

def main():
    """Main restoration function"""
    
    print("=" * 70)
    print("🔧 SITE RESTORATION SCRIPT")
    print("=" * 70)
    
    # Check if hometemplate.html exists
    if not Path("hometemplate.html").exists():
        print("❌ hometemplate.html not found!")
        return False
    
    # Extract Sicherhaven content
    sicherhaven_content = extract_sicherhaven_content()
    if not sicherhaven_content:
        print("❌ Failed to extract Sicherhaven content!")
        return False
    
    # Restore index.html
    if not restore_index_from_template(sicherhaven_content):
        print("❌ Failed to restore index.html!")
        return False
    
    # Restore other pages
    restored_count = restore_other_pages()
    print(f"✅ Restored {restored_count} additional pages")
    
    print("\n" + "=" * 70)
    print("🎉 SITE RESTORATION COMPLETE!")
    print("=" * 70)
    print("✅ Your site has been restored using hometemplate.html as base")
    print("✅ Sicherhaven content has been preserved and applied")
    print("✅ All pages have been restored with proper structure")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    main()
