import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove the logo from navbar-brand
    content = re.sub(r'<img src="image/LOGO\.jpeg"[^>]*>', '', content)
    
    # Step 2: Ensure the brand-name is LUNA BIANCA
    content = content.replace('LUNA BLANCA', 'LUNA BIANCA')
    content = content.replace('Luna Blanca', 'Luna Bianca')
    content = content.replace('لونا بلانكا', 'لونا بيانكا')

    # Step 3: We need to restructure the navbar.
    # Current structure might have:
    # <div class="header-right"...>
    #   <div class="lang-dropdown">...</div>
    #   <button class="navbar-toggle"...>...</button>
    # </div>
    
    # Let's extract the lang-dropdown
    lang_dropdown_match = re.search(r'<div class="lang-dropdown">.*?</div>', content, re.DOTALL)
    if not lang_dropdown_match:
        print(f"No lang-dropdown in {file}, skipping restructuring")
        continue
        
    lang_dropdown = lang_dropdown_match.group(0)
    
    # Remove it from header-right
    content = content.replace(lang_dropdown, '')
    
    # Now we insert the lang-dropdown in the center, and the logo in header-right
    # Find the navbar-brand closing tag
    brand_end_idx = content.find('</a>', content.find('class="navbar-brand"')) + 4
    
    center_html = f'\n      <div class="header-center" style="position: absolute; left: 50%; transform: translateX(-50%); z-index: 10;">\n        {lang_dropdown}\n      </div>'
    
    # Insert center_html after </a>
    content = content[:brand_end_idx] + center_html + content[brand_end_idx:]
    
    # Now add the logo to header-right, right before navbar-toggle
    logo_html = '<img src="image/LOGO.jpeg" class="logo" style="mix-blend-mode: multiply; border-radius: 50%; object-fit: cover; width: 42px; height: 42px;" alt="Luna Bianca">'
    content = content.replace('<button class="navbar-toggle"', f'{logo_html}\n        <button class="navbar-toggle"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navbar layout.")
