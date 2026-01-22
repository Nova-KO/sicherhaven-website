
import os
import glob

# Find files with locations/offices sections and replace with include
files_to_update = ['our-team.php', 'contact-us.php']

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r') as f:
        content = f.read()
    
    # Look for the offices section
    # It typically starts with: <div class="section-wrapper"><section class="card-section">
    # and contains "Visit our locations" or "Offices"
    
    start_marker = 'class="text-color-neutral-400">Offices</div>'
    
    if start_marker not in content:
        print(f"No offices section found in {filename}")
        continue
        
    # Find the start of the section-wrapper containing this
    marker_pos = content.find(start_marker)
    
    # Go back to find <div class="section-wrapper">
    section_start = content.rfind('<div class="section-wrapper">', 0, marker_pos)
    if section_start == -1:
        # Try alternate: just card-section
        section_start = content.rfind('<section class="card-section">', 0, marker_pos)
        if section_start == -1:
            print(f"Could not find section start in {filename}")
            continue
            
    # Find the end - it's typically </section></div>
    # We need to count div/section tags properly
    # For simplicity, let's find the next occurrence of </section></div> after the marker
    section_end = content.find('</section></div>', marker_pos)
    if section_end == -1:
        print(f"Could not find section end in {filename}")
        continue
        
    section_end += len('</section></div>')
    
    # Replace with include
    new_content = content[:section_start] + "<?php include 'locations.php'; ?>" + content[section_end:]
    
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Replaced offices section with include in {filename}")

