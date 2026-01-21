
import os
import glob

files = glob.glob('*.php') + glob.glob('*.html')

for filename in files:
    if os.path.isdir(filename): continue
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # We look for href="css/style.css"
    # We replace it with href="css/style.css?v=<?php echo time(); ?>" if it's a php file, 
    # but some might be just html strings in php.
    # To be safe and since I don't want to break caching completely (cache busting on every reload is inefficient), 
    # I'll just use a static version number that I can increment if needed.
    
    if 'href="css/style.css"' in content:
        new_content = content.replace('href="css/style.css"', 'href="css/style.css?v=2"')
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated style link in {filename}")
    elif "href='css/style.css'" in content:
        new_content = content.replace("href='css/style.css'", "href='css/style.css?v=2'")
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated style link in {filename}")

