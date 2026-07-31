import os

css_path = r'C:\Sharm\Sharm\assets\css\responsive.css'

mobile_css = """
/* ==========================================================
   TRANSFER WIDGET MOBILE RESPONSIVE
   ========================================================== */
@media (max-width: 992px) {
  .hero-container-redesign {
    padding-top: 140px; /* clear the new navbar */
  }

  .transfer-widget-container {
    padding: 15px;
    margin-top: 15px;
  }

  .details-grid {
    grid-template-columns: 1fr 1fr;
  }
  
  .details-grid .input-group:last-child {
    grid-column: 1 / -1; /* Flight number full width */
  }

  .return-grid {
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .locations-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }
  
  .details-grid .input-group:last-child {
    grid-column: auto;
  }

  .transfer-type-selector {
    grid-template-columns: 1fr;
  }
  
  .transfer-type-selector .card-content {
    flex-direction: row;
    justify-content: flex-start;
    padding: 10px 15px;
  }
  
  .transfer-type-selector .card-content .emoji {
    font-size: 1.4rem;
  }

  .direction-selector, .trip-type-selector {
    flex-direction: column;
    gap: 10px;
  }
  
  .widget-footer {
    flex-direction: column;
    gap: 10px;
    align-items: center;
  }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + mobile_css)

print("Transfer widget mobile CSS appended successfully.")
