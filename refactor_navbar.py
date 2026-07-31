import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the navbar-links div
    links_match = re.search(r'<div class="navbar-links">.*?</div>', content, re.DOTALL)
    if not links_match:
        print(f"Skipping {file} - no navbar links found")
        continue
    navbar_links = links_match.group(0)

    # New container content
    new_container = f"""
    <div class="container">
      <a href="index.html" class="navbar-brand">
        <img src="image/LOGO.jpeg" class="logo" alt="Luna Bianca">
        <div class="brand-text">
          <span class="brand-name" data-lang-en="LUNA BIANCA" data-lang-ar="لونا بيانكا">LUNA BIANCA</span>
          <span class="brand-tagline" data-lang-en="Discover the Red Sea" data-lang-ar="اكتشف البحر الأحمر">Discover the Red Sea</span>
        </div>
      </a>

      <div class="navbar-menu" id="navbarMenu">
        {navbar_links}
      </div>

      <div class="header-right">
        <div class="lang-dropdown">
          <select id="langSelect" class="lang-select" aria-label="Select Language">
            <option value="en">English</option>
            <option value="ar">العربية</option>
            <option value="ru">Русский</option>
            <option value="it">Italiano</option>
            <option value="tr">Türkçe</option>
            <option value="he">עברית</option>
            <option value="fr">Français</option>
            <option value="es">Español</option>
          </select>
        </div>
        
        <a href="trips.html" class="navbar-cta">
          <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span data-lang-en="Book Now" data-lang-ar="احجز الآن" class="cta-text">Book Now</span>
        </a>

        <button class="navbar-toggle" id="navbarToggle" aria-label="Toggle navigation">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
"""

    # Replace the entire <nav ...> ... </nav> EXCEPT the opening and closing nav tag.
    # We will match <div class="container"> inside nav to its closing </div> which is right before </nav>
    
    # We can use regex to replace from <div class="container"> up to </nav>
    # Find <nav class="navbar"...>
    nav_start = content.find('<nav class="navbar')
    nav_close = content.find('</nav>', nav_start)
    if nav_start != -1 and nav_close != -1:
        # we need to keep <nav ...> tag
        first_child = content.find('<div class="container">', nav_start)
        if first_child != -1:
            # Reconstruct content
            content = content[:first_child] + new_container.strip() + "\n  </nav>" + content[nav_close+6:]
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
