import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

svg_pattern = re.compile(r'<svg class="logo"[^>]*>.*?</svg>', re.DOTALL)
new_logo = '<img src="image/LOGO.jpeg" class="logo" style="mix-blend-mode: multiply; border-radius: 50%; object-fit: cover; width: 42px; height: 42px;" alt="Luna Blanca">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the SVG logo
    content = svg_pattern.sub(new_logo, content)
    
    # Replace Sharm Excursions with LUNA BLANCA
    content = content.replace('Sharm Excursions', 'LUNA BLANCA')
    content = content.replace('شرم للرحلات', 'لونا بلانكا')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated all HTML files.")
