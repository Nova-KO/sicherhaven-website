
import re

with open('PORTFOLIO.php', 'r') as f:
    content = f.read()

# Replace Converra with Eventify
# We need to be careful to replace the display text and links/images if possible, or at least the text.
# The user asked "make the 2 products as Eventify and Wealthwise"

# Strategy:
# 1. Find the first portfolio item (Converra) and update its title and description.
# 2. Find the second portfolio item (Nexora) and update its title and description.

# Locate Converra Block
# <h2 class="display-5">Converra</h2>
if 'Converra' in content:
    content = content.replace('Converra', 'Eventify')
    # Also update the description if needed, or leave generic?
    # "An innovative solution designed to enhance user engagement..." -> Keep as is since I updated it recently.
    
# Locate Nexora Block
# <h2 class="display-5">Nexora</h2>
if 'Nexora' in content:
    content = content.replace('Nexora', 'Wealthwise')

# Update dates if needed? The user didn't specify, but "Eventify" is Q2 2026? "Wealthwise" is Q3 2025?
# Let's assume dates are fine or user will ask to change them.

# Also update the links? href="/portfolio/converra" -> href="/eventify-app.php"
content = content.replace('href="/portfolio/converra"', 'href="/eventify-app.php"')
content = content.replace('href="/portfolio/eventify"', 'href="/eventify-app.php"') # In case it was already replaced

# Update Wealthwise link? href="/portfolio/nexora" -> href="/wealthwise.php"
content = content.replace('href="/portfolio/nexora"', 'href="/wealthwise.php"')
content = content.replace('href="/portfolio/wealthwise"', 'href="/wealthwise.php"')

with open('PORTFOLIO.php', 'w') as f:
    f.write(content)

print("Updated PORTFOLIO.php")
