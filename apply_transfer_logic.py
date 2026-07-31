import re

filepath = r'C:\Sharm\Sharm\assets\js\transfer.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the URL parsing and update summary section
replacement1 = """  // --- NEW: Parse URL parameters for vehicle ---
  const urlParams = new URLSearchParams(window.location.search);
  const selectedVehicleParam = urlParams.get('vehicle');
  
  let selectedCarData = null;
  if (selectedVehicleParam && typeof getFleetCarById !== 'undefined') {
    selectedCarData = getFleetCarById(selectedVehicleParam);
  }

  // Fallback to a default if not found
  if (!selectedCarData && typeof getFleetCarById !== 'undefined') {
    selectedCarData = getFleetCarById('std_1'); // Default to first standard car
  }

  // --- NEW: Update Summary UI ---
  function updateVehicleSummary() {
    const summaryImg = document.getElementById('summaryVehicleImg');
    const summaryName = document.getElementById('summaryVehicleName');
    const summaryPrice = document.getElementById('summaryVehiclePrice');
    if (!summaryImg || !selectedCarData) return;

    summaryImg.src = selectedCarData.img;
    summaryName.textContent = currentLang === 'ar' ? selectedCarData.nameAr : selectedCarData.nameEn;
    summaryPrice.textContent = currentLang === 'ar' ? 'يبدأ من $' + selectedCarData.price : 'From $' + selectedCarData.price;
  }
  
  updateVehicleSummary();
"""

content = re.sub(r'  // --- NEW: Parse URL parameters for vehicle ---.*?// 1\. Initialize Custom Searchable Dropdowns', replacement1 + '\n  // 1. Initialize Custom Searchable Dropdowns', content, flags=re.DOTALL)

# Replace the vehicle name extraction in the submit event
replacement2 = """    let vehicle = selectedCarData ? (currentLang === 'ar' ? selectedCarData.nameAr : selectedCarData.nameEn) : 'Taxi';"""
content = re.sub(r'    let vehicle = \'Taxi\';\n    document\.querySelectorAll\(\'input\[name="vehicle"\]\'\)\.forEach\(r => \{ if \(r\.checked\) vehicle = r\.parentElement\.textContent\.trim\(\); \}\);', replacement2, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
