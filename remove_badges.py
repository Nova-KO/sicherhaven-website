
import os
import glob
import re

# 1. Remove "Made in Webflow" badge via CSS
css_file = 'css/style.css'
if os.path.exists(css_file):
    with open(css_file, 'a') as f:
        f.write('\n/* Hide Made in Webflow Badge */\n.w-webflow-badge { display: none !important; }\n')
    print("Added CSS to hide Webflow badge.")

# 2. Remove brix-badges-wrapper from all files
files = glob.glob('*.php') + glob.glob('*.html')

# We'll look for <div ... class="brix-badges-wrapper"> and remove everything until the closing div.
# Because the content inside is complex, we will use a regex or a simple stack-based parser if nested divs are an issue.
# However, looking at the file content, the structure is:
# <div ... class="brix-badges-wrapper">
#    ... content ...
# </div>
# The indentation suggests it might be a direct child of body or similar, but let's check for nested divs.
# The content inside `brix-badges-wrapper` contains `div`s (e.g., `more-templates-logo-wrapper`, `hidden-code`).
# So a simple regex might fail if it stops at the first </div>.
# We need to count braces.

for filename in files:
    if os.path.isdir(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Locate the start of the wrapper
    start_pos = content.find('class="brix-badges-wrapper"')
    if start_pos == -1:
        continue
    
    # Find the actual start of the tag (move backwards to <div)
    # We assume it looks like <div ... class="brix-badges-wrapper">
    # We'll search backwards for '<div' from start_pos
    tag_start = content.rfind('<div', 0, start_pos)
    if tag_start == -1:
        print(f"Could not find start tag for brix-badges-wrapper in {filename}")
        continue
        
    # Now find the matching closing div
    # We will scan forward from tag_start, counting <div> and </div>
    open_divs = 0
    close_pos = -1
    
    # We'll iterate through the string starting from tag_start
    i = tag_start
    length = len(content)
    
    found_end = False
    
    while i < length:
        # Check for opening div
        if content[i:].startswith('<div'):
            open_divs += 1
            i += 4
        # Check for closing div
        elif content[i:].startswith('</div>'):
            open_divs -= 1
            i += 6
            if open_divs == 0:
                close_pos = i # i has advanced past </div>
                found_end = True
                break
        else:
            i += 1
            
    if found_end:
        # Remove the block
        # check if there's a trailing newline to remove strictly empty lines
        to_remove = content[tag_start:close_pos]
        new_content = content[:tag_start] + content[close_pos:]
        
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Removed brix-badges-wrapper from {filename}")
    else:
        print(f"Could not find matching closing div for brix-badges-wrapper in {filename}")

