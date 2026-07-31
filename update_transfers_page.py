import re

filepath = r'C:\Sharm\Sharm\transfers.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the transfer form section entirely
content = re.sub(r'<!-- Transfer Booking Form -->.*?<!-- Vehicle Selection -->', '<!-- Vehicle Selection -->', content, flags=re.DOTALL)

# Update the vehicle cards
# Sedan -> Taxi
sedan_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- Sedan -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- Sedan -->\n        <div class="vehicle-card">\n          {sedan_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>Sedan</h3>', '<h3 data-lang-en="Taxi / Sedan" data-lang-ar="تاكسي / سيدان">Taxi / Sedan</h3>')
content = re.sub(r'<div class="vehicle-price">\$15.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=taxi" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# SUV (Maybe we don't have SUV in the widget yet, but let's keep it and map to "limousine" or "suv" later, or just map it to taxi for now or create new vehicle types)
suv_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- SUV -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- SUV -->\n        <div class="vehicle-card">\n          {suv_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>SUV</h3>', '<h3 data-lang-en="SUV" data-lang-ar="سيارة دفع رباعي">SUV</h3>')
content = re.sub(r'<div class="vehicle-price">\$25.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=suv" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# Minivan -> Private Van
minivan_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1590634639912-88f5799971db?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- Minivan -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- Minivan -->\n        <div class="vehicle-card">\n          {minivan_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>Minivan</h3>', '<h3 data-lang-en="Minivan" data-lang-ar="ميني فان">Minivan</h3>')
content = re.sub(r'<div class="vehicle-price">\$35.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=private" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# Large Van -> Minibus
van_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- Large Van -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- Large Van -->\n        <div class="vehicle-card">\n          {van_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>Large Van</h3>', '<h3 data-lang-en="Minibus" data-lang-ar="ميني باص">Minibus</h3>')
content = re.sub(r'<div class="vehicle-price">\$50.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=minibus" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# Bus
bus_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- Bus -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- Bus -->\n        <div class="vehicle-card">\n          {bus_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>Bus</h3>', '<h3 data-lang-en="Coach Bus" data-lang-ar="أتوبيس سياحي">Coach Bus</h3>')
content = re.sub(r'<div class="vehicle-price">\$80.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=bus" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# Luxury -> Limousine
lux_img = '<div class="vehicle-card-image" style="background: url(\'https://images.unsplash.com/photo-1503376760-36fd41d11640?auto=format&fit=crop&q=80&w=600\') center/cover; height: 180px;"></div>'
content = re.sub(r'<!-- Luxury -->.*?<div class="vehicle-card-image".*?</div>\s*</div>', f'<!-- Luxury -->\n        <div class="vehicle-card">\n          {lux_img}', content, flags=re.DOTALL, count=1)
content = content.replace('<h3>Luxury Vehicle</h3>', '<h3 data-lang-en="Luxury Limousine" data-lang-ar="ليموزين فاخر">Luxury Limousine</h3>')
content = re.sub(r'<div class="vehicle-price">\$60.*?</div>', '<div style="margin-top: 15px;"><a href="book-transfer.html?vehicle=limousine" class="btn btn-primary" style="width:100%; justify-content:center;" data-lang-en="Select Vehicle" data-lang-ar="اختر السيارة">Select Vehicle</a></div>', content, count=1)

# Remove the CTA below the grid since they now click directly on the cards
content = re.sub(r'<!-- CTA -->.*?</div>\s*</section>', '</section>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
