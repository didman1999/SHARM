import re

filepath = r'C:\Sharm\Sharm\transfers.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the vehicle selection section with a dynamic container
replacement = """      <!-- Vehicle Selection -->
      <div id="fleet-container"></div>
"""

content = re.sub(r'<!-- Vehicle Selection -->.*?(?=</section>)', replacement, content, flags=re.DOTALL)

# Add fleet.js script before main.js
if 'assets/js/fleet.js' not in content:
    content = content.replace('<script src="assets/js/main.js"></script>', '<script src="assets/js/fleet.js"></script>\n  <script src="assets/js/main.js"></script>')

# Add rendering logic for fleet
script_logic = """
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const container = document.getElementById('fleet-container');
      if (!container || typeof fleetDatabase === 'undefined') return;

      const currentLang = document.documentElement.lang === 'ar' ? 'ar' : 'en';

      let html = '';
      fleetDatabase.categories.forEach(category => {
        html += `
          <div class="fleet-category" style="margin-bottom: var(--space-10);">
            <div class="section-header" style="text-align: center; margin-bottom: var(--space-6);">
              <h3 style="font-size: var(--text-2xl); color: var(--navy);" data-lang-en="${category.titleEn}" data-lang-ar="${category.titleAr}">${currentLang === 'ar' ? category.titleAr : category.titleEn}</h3>
              <p style="color: var(--gray-500);" data-lang-en="${category.descriptionEn}" data-lang-ar="${category.descriptionAr}">${currentLang === 'ar' ? category.descriptionAr : category.descriptionEn}</p>
            </div>
            <div class="grid grid-3">
        `;

        category.cars.forEach(car => {
          html += `
              <div class="vehicle-card">
                <div class="vehicle-card-image" style="background: url('${car.img}') center/cover; height: 180px;"></div>
                <div class="vehicle-card-body">
                  <h3 data-lang-en="${car.nameEn}" data-lang-ar="${car.nameAr}">${currentLang === 'ar' ? car.nameAr : car.nameEn}</h3>
                  <div class="vehicle-specs">
                    <div class="vehicle-spec"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg><span>${car.pax} ${currentLang === 'ar' ? 'ركاب' : 'passengers'}</span></div>
                    <div class="vehicle-spec"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3h-8l-2 4h12z"/></svg><span>${car.bags} ${currentLang === 'ar' ? 'حقائب' : 'bags'}</span></div>
                  </div>
                  <p style="font-size: var(--text-xs); color: var(--gray-500); margin-bottom: var(--space-3);" data-lang-en="${car.featuresEn}" data-lang-ar="${car.featuresAr}">${currentLang === 'ar' ? car.featuresAr : car.featuresEn}</p>
                  <div class="vehicle-price" style="font-size: 1.1rem; font-weight: bold; color: var(--accent); margin-bottom: 15px;">
                    ${currentLang === 'ar' ? 'يبدأ من $' + car.price : 'From $' + car.price}
                  </div>
                  <div>
                    <a href="book-transfer.html?vehicle=${car.id}" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">${currentLang === 'ar' ? 'اختر السيارة' : 'Select Vehicle'}</a>
                  </div>
                </div>
              </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    });
  </script>
"""

# Append script before </body>
content = content.replace('</body>', script_logic + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
