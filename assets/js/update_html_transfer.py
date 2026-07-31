import re
import os

html_path = r'C:\Sharm\Sharm\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_hero_content = """
    <div class="container hero-container-redesign">
      <div class="hero-content" style="text-align: center; max-width: 900px; margin: 0 auto;">
        <div class="hero-badge" style="justify-content: center;">
          <span class="dot"></span>
          <span data-lang-en="✈️ 24/7 Airport Transfers" data-lang-ar="✈️ توصيلات المطار على مدار 24 ساعة">24/7 Airport Transfers</span>
        </div>

        <h1 data-lang-en="Book Your Sharm El Sheikh <span>Transfer</span>" data-lang-ar="احجز <span>توصيلتك</span> في شرم الشيخ">Book Your Sharm El Sheikh <span>Transfer</span></h1>

        <p data-lang-en="Taxi & Limousine transfers from Sharm El Sheikh Airport to your hotel. Fast, safe, and reliable." data-lang-ar="توصيلات التاكسي والليموزين من مطار شرم الشيخ إلى فندقك. أمان وسرعة وموثوقية.">Taxi & Limousine transfers from Sharm El Sheikh Airport to your hotel. Fast, safe, and reliable.</p>

        <!-- TRANSFER WIDGET -->
        <div class="transfer-widget-container">
          <form id="transferBookingForm" class="transfer-widget">
            
            <!-- Vehicle Type -->
            <div class="widget-row transfer-type-selector">
              <label class="radio-card">
                <input type="radio" name="vehicle" value="taxi" checked>
                <div class="card-content">
                  <span class="emoji">🚕</span>
                  <span data-lang-en="Taxi" data-lang-ar="تاكسي">Taxi</span>
                </div>
              </label>
              <label class="radio-card">
                <input type="radio" name="vehicle" value="limousine">
                <div class="card-content">
                  <span class="emoji">🚘</span>
                  <span data-lang-en="Limousine" data-lang-ar="ليموزين">Limousine</span>
                </div>
              </label>
              <label class="radio-card">
                <input type="radio" name="vehicle" value="private">
                <div class="card-content">
                  <span class="emoji">🚐</span>
                  <span data-lang-en="Private Van" data-lang-ar="فان خاص">Private Van</span>
                </div>
              </label>
            </div>

            <!-- Direction -->
            <div class="widget-row direction-selector">
              <label><input type="radio" name="transfer_direction" value="airport_to_hotel" checked> <span data-lang-en="Airport to Hotel" data-lang-ar="من المطار للفندق">Airport to Hotel</span></label>
              <label><input type="radio" name="transfer_direction" value="hotel_to_airport"> <span data-lang-en="Hotel to Airport" data-lang-ar="من الفندق للمطار">Hotel to Airport</span></label>
              <label><input type="radio" name="transfer_direction" value="hotel_to_hotel"> <span data-lang-en="Hotel to Hotel / Other" data-lang-ar="من فندق لفندق / أخرى">Hotel to Hotel / Other</span></label>
            </div>

            <!-- Locations -->
            <div class="widget-row locations-grid">
              <div class="input-group">
                <label data-lang-en="Pickup Location" data-lang-ar="مكان الاستلام">Pickup Location</label>
                <div class="custom-dropdown">
                  <input type="text" id="pickupInput" placeholder="Search area or hotel..." autocomplete="off" required disabled value="Sharm El Sheikh International Airport">
                  <div class="dropdown-list" id="pickupList"></div>
                </div>
              </div>
              <div class="input-group">
                <label data-lang-en="Drop-off Location" data-lang-ar="مكان التوصيل">Drop-off Location</label>
                <div class="custom-dropdown">
                  <input type="text" id="dropoffInput" placeholder="Search area or hotel..." autocomplete="off" required>
                  <div class="dropdown-list" id="dropoffList"></div>
                </div>
              </div>
            </div>

            <!-- Details -->
            <div class="widget-row details-grid">
              <div class="input-group">
                <label data-lang-en="Pickup Date" data-lang-ar="تاريخ الاستلام">Pickup Date</label>
                <input type="date" required>
              </div>
              <div class="input-group">
                <label data-lang-en="Pickup Time" data-lang-ar="وقت الاستلام">Pickup Time</label>
                <input type="time" required>
              </div>
              <div class="input-group">
                <label data-lang-en="Passengers" data-lang-ar="عدد الركاب">Passengers</label>
                <input type="number" min="1" value="2" required>
              </div>
              <div class="input-group">
                <label data-lang-en="Luggage" data-lang-ar="الحقائب">Luggage</label>
                <input type="number" min="0" value="2">
              </div>
              <div class="input-group">
                <label data-lang-en="Flight No. (Optional)" data-lang-ar="رقم الرحلة (اختياري)">Flight No. (Optional)</label>
                <input type="text" placeholder="e.g. MS771">
              </div>
            </div>

            <!-- Trip Type -->
            <div class="widget-row trip-type-selector">
              <label><input type="radio" name="trip_type" value="one_way" checked> <span data-lang-en="One-way" data-lang-ar="اتجاه واحد">One-way</span></label>
              <label><input type="radio" name="trip_type" value="round_trip"> <span data-lang-en="Round-trip" data-lang-ar="ذهاب وعودة">Round-trip</span></label>
            </div>
            
            <div id="returnDateContainer" style="display:none;" class="widget-row details-grid return-grid">
              <div class="input-group">
                <label data-lang-en="Return Date" data-lang-ar="تاريخ العودة">Return Date</label>
                <input type="date" id="returnDate">
              </div>
              <div class="input-group">
                <label data-lang-en="Return Time" data-lang-ar="وقت العودة">Return Time</label>
                <input type="time" id="returnTime">
              </div>
            </div>

            <button type="submit" class="btn btn-accent btn-lg transfer-submit-btn" style="width: 100%; justify-content: center; margin-top: 15px;">
              <span data-lang-en="Book Transfer" data-lang-ar="احجز التوصيلة">Book Transfer</span>
            </button>
            
            <div class="widget-footer">
              <span>✅ <span data-lang-en="Confirmation within 10 min" data-lang-ar="تأكيد خلال 10 دقائق">Confirmation within 10 min</span></span>
              <span>✅ <span data-lang-en="24/7 Service" data-lang-ar="خدمة 24/7">24/7 Service</span></span>
              <span>✅ <span data-lang-en="Pay on Arrival" data-lang-ar="الدفع عند الوصول">Pay on Arrival</span></span>
            </div>
          </form>
        </div>
      </div>
    </div>
