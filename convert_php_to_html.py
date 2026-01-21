
import os
import re
import glob

def process_php_includes(content, base_dir='.'):
    """Replace PHP includes with actual file content"""
    # Pattern to match PHP includes
    pattern = r"<\?php\s+include\s+['\"]([^'\"]+)['\"]\s*;\s*\?>"
    
    def replace_include(match):
        include_file = match.group(1)
        include_path = os.path.join(base_dir, include_file)
        
        if os.path.exists(include_path):
            with open(include_path, 'r', encoding='utf-8') as f:
                included_content = f.read()
            # Recursively process includes in the included file
            included_content = process_php_includes(included_content, base_dir)
            return included_content
        else:
            print(f"  Warning: Include file not found: {include_path}")
            return match.group(0)  # Keep original if file not found
    
    # Replace all includes
    result = re.sub(pattern, replace_include, content)
    return result

def convert_php_to_html(php_file, output_dir='.'):
    """Convert a PHP file to HTML by processing includes"""
    with open(php_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process PHP includes
    content = process_php_includes(content, os.path.dirname(php_file) or '.')
    
    # Generate HTML filename
    base_name = os.path.basename(php_file)
    html_name = base_name.replace('.php', '.html')
    html_path = os.path.join(output_dir, html_name)
    
    # Update internal links from .php to .html
    content = content.replace('.php"', '.html"')
    content = content.replace(".php'", ".html'")
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted: {php_file} -> {html_path}")

# Get all PHP files in current directory
php_files = glob.glob('*.php')
# Exclude include files (header, footer, etc.)
exclude = ['header.php', 'header-dark.php', 'header-light.php', 'footer.php', 'faq.php', 'locations.php']
php_files = [f for f in php_files if f not in exclude]

print(f"Found {len(php_files)} PHP files to convert")
for php_file in php_files:
    convert_php_to_html(php_file)

# Also convert blog PHP files
blog_php_files = glob.glob('blogs/*.php')
for php_file in blog_php_files:
    convert_php_to_html(php_file, 'blogs')

print("\nDone! PHP files converted to HTML.")
