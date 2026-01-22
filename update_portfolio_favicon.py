
import os
import glob

# Update PORTFOLIO.php with proper descriptions
with open('PORTFOLIO.php', 'r') as f:
    content = f.read()

# Update Eventify description
eventify_old_desc = "An innovative solution designed to enhance user engagement and streamline complex financial operations."
eventify_new_desc = "A community event management platform that connects people through local events, making it easy to discover, create, and participate in community activities."

# We need to be careful - only replace the first occurrence for Eventify
# Find the Eventify section and replace
eventify_pos = content.find('Eventify</h2>')
if eventify_pos != -1:
    # Find the description after Eventify
    desc_start = content.find(eventify_old_desc, eventify_pos)
    if desc_start != -1 and desc_start < eventify_pos + 500:  # within reasonable range
        content = content[:desc_start] + eventify_new_desc + content[desc_start + len(eventify_old_desc):]

# Update Wealthwise description
wealthwise_old_desc = "An innovative solution designed to enhance user engagement and streamline complex financial operations."
wealthwise_new_desc = "An AI-powered financial wellness app that helps users understand and improve their financial health through personalized insights, credit monitoring, and expense tracking."

wealthwise_pos = content.find('Wealthwise</h2>')
if wealthwise_pos != -1:
    desc_start = content.find(wealthwise_old_desc, wealthwise_pos)
    if desc_start != -1 and desc_start < wealthwise_pos + 500:
        content = content[:desc_start] + wealthwise_new_desc + content[desc_start + len(wealthwise_old_desc):]

with open('PORTFOLIO.php', 'w') as f:
    f.write(content)

print("Updated PORTFOLIO.php with new descriptions")

# Now update favicon across all pages
files = glob.glob('*.php') + glob.glob('*.html')

favicon_replacements = [
    ('href="https://cdn.prod.website-files.com/686b7d020ea82bd1ba5003a8/686b7f3bbd8388a55d8ad668_favicon-equity-webflow-template.svg"', 'href="favicon.svg"'),
    ('href="favicon.png"', 'href="favicon.svg"'),
    ("href='favicon.png'", "href='favicon.svg'"),
    ('type="image/png"', 'type="image/svg+xml"'),
    ("type='image/png'", "type='image/svg+xml'"),
]

for filename in files:
    if os.path.isdir(filename):
        continue
        
    with open(filename, 'r') as f:
        content = f.read()
    
    modified = False
    new_content = content
    
    for old, new in favicon_replacements:
        if old in new_content:
            new_content = new_content.replace(old, new)
            modified = True
    
    if modified:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated favicon in {filename}")

