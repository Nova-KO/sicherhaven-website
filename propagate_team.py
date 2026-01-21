
import os

# 1. Extract the team section from index.php
with open('index.php', 'r') as f:
    index_content = f.read()

# Locate the team section in index.php
# It starts with <div class="mg-top-regular"> and contains "Founding Partner" or similar team keywords 
# to distinguish it from other mg-top-regular blocks (testimonials, etc.)

# The previous view_file showed it starts at line 554 in index.php
# <div class="mg-top-regular">
# <div class="inner-container---925px center">
# ...

start_marker = '<div class="mg-top-regular">'
team_keyword = 'Founding Partner'

start_pos = 0
team_block = ""

while True:
    start_pos = index_content.find(start_marker, start_pos)
    if start_pos == -1:
        break
    
    # Find the end of this div block
    open_divs = 1
    i = start_pos + len(start_marker)
    length = len(index_content)
    
    while i < length and open_divs > 0:
        if index_content[i:i+4] == '<div':
            open_divs += 1
            i += 4
        elif index_content[i:i+6] == '</div>':
            open_divs -= 1
            i += 6
        else:
            i += 1
            
    block_content = index_content[start_pos:i]
    
    if team_keyword in block_content:
        team_block = block_content
        break
    
    start_pos = i # Continue searching

if not team_block:
    print("Could not find team section in index.php")
    exit(1)

print("Found team section in index.php")

# 2. Replace in likely target files
target_files = ['our-team.php', 'about.php', 'INVESTORS.php']

for filename in target_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r') as f:
        content = f.read()
    
    # We look for the same structure to replace: <div class="mg-top-regular"> containing team members
    # OR if the user wants to replace *any* team section, we might need to be broader.
    # But usually it's the same class structure.
    
    # We will search for mg-top-regular blocks that look like the team section (contain similar classes or keywords)
    # OR just replace the main team list if we can identify it.
    
    # specific logic for our-team.php: likely the main mg-top-regular list
    
    new_content = content
    current_pos = 0
    modified = False
    
    # We construct a new content string
    final_content = ""
    last_pos = 0
    
    # Iterate through all mg-top-regular blocks
    while True:
        start_idx = content.find(start_marker, current_pos)
        if start_idx == -1:
            final_content += content[last_pos:]
            break
            
        # Add content up to this block
        final_content += content[last_pos:start_idx]
        
        # Find end of this block
        open_divs = 1
        i = start_idx + len(start_marker)
        length = len(content)
        while i < length and open_divs > 0:
            if content[i:i+4] == '<div':
                open_divs += 1
                i += 4
            elif content[i:i+6] == '</div>':
                open_divs -= 1
                i += 6
            else:
                i += 1
        
        block = content[start_idx:i]
        
        # Decide if this block should be replaced
        # Criteria: contains "Founding Partner" OR "w-dyn-list" (if generic) AND is in a relevant file?
        # To be safe, let's strictly look for team indicators if matching existing content.
        # But if the existing content is empty or different, how do we know?
        # The user said "wherever the team is mentioned".
        
        if "Founding Partner" in block or "Nafih Najeeb" in block or "w-dyn-list" in block: 
            # This is a weak heuristic for "w-dyn-list" generally, but combined with the filename context it likely fits.
            # However, simpler: if it has "Founding Partner" it is definitely the one to replace.
            
            # Additional check: our-team.php definitely has it.
            if "Founding Partner" in block or "w-dyn-list" in block:
                 final_content += team_block
                 modified = True
                 print(f"Replaced team block in {filename}")
            else:
                 final_content += block
        else:
            final_content += block
            
        last_pos = i
        current_pos = i

    if modified:
        with open(filename, 'w') as f:
            f.write(final_content)
    else:
        print(f"No matching team block found to replace in {filename}")

