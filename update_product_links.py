
import os
import glob
import re

# Files to update
files = ['index.php', 'faq.php', 'footer.php', 'header-dark.php', 'header-light.php', 'header.php', 'internal-container-925px.php', 'our-team.php']

for filename in files:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    original = content
    
    # Look for links/buttons near Eventify mentions that don't already point to eventify-app.php
    # Find href patterns that should point to eventify-app.php
    # Common patterns: href="/portfolio" href="/contact" href="contact-us.php" near Eventify
    
    # For the homepage, the "Discover Eventify" or similar buttons
    # Check if there are generic links that should be updated
    
    # Pattern 1: Links in sections mentioning Eventify should go to eventify-app.php
    # Pattern 2: Links in sections mentioning Wealthwise should go to wealthwise.php
    
    modified = False
    
    with open(filename, 'w') as f:
        f.write(content)

print("Checking files for Eventify/Wealthwise mentions...")

# Check index.php for product section links
with open('index.php', 'r') as f:
    content = f.read()

# Find product cards and update their links
# The index.php likely has product cards linking to generic pages

# Look for the products section and update links
# This would require understanding the specific structure

print("index.php content check complete")
print("Files that mention Eventify/Wealthwise:")
for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        if 'Eventify' in content or 'Wealthwise' in content or 'WealthWise' in content:
            # Count mentions
            eventify_count = content.count('Eventify')
            wealthwise_count = content.count('Wealthwise') + content.count('WealthWise')
            print(f"  {filename}: Eventify={eventify_count}, Wealthwise={wealthwise_count}")
