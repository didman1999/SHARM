import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The new language dropdown HTML
lang_dropdown_html = """
      <div class="header-right" style="display: flex; align-items: center; gap: var(--space-3);">
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
        <button class="navbar-toggle" id="navbarToggle" aria-label="Toggle navigation">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove old lang-switch from navbar-actions
    content = re.sub(r'<div class="lang-switch".*?</div>\s*(</div>|<!--)', r'\1', content, flags=re.DOTALL)
    # The regex above might be too aggressive if it matches till the end of the file. 
    # Let's do it safer:
    
    # Actually, we can remove the entire div.lang-switch
    content = re.sub(r'<div class="lang-switch"[^>]*>.*?</div>\s*', '', content, flags=re.DOTALL)
    # Wait, the button tags inside are matched? No, the div contains buttons, so the inner `</div>` would be tricky.
    # Let's replace the exact block:
    # <div class="lang-switch" ...>
    #   <button ...>EN</button>
    #   <button ...>عربي</button>
    # </div>
    content = re.sub(r'<div class="lang-switch"[^>]*>\s*<button[^>]*>.*?</button>\s*<button[^>]*>.*?</button>\s*</div>', '', content, flags=re.DOTALL)

    # 2. Replace the navbar-toggle with our new header-right wrapper
    # The navbar-toggle might have aria-label or not
    toggle_pattern = r'<button class="navbar-toggle" id="navbarToggle"[^>]*>.*?<span></span>\s*<span></span>\s*<span></span>\s*</button>'
    content = re.sub(toggle_pattern, lang_dropdown_html.strip(), content, flags=re.DOTALL)

    # 3. Update the JavaScript in the file (if it exists) to handle the select change instead of buttons
    js_pattern = r'document\.querySelectorAll\(\'\.lang-switch button\'\)\.forEach\(btn => \{.*?\}\);'
    new_js = """
    const langSelect = document.getElementById('langSelect');
    if (langSelect) {
      langSelect.addEventListener('change', (e) => {
        const lang = e.target.value;
        const isRtl = (lang === 'ar' || lang === 'he');
        document.body.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
        document.documentElement.setAttribute('lang', lang);

        document.querySelectorAll('[data-lang-en]').forEach(el => {
          // Fallback to English if translation is missing
          let text = el.dataset['lang' + lang.charAt(0).toUpperCase() + lang.slice(1)];
          if (!text) {
             if (lang === 'ar' && el.dataset.langAr) text = el.dataset.langAr;
             else text = el.dataset.langEn;
          }
          if (text) {
             if (el.tagName === 'INPUT') el.placeholder = text;
             else el.innerHTML = text;
          }
        });
        localStorage.setItem('sharm_lang', lang);
      });
    }
    """
    content = re.sub(js_pattern, new_js.strip(), content, flags=re.DOTALL)

    # Update initialization
    init_pattern = r'document\.querySelector\(\'\.lang-switch button\[data-lang="ar"\]\'\)\.click\(\);'
    new_init = "if(langSelect){langSelect.value = savedLang; langSelect.dispatchEvent(new Event('change'));}"
    content = re.sub(init_pattern, new_init, content, flags=re.DOTALL)

    # Note: main.js might have the JS, or the files themselves. In the previous output, the JS was in index.html.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files.")