"""

# Replace hero content and remove hero-search and hero-stats
# The hero container starts at <div class="container"> inside <section class="hero" id="hero">
# and goes until the end of the section. Then we have <div class="hero-search">.
# We will use regex to replace everything from <div class="container"> in hero until the end of hero-search.

hero_match = re.search(r'<div class="container">(?=\s*<div class="hero-content">).*?</section>', content, flags=re.DOTALL)
if hero_match:
    hero_end_index = hero_match.end()
    # Find hero-search and remove it completely
    content = re.sub(r'<!-- ============================================================\s*SEARCH FORM\s*============================================================ -->.*?<div class="hero-search">.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Replace the container inside hero
    content = re.sub(r'<div class="container">(?=\s*<div class="hero-content">).*?(?=\s*<div class="hero-dots">)', new_hero_content, content, flags=re.DOTALL)

# Inject JS scripts at the bottom
if '<script src="assets/js/hotels.js"></script>' not in content:
    content = content.replace('<script src="assets/js/main.js"></script>', 
                              '<script src="assets/js/hotels.js"></script>\n  <script src="assets/js/main.js"></script>\n  <script src="assets/js/transfer.js"></script>')

# Update navbar 'Book Now' link to point to #hero instead of trips.html
content = content.replace('<a href="trips.html" class="navbar-cta">', '<a href="#hero" class="navbar-cta">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with Transfer Widget!")
