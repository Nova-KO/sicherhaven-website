
import os
import glob

# Standard footer bottom content
standard_footer = '<p>Copyright © 2024 Sicherhaven | Designed by <a href="https://bshtech.net" target="_blank" class="text-link">BSH Technologies</a></p>'

files = glob.glob('*.php') + glob.glob('*.html')

for filename in files:
    if os.path.isdir(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Locate the start of footer-bottom
    start_str = 'class="footer-bottom"'
    start_pos = content.find(start_str)
    
    if start_pos == -1:
        # Maybe it's defined differently or not present
        continue
        
    # Find the actual start of the tag (move backwards to <div)
    tag_start = content.rfind('<div', 0, start_pos)
    if tag_start == -1:
        print(f"Could not find start tag for footer-bottom in {filename}")
        continue
    
    # Find the matching closing div
    open_divs = 0
    close_pos = -1
    i = tag_start
    length = len(content)
    found_end = False
    
    while i < length:
        if content[i:].startswith('<div'):
            open_divs += 1
            i += 4
        elif content[i:].startswith('</div>'):
            open_divs -= 1
            i += 6
            if open_divs == 0:
                close_pos = i 
                found_end = True
                break
        else:
            i += 1
            
    if found_end:
        # Reconstruct the div with standard content
        # We prefer to keep the original class definition in case there were other classes, 
        # but here we know it is <div class="footer-bottom"> usually.
        # To be safe, let's keep the opening tag as is.
        
        # Extract opening tag
        opening_tag_end = content.find('>', tag_start) + 1
        opening_tag = content[tag_start:opening_tag_end]
        
        # New block
        new_block = f"{opening_tag}{standard_footer}</div>"
        
        new_content = content[:tag_start] + new_block + content[close_pos:]
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Updated footer copyright in {filename}")
    else:
        print(f"Could not find matching closing div for footer-bottom in {filename}")
