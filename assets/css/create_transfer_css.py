import os

css_path = r'C:\Sharm\Sharm\assets\css\style.css'

widget_css = """
/* ==========================================================
   TRANSFER WIDGET STYLES
   ========================================================== */
.hero-container-redesign {
  z-index: 2;
  position: relative;
  width: 100%;
}

.transfer-widget-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: var(--radius-xl);
  padding: 25px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  margin-top: 30px;
  text-align: left;
  border: 1px solid rgba(255,255,255,0.4);
}

body[dir="rtl"] .transfer-widget-container {
  text-align: right;
}

.transfer-widget .widget-row {
  margin-bottom: 20px;
}

/* Radio Cards (Vehicle Type) */
.transfer-type-selector {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.transfer-type-selector label {
  cursor: pointer;
  position: relative;
}

.transfer-type-selector input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

.transfer-type-selector .card-content {
  background: var(--gray-100);
  border: 2px solid transparent;
  border-radius: var(--radius-lg);
  padding: 15px 10px;
  text-align: center;
  transition: all var(--transition);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--gray-800);
  font-weight: 600;
  font-size: 0.95rem;
}

.transfer-type-selector .card-content .emoji {
  font-size: 1.8rem;
}

.transfer-type-selector input:checked ~ .card-content {
  background: var(--navy);
  border-color: var(--navy);
  color: var(--white);
  box-shadow: var(--shadow-md);
}

/* Text Radio (Direction & Trip Type) */
.direction-selector, .trip-type-selector {
  display: flex;
  gap: 20px;
  border-bottom: 1px solid var(--gray-200);
  padding-bottom: 15px;
  flex-wrap: wrap;
}

.direction-selector label, .trip-type-selector label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: 500;
  color: var(--gray-800);
  font-size: 0.95rem;
}

.direction-selector input[type="radio"], .trip-type-selector input[type="radio"] {
  accent-color: var(--accent);
  width: 18px;
  height: 18px;
}

/* Grids */
.locations-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 15px;
}

.return-grid {
  grid-template-columns: repeat(2, 1fr);
  max-width: 40%;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--gray-600);
}

.input-group input[type="text"],
.input-group input[type="date"],
.input-group input[type="time"],
.input-group input[type="number"] {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid var(--gray-300);
  border-radius: var(--radius-md);
  font-size: 1rem;
  background: var(--white);
  color: var(--gray-800);
  transition: border-color var(--transition);
}

.input-group input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(251, 140, 0, 0.1);
}

.input-group input:disabled {
  background: var(--gray-100);
  cursor: not-allowed;
  opacity: 0.8;
}

/* Custom Dropdown */
.custom-dropdown {
  position: relative;
}

.dropdown-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--white);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  max-height: 250px;
  overflow-y: auto;
  z-index: 100;
  display: none;
  margin-top: 5px;
}

.dropdown-list.active {
  display: block;
}

.dropdown-group-label {
  padding: 10px 15px;
  font-weight: 700;
  background: var(--gray-50);
  color: var(--navy);
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.dropdown-item {
  padding: 12px 15px;
  cursor: pointer;
  transition: background var(--transition);
  font-size: 0.95rem;
  color: var(--gray-800);
  border-bottom: 1px solid var(--gray-100);
}

.dropdown-item:last-child {
  border-bottom: none;
}

.dropdown-item:hover {
  background: rgba(251, 140, 0, 0.1);
  color: var(--accent);
}

/* Footer */
.widget-footer {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-top: 20px;
  color: var(--gray-600);
  font-size: 0.85rem;
  font-weight: 500;
  flex-wrap: wrap;
}

.booking-success {
  text-align: center;
  padding: 30px;
  color: var(--navy);
}

.booking-success svg {
  margin-bottom: 15px;
}

.booking-success h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: var(--success);
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + widget_css)

print("Transfer widget CSS appended successfully.")
