
import os

with open('PORTFOLIO.php', 'r') as f:
    content = f.read()

# Update Eventify card with new logo and correct info
content = content.replace(
    'src="https://wubflow-shield.NOCODEXPORT.DEV/686b7d020ea82bd1ba5003b1/686bf9992d7e4e9f2a1a1dbc_converra-logo-equity-webflow-template.svg"',
    'src="img/eventify-logo.png"'
)
content = content.replace('>Eventify<', '>EventifyPlus<')
content = content.replace('>Q2 2026<', '>Q1 2026<')
content = content.replace(
    'A community event management platform that connects people through local events, making it easy to discover, create, and participate in community activities.',
    "Kerala's premier hyperlocal event discovery platform connecting you with local festivals, cultural performances, and community gatherings."
)

# Update Wealthwise card with new logo and correct info
content = content.replace(
    'src="https://wubflow-shield.NOCODEXPORT.DEV/686b7d020ea82bd1ba5003b1/686bf9623211842a0ab26d79_nexora-logo-equity-webflow-template.svg"',
    'src="img/wealthwise-logo.png"'
)
content = content.replace('>Q3 2025<', '>Early 2026<')
content = content.replace('>2025<', '>2026<')

with open('PORTFOLIO.php', 'w') as f:
    f.write(content)

print("Updated PORTFOLIO.php with new logos and info")
