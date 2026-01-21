
import os
import glob
import re

files = glob.glob('*.php') + glob.glob('*.html')

# We want to replace any link that looks like:
# <link href="https://cdn.prod.website-files.com/.../css/....css" ...>
# with
# <link href="css/style.css?v=3" rel="stylesheet" type="text/css"/>

# Regex to match the href specifically
remote_css_pattern = re.compile(r'href="https://cdn\.prod\.website-files\.com/[^"]+\.css"')

for filename in files:
    if os.path.isdir(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    if remote_css_pattern.search(content):
        # We replace the entire match with our local file
        # Note the pattern matches `href="..."`. 
        new_content = remote_css_pattern.sub('href="css/style.css?v=3"', content)
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Replaced remote CSS in {filename}")
    else:
        # Also let's standardize even if it was local but without cache busting or older version
        if 'href="css/style.css"' in content or "href='css/style.css'" in content:
             # Just update valid local links to v3
             new_content = content.replace('href="css/style.css"', 'href="css/style.css?v=3"')
             new_content = new_content.replace("href='css/style.css'", "href='css/style.css?v=3'")
             # Handle previous v2
             new_content = new_content.replace('href="css/style.css?v=2"', 'href="css/style.css?v=3"')
             new_content = new_content.replace("href='css/style.css?v=2'", "href='css/style.css?v=3'")
             
             if new_content != content:
                with open(filename, 'w') as f:
                    f.write(new_content)
                print(f"Updated local CSS version in {filename}")

