
import os
import glob

replacements = {
    # Longest matches first to avoid partial replacements
    "Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et vehicula a eget facilisis nec porta interdum lorem pharetra proin ac lacus.": 
        "Sicherhaven connects communities and empowers financial growth through innovative technology. Our team is dedicated to building a sustainable future.",
        
    "Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et vehicula a eget facilisis nec porta interdum lorem pharetra.": 
        "We are redefining the intersection of finance and community. Our mission is to provide accessible, transparent, and effective tools for everyone.",
        
    "Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et vehicula a eget.": 
        "Discover how Sicherhaven is making a difference in the world of fintech and community engagement.",
        
    "Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et vehicula a eget facilisis nec porta.":
        "Stay updated with the latest news and announcements from Sicherhaven as we continue to grow and innovate.",
        
    "Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing platea tortor magna orci netus.": 
        "An innovative solution designed to enhance user engagement and streamline complex financial operations.",
        
    "Lorem ipsum dolor sit amet consectetur nibh nunc luctus iaculis posuere adipiscing.": 
        "Our strategic location fosters collaboration and innovation, allowing us to serve our global clients effectively.", 
        
    "From portfolio tracking to strategic analysis, their team has amplified our operations. It truly feels like they’re investing in our growth every single day":
        "Sicherhaven's strategic insights and technological support have been pivotal in our expansion. They are true partners in our success.",
        
    "Lorem ipsum dolor sit amet consectetur lacus sed nam varius quis pharetra arcu id amet et": # Short fragment if any
        "Sicherhaven is committed to excellence in every aspect of our business."
}

files = glob.glob('*.php') + glob.glob('*.html')

for filename in files:
    if os.path.isdir(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    new_content = content
    modified = False
    
    for lorem, replacement in replacements.items():
        if lorem in new_content:
            new_content = new_content.replace(lorem, replacement)
            modified = True
            
    if modified:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Replaced placeholders in {filename}")

