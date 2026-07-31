import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Increase logo size in HTML inline styles (remove inline width/height to let CSS handle it, or increase it)
    content = content.replace('width: 42px; height: 42px;', 'width: 55px; height: 55px;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated logo size in HTML.")
