import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

cta_html = """        <div class="navbar-actions">
          <a href="trips.html" class="navbar-cta">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <span data-lang-en="Book Now" data-lang-ar="احجز الآن">Book Now</span>
          </a>
        </div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The empty navbar-actions looks like:
    #         <div class="navbar-actions">
    #           </div>
    content = content.replace('        <div class="navbar-actions">\n          </div>', cta_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored navbar-cta.")
