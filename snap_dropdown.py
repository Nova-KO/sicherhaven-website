
import re

file_path = 'test.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target the margin-left in the nested-list tag
# From: margin-left: var(--main-spacers--small);
# To: margin-left: 0px;

start_marker = 'class="w-dropdown-list nested-list"'
end_marker = '>'

match = re.search(f'{start_marker}[^>]+{end_marker}', content)

if match:
    full_tag = match.group(0)
    if 'margin-left: var(--main-spacers--small);' in full_tag:
        new_tag = full_tag.replace('margin-left: var(--main-spacers--small);', 'margin-left: 0px;')
        content = content.replace(full_tag, new_tag)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully snapped the product dropdown by removing the margin-left gap.")
    else:
        print("Target margin-left not found in the tag.")
        print(f"Current tag: {full_tag}")
else:
    print("Could not find nested-list tag.")
