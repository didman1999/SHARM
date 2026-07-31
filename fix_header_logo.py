import os
import re

with open(r'd:\Sharm\assets\css\responsive.css', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to remove the previous "Mobile & Tablet Responsive Nav Fixes" entirely
# from responsive.css, and put the new correct version.
# Let's use regex to find and remove it.

pattern = r'/\* Mobile & Tablet Responsive Nav Fixes \*/.*?(?=\z|/\* --- Print Styles --- \*/|/\* ============================================================)'
# Wait, it's at the end of the file.
pattern = r'/\* Mobile & Tablet Responsive Nav Fixes \*/.*'

content = re.sub(pattern, '', content, flags=re.DOTALL)

new_css = """/* Mobile & Tablet Responsive Nav Fixes */
@media (max-width: 992px) {
  .navbar .container {
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
  }

  .navbar-brand {
    order: 1;
    flex-shrink: 0;
    margin-bottom: 0;
  }

  .header-right {
    order: 2;
    display: flex;
    align-items: center;
    gap: var(--space-3);
    flex-shrink: 0;
    z-index: 15; /* Above mobile menu which is z-index 5 */
  }

  .header-right .logo {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    flex-shrink: 0 !important;
    width: 45px !important;
    height: 45px !important;
    z-index: 15;
  }

  .header-center {
    order: 3;
    width: 100%;
    position: static !important;
    transform: none !important;
    margin: 15px 0 0 0;
    display: flex;
    justify-content: center;
    flex-shrink: 0;
    z-index: 10;
  }
}

@media (max-width: 576px) {
  .navbar-brand .brand-name {
    font-size: 1.2rem;
  }
  .navbar-brand .brand-tagline {
    display: none;
  }
  .header-right .logo {
    width: 38px !important;
    height: 38px !important;
  }
  .header-center {
    margin: 10px 0 0 0;
  }
}
"""

content = content.strip() + "\n\n" + new_css

with open(r'd:\Sharm\assets\css\responsive.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated responsive header CSS.")
