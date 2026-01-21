
import os
import glob
import re

files = glob.glob('*.php') + glob.glob('*.html')
exclude_files = ['faq.php', 'footer.php']

# We want to replace the FAQ section.
# The FAQ section typically is a <section> containing "Frequently asked questions" or similar.
# Since the markup might vary slightly or be identical, we'll search for the keyword and then try to capture the surrounding section.

# Regex to find <section> ... "Frequently asked questions" ... </section>
# This is tricky without a proper parser, but let's assume the structure is relatively standard.
# We'll look for "Frequently asked questions" and walk backwards to <section and forward to </section>.

keyword = "Frequently asked questions"

for filename in files:
    if os.path.isdir(filename) or filename in exclude_files:
        continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if this file has the keyword
    if keyword not in content:
        continue
        
    print(f"Found FAQ keyword in {filename}")
    
    # Locate the keyword
    keyword_pos = content.find(keyword)
    
    # Find the start of the section containing this keyword
    # We assume it's wrapped in a <section> tag
    section_start = content.rfind('<section', 0, keyword_pos)
    if section_start == -1:
        print(f"Could not find start <section> for FAQ in {filename}")
        continue
        
    # Find the end of this section
    # Count open/close section tags
    open_tags = 0
    close_pos = -1
    i = section_start
    length = len(content)
    found_end = False
    
    # We are looking for closing </section>
    while i < length:
        if content[i:].startswith('<section'):
            open_tags += 1
            i += 8
        elif content[i:].startswith('</section>'):
            open_tags -= 1
            i += 10
            if open_tags == 0:
                close_pos = i
                found_end = True
                break
        else:
            i += 1
            
    if found_end:
        # Check if this is indeed the FAQ section by verifying content
        block = content[section_start:close_pos]
        if keyword in block:
            
            # Replace with include
            new_block = "<?php include 'faq.php'; ?>"
            new_content = content[:section_start] + new_block + content[close_pos:]
            
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Replaced FAQ section in {filename}")
        else:
            print(f"Section block did not contain keyword in {filename}")

