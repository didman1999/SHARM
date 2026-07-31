import os
import shutil
import re

html_path = r'C:\Sharm\Sharm\index.html'
new_html_path = r'C:\Sharm\Sharm\book-transfer.html'
img_src = r'C:\Users\Merank\.gemini\antigravity-ide\brain\fe0b528f-d263-4009-8b7f-42db4ccce8e0\luxury_transfer_car_1785518454972.png'
img_dst = r'C:\Sharm\Sharm\assets\images\hero\luxury_car.png'

# Move image
if os.path.exists(img_src):
    shutil.copy(img_src, img_dst)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Create book-transfer.html
# We want to keep the header, footer, and the hero section but without the huge car button.
# And we keep the transfer widget.
# Let's just copy the content, but we will remove the hero slider images to make it a solid background.
bt_content = content
bt_content = re.sub(r'<div class="hero-slider">.*?</div>\s*<div class="hero-overlay"></div>', '<div class="hero-overlay" style="background: linear-gradient(135deg, var(--navy) 0%, #1a237e 100%); opacity: 1;"></div>', bt_content, flags=re.DOTALL)

# Remove the fast car button if it exists in book-transfer
bt_content = re.sub(r'<div style="margin: 25px 0 35px; text-align: center;">.*?</a>\s*</div>', '', bt_content, flags=re.DOTALL)

with open(new_html_path, 'w', encoding='utf-8') as f:
    f.write(bt_content)


# 2. Update index.html
# Remove the transfer widget entirely
content = re.sub(r'<!-- TRANSFER WIDGET -->\s*<div class="transfer-widget-container" id="transferWidgetSection">.*?</form>\s*</div>', '', content, flags=re.DOTALL)

# Replace the old button with a new animated image button
new_button = """
        <div style="margin: 40px 0 35px; text-align: center; position: relative;">
          <style>
            @keyframes driveInAndPulse {
              0% { transform: translateX(-100vw) scale(0.8); opacity: 0; }
              60% { transform: translateX(20px) scale(1.1); opacity: 1; }
              80% { transform: translateX(-10px) scale(0.95); }
              100% { transform: translateX(0) scale(1); }
            }
            @keyframes hoverFloat {
              0%, 100% { transform: translateY(0) scale(1); filter: drop-shadow(0 20px 30px rgba(0,0,0,0.5)); }
              50% { transform: translateY(-10px) scale(1.02); filter: drop-shadow(0 30px 40px rgba(0,0,0,0.6)); }
            }
            .luxury-car-btn {
              display: inline-block;
              animation: driveInAndPulse 1.5s cubic-bezier(0.25, 1, 0.5, 1) forwards, hoverFloat 4s ease-in-out 1.5s infinite;
              transition: all 0.3s ease;
              position: relative;
              cursor: pointer;
              text-decoration: none;
            }
            .luxury-car-btn:hover {
              transform: scale(1.05) !important;
              filter: drop-shadow(0 0 30px rgba(255,152,0,0.8));
            }
            .luxury-car-img {
              width: 100%;
              max-width: 450px;
              border-radius: 20px;
              border: 3px solid rgba(255, 255, 255, 0.2);
              box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            }
            .car-btn-label {
              position: absolute;
              bottom: -20px;
              left: 50%;
              transform: translateX(-50%);
              background: var(--accent);
              color: #fff;
              padding: 10px 30px;
              border-radius: 30px;
              font-weight: 900;
              font-size: 1.2rem;
              white-space: nowrap;
              box-shadow: 0 10px 20px rgba(251,140,0,0.5);
              border: 2px solid #fff;
            }
          </style>
          <a href="book-transfer.html" class="luxury-car-btn">
            <img src="assets/images/hero/luxury_car.png" alt="Luxury Transfer" class="luxury-car-img">
            <div class="car-btn-label" data-lang-en="Book Transfer Now" data-lang-ar="احجز سيارتك الآن">Book Transfer Now</div>
          </a>
        </div>
"""

content = re.sub(r'<div style="margin: 25px 0 35px; text-align: center;">.*?</a>\s*</div>', new_button, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Split transfer widget to book-transfer.html and added animated luxury car button to index.html successfully.")
