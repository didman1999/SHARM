import os
import re

# 1. Update hotels.js
js_path = r'C:\Sharm\Sharm\assets\js\hotels.js'
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'areaEn: "Airport",': 'areaEn: "Airport",\n    basePrice: 10,',
    'areaEn: "Naama Bay",': 'areaEn: "Naama Bay",\n    basePrice: 15,',
    'areaEn: "SOHO Square / Sharks Bay",': 'areaEn: "SOHO Square / Sharks Bay",\n    basePrice: 20,',
    'areaEn: "Nabq Bay",': 'areaEn: "Nabq Bay",\n    basePrice: 25,',
    'areaEn: "Hadaba & Ras Um Sid",': 'areaEn: "Hadaba & Ras Um Sid",\n    basePrice: 20,',
    'areaEn: "Montazah & Ras Nasrani",': 'areaEn: "Montazah & Ras Nasrani",\n    basePrice: 22,',
    'areaEn: "Old Market & Sharm El Maya",': 'areaEn: "Old Market & Sharm El Maya",\n    basePrice: 20,',
    'areaEn: "Other Destinations",': 'areaEn: "Other Destinations",\n    basePrice: 30,'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update index.html
html_path = r'C:\Sharm\Sharm\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

price_display_html = """
            <div id="priceDisplayContainer" style="display:none; text-align: center; margin: 15px 0; padding: 15px; background: rgba(251,140,0,0.1); border-radius: var(--radius-md); border: 1px dashed var(--accent);">
              <span style="font-size: 1.1rem; font-weight: 600; color: var(--navy);" data-lang-en="Estimated Total:" data-lang-ar="الإجمالي التقديري:">Estimated Total:</span>
              <span id="priceValue" style="font-size: 1.8rem; font-weight: 800; color: var(--accent); margin-left: 10px;">$0</span>
            </div>
            
            <button type="submit" """

html_content = html_content.replace('<button type="submit" ', price_display_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)


# 3. Update transfer.js
transfer_js_path = r'C:\Sharm\Sharm\assets\js\transfer.js'
with open(transfer_js_path, 'r', encoding='utf-8') as f:
    tjs = f.read()

price_logic = """
  // Pricing Logic
  function calculatePrice() {
    const pickupVal = pickupInput.value;
    const dropoffVal = dropoffInput.value;
    
    let pickupPrice = 0;
    let dropoffPrice = 0;
    
    sharmHotels.forEach(area => {
      area.hotels.forEach(h => {
        if (h.en === pickupVal || h.ar === pickupVal) pickupPrice = area.basePrice;
        if (h.en === dropoffVal || h.ar === dropoffVal) dropoffPrice = area.basePrice;
      });
    });

    let basePrice = 0;
    let direction = 'hotel_to_hotel';
    directionInputs.forEach(rad => { if(rad.checked) direction = rad.value; });

    if (direction === 'airport_to_hotel') {
        basePrice = dropoffPrice;
    } else if (direction === 'hotel_to_airport') {
        basePrice = pickupPrice;
    } else {
        basePrice = Math.max(pickupPrice, dropoffPrice) + 5; 
    }

    if (!basePrice || basePrice === 0) return 0;

    let vehicleMult = 1;
    let vehicle = 'taxi';
    document.querySelectorAll('input[name="vehicle"]').forEach(r => { if(r.checked) vehicle = r.value; });
    if (vehicle === 'limousine') vehicleMult = 1.5;
    if (vehicle === 'private') vehicleMult = 2;

    let tripMult = 1;
    let tripTypeVal = 'one_way';
    document.querySelectorAll('input[name="trip_type"]').forEach(r => { if(r.checked) tripTypeVal = r.value; });
    if (tripTypeVal === 'round_trip') tripMult = 2;

    return Math.round(basePrice * vehicleMult * tripMult);
  }

  function updatePriceDisplay() {
    const price = calculatePrice();
    const container = document.getElementById('priceDisplayContainer');
    const valueEl = document.getElementById('priceValue');
    if (container && valueEl) {
      if (price > 0) {
          container.style.display = 'block';
          valueEl.textContent = '$' + price;
      } else {
          container.style.display = 'none';
      }
    }
  }

  // Attach price updates to inputs
  form.addEventListener('change', updatePriceDisplay);
  pickupInput.addEventListener('blur', () => setTimeout(updatePriceDisplay, 250));
  dropoffInput.addEventListener('blur', () => setTimeout(updatePriceDisplay, 250));

"""

# Insert price logic before Form Submission
tjs = tjs.replace('// 5. Form Submission', price_logic + '\n  // 5. Form Submission')

# Update Whatsapp message string to include Price
tjs = tjs.replace('const encodedMsg = encodeURIComponent(message);', 
                  'const estPrice = calculatePrice();\n    if (estPrice > 0) {\n      if (currentLang === "ar") message += `\\n💰 السعر التقديري: $${estPrice}`;\n      else message += `\\n💰 Estimated Price: $${estPrice}`;\n    }\n\n    const encodedMsg = encodeURIComponent(message);')

with open(transfer_js_path, 'w', encoding='utf-8') as f:
    f.write(tjs)

print("Pricing added successfully.")
