import os

with open(r'd:\Sharm\assets\css\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Update .navbar-brand .logo to remove width override if any
# Let's completely overwrite .navbar-brand .logo and .header-right styling

css_update = """
.navbar-brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  z-index: 20;
  flex-shrink: 0;
}

.navbar-brand .logo {
  flex-shrink: 0;
  width: 55px;
  height: 55px;
  mix-blend-mode: multiply;
  border-radius: 50%;
  object-fit: contain;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  flex: 1;
  justify-content: center;
}

.header-right {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  flex-shrink: 0;
  z-index: 20;
}

.lang-dropdown {
  flex-shrink: 0;
}

.lang-select {
  appearance: none;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  color: var(--white);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: var(--space-2) var(--space-6) var(--space-2) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition);
  outline: none;
  background-image: url('data:image/svg+xml;utf8,<svg fill="white" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 16px;
  min-width: 110px;
}
.navbar.scrolled .lang-select {
  background-color: var(--gray-100);
  color: var(--gray-600);
  border-color: var(--gray-200);
  background-image: url('data:image/svg+xml;utf8,<svg fill="%234B5563" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>');
}
"""

content += "\n" + css_update

with open(r'd:\Sharm\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated style.css")
