import re

css_path = r'C:\Sharm\Sharm\assets\css\responsive.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# I will append a robust flexbox order rule at the very end of responsive.css
# This will guarantee the layout.

robust_css = """
/* ==========================================================
   FORCE MOBILE NAVBAR LAYOUT
   ========================================================== */
@media (max-width: 992px) {
  .navbar .container {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-top: 10px !important;
    padding-bottom: 5px !important;
  }
  
  .navbar-brand {
    order: 1 !important;
    flex: 0 0 auto !important;
  }
  
  .header-right {
    order: 2 !important;
    flex: 0 0 auto !important;
  }
  
  .navbar-menu {
    order: 3 !important;
    position: relative !important; /* NOT static, relative is safer */
    width: 100% !important;
    height: auto !important;
    background: transparent !important;
    padding: 15px 0 5px 0 !important;
    box-shadow: none !important;
    display: flex !important;
    flex-direction: row !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
    gap: 15px !important;
    margin-top: 5px !important;
    border-top: 1px solid rgba(255,255,255,0.1) !important;
    transition: none !important;
    right: auto !important;
    left: auto !important;
    top: auto !important;
  }
  
  .navbar.scrolled .navbar-menu {
    border-top: 1px solid rgba(0,0,0,0.1) !important;
  }

  .navbar-links {
    display: flex !important;
    flex-direction: row !important;
    gap: 10px !important;
    align-items: center !important;
    width: max-content !important;
    padding-bottom: 5px !important; 
    margin: 0 !important;
  }

  .navbar-links a {
    font-size: 0.9rem !important;
    padding: 6px 14px !important;
    background: rgba(255,255,255,0.15) !important;
    border-radius: 20px !important;
    color: var(--white) !important;
    border-bottom: none !important;
    font-weight: 500 !important;
  }

  .navbar.scrolled .navbar-links a {
    background: var(--gray-100) !important;
    color: var(--gray-800) !important;
  }

  .navbar-links a.active {
    background: var(--primary) !important;
    color: var(--white) !important;
  }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + robust_css)

print("Navbar mobile layout forced.")
