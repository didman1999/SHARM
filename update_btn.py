import re

html_path = r'C:\Sharm\Sharm\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous image button with the simple animated button
new_button = """
        <div style="margin: 40px 0 35px; text-align: center; position: relative;">
          <style>
            .animated-car-btn {
              position: relative;
              overflow: hidden;
              display: inline-flex;
              align-items: center;
              justify-content: center;
              padding: 18px 50px;
              font-size: 1.4rem;
              font-weight: 800;
              border-radius: 50px;
              background: linear-gradient(45deg, var(--accent), #ff9800);
              color: white;
              text-decoration: none;
              box-shadow: 0 10px 25px rgba(251, 140, 0, 0.4);
              transition: transform 0.3s ease, box-shadow 0.3s ease;
              border: 3px solid transparent;
            }
            .animated-car-btn:hover {
              transform: translateY(-5px);
              box-shadow: 0 15px 35px rgba(251, 140, 0, 0.6);
              border: 3px solid rgba(255,255,255,0.5);
            }
            .car-track {
              position: absolute;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
              pointer-events: none;
              z-index: 1;
            }
            .running-car {
              position: absolute;
              top: 50%;
              transform: translateY(-50%);
              font-size: 2.2rem;
              left: -60px;
              animation: driveAcross 2.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
              opacity: 0.3; /* Transparent so it runs smoothly behind text */
            }
            .animated-car-btn .btn-text {
              position: relative;
              z-index: 2;
              text-transform: uppercase;
              letter-spacing: 1px;
              text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
            }
            @keyframes driveAcross {
              0% { left: -60px; }
              100% { left: 110%; }
            }
          </style>
          
          <a href="book-transfer.html" class="animated-car-btn">
            <span class="car-track">
              <span class="running-car">🏎️</span>
            </span>
            <span class="btn-text">
              <span data-lang-en="Book Fast Transfer" data-lang-ar="احجز سيارة سريعة">Book Fast Transfer</span>
            </span>
          </a>
        </div>
"""

# The regex should match the previously inserted large car div
content = re.sub(r'<div style="margin: 40px 0 35px; text-align: center; position: relative;">.*?</a>\s*</div>', new_button, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated button to a simple one with running car animation.")
