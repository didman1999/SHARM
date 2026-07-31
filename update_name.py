import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace English and Arabic names
    content = content.replace('LUNA BLANCA', 'LUNA BIANCA')
    content = content.replace('Luna Blanca', 'Luna Bianca')
    content = content.replace('لونا بلانكا', 'لونا بيانكا')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated name to LUNA BIANCA.")
