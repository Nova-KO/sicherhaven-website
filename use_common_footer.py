
import os
import glob

files = glob.glob('*.php') + glob.glob('*.html')

# We'll skip the footer.php itself, and maybe header files if they don't have footers.
exclude_files = ['footer.php', 'header.php', 'header-dark.php', 'header-light.php']

for filename in files:
    if os.path.isdir(filename) or filename in exclude_files:
        continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Locate the start of the footer container
    start_str = 'class="footer-container"'
    start_pos = content.find(start_str)
    
    if start_pos == -1:
        continue
        
    # Find the actual start of the tag (move backwards to <div)
    tag_start = content.rfind('<div', 0, start_pos)
    if tag_start == -1:
        print(f"Could not find start tag for footer-container in {filename}")
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
        # Check if we are in a PHP file or HTML file.
        # If PHP, we use the include.
        # If HTML, well... the user requested "header of ... index.php is used". index.php is php.
        # So we probably should use the php include if possible. 
        # But if it's an html file, php include won't work unless served as php.
        # Luckily most files are php now.
        
        replacement = "<?php include 'footer.php'; ?>"
        
        # Replace the block
        # Also, check if there was the badge wrapper right after it, we might want to clean that up if strictly adhering to "replace with common footer".
        # But my previous badge remover should have handled it.
        
        new_content = content[:tag_start] + replacement + content[close_pos:]
        
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Replaced footer in {filename}")
    else:
        print(f"Could not find matching closing div for footer-container in {filename}")
