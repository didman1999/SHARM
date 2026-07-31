// Transfer Booking Widget Logic

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('transferBookingForm');
  if (!form) return;

  const directionInputs = document.querySelectorAll('input[name="transfer_direction"]');
  const pickupContainer = document.getElementById('pickupContainer');
  const dropoffContainer = document.getElementById('dropoffContainer');
  const pickupInput = document.getElementById('pickupInput');
  const dropoffInput = document.getElementById('dropoffInput');
  
  const tripTypeInputs = document.querySelectorAll('input[name="trip_type"]');
  const returnDateContainer = document.getElementById('returnDateContainer');
  
  const currentLang = document.documentElement.lang === 'ar' ? 'ar' : 'en';

  // 1. Initialize Custom Searchable Dropdowns
  function setupSearchableDropdown(inputId, listId, isPickup) {
    const input = document.getElementById(inputId);
    const list = document.getElementById(listId);
    if (!input || !list) return;

    // Populate list
    sharmHotels.forEach(area => {
      const groupLabel = document.createElement('div');
      groupLabel.className = 'dropdown-group-label';
      groupLabel.textContent = currentLang === 'ar' ? area.areaAr : area.areaEn;
      list.appendChild(groupLabel);

      area.hotels.forEach(hotel => {
        const item = document.createElement('div');
        item.className = 'dropdown-item';
        item.textContent = currentLang === 'ar' ? hotel.ar : hotel.en;
        item.dataset.value = hotel.en;
        
        item.addEventListener('click', () => {
          input.value = item.textContent;
          input.dataset.selectedValue = hotel.en;
          list.classList.remove('active');
          validateLocations();
        });
        
        list.appendChild(item);
      });
    });

    // Toggle list on click
    input.addEventListener('focus', () => {
      list.classList.add('active');
      filterList(input, list);
    });

    // Hide list on blur (with delay to allow click)
    input.addEventListener('blur', () => {
      setTimeout(() => list.classList.remove('active'), 200);
    });

    // Filter on type
    input.addEventListener('input', () => {
      list.classList.add('active');
      filterList(input, list);
    });
  }

  function filterList(input, list) {
    const filter = input.value.toLowerCase();
    const items = list.querySelectorAll('.dropdown-item');
    const groups = list.querySelectorAll('.dropdown-group-label');
    
    // Hide all groups initially
    groups.forEach(g => g.style.display = 'none');
    
    let currentGroup = null;
    let hasVisibleInGroup = false;

    Array.from(list.children).forEach(child => {
      if (child.classList.contains('dropdown-group-label')) {
        // If previous group had visible items, make sure its label is visible
        if (currentGroup && hasVisibleInGroup) {
          currentGroup.style.display = 'block';
        }
        currentGroup = child;
        hasVisibleInGroup = false;
      } else if (child.classList.contains('dropdown-item')) {
        const text = child.textContent.toLowerCase();
        if (text.indexOf(filter) > -1) {
          child.style.display = 'block';
          hasVisibleInGroup = true;
        } else {
          child.style.display = 'none';
        }
      }
    });
    
    // Check last group
    if (currentGroup && hasVisibleInGroup) {
      currentGroup.style.display = 'block';
    }
  }

  setupSearchableDropdown('pickupInput', 'pickupList', true);
  setupSearchableDropdown('dropoffInput', 'dropoffList', false);

  // 2. Handle Direction Changes
  function updateDirectionFields() {
    let direction = 'hotel_to_hotel';
    directionInputs.forEach(rad => { if(rad.checked) direction = rad.value; });

    const airportName = currentLang === 'ar' ? "مطار شرم الشيخ الدولي" : "Sharm El Sheikh International Airport";
    
    pickupInput.disabled = false;
    dropoffInput.disabled = false;

    if (direction === 'airport_to_hotel') {
      pickupInput.value = airportName;
      pickupInput.dataset.selectedValue = "Sharm El Sheikh International Airport";
      pickupInput.disabled = true;
      if (dropoffInput.dataset.selectedValue === "Sharm El Sheikh International Airport") {
        dropoffInput.value = '';
      }
    } else if (direction === 'hotel_to_airport') {
      dropoffInput.value = airportName;
      dropoffInput.dataset.selectedValue = "Sharm El Sheikh International Airport";
      dropoffInput.disabled = true;
      if (pickupInput.dataset.selectedValue === "Sharm El Sheikh International Airport") {
        pickupInput.value = '';
      }
    } else {
      // Free selection
      if (pickupInput.disabled) pickupInput.value = '';
      if (dropoffInput.disabled) dropoffInput.value = '';
    }
  }

  directionInputs.forEach(rad => rad.addEventListener('change', updateDirectionFields));
  updateDirectionFields();

  // 3. Validation: Prevent same locations
  function validateLocations() {
    if (pickupInput.value && dropoffInput.value && pickupInput.value === dropoffInput.value) {
      dropoffInput.value = '';
      dropoffInput.dataset.selectedValue = '';
      alert(currentLang === 'ar' ? 'لا يمكن أن يكون موقع الاستلام والتوصيل متطابقين.' : 'Pickup and drop-off locations cannot be the same.');
    }
  }

  // 4. Round trip toggle
  tripTypeInputs.forEach(rad => {
    rad.addEventListener('change', () => {
      if (rad.value === 'round_trip') {
        returnDateContainer.style.display = 'block';
        document.getElementById('returnDate').required = true;
      } else {
        returnDateContainer.style.display = 'none';
        document.getElementById('returnDate').required = false;
      }
    });
  });

  // 5. Form Submission
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Simulate booking process
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="spinner"></span> Processing...';
    btn.disabled = true;

    setTimeout(() => {
      form.innerHTML = `
        <div class="booking-success">
          <svg width="64" height="64" fill="none" stroke="var(--success)" stroke-width="2" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          <h3>${currentLang === 'ar' ? 'تم تأكيد طلبك بنجاح!' : 'Booking Requested Successfully!'}</h3>
          <p>${currentLang === 'ar' ? 'الرقم المرجعي:' : 'Booking Reference:'} <strong>SHM-${Math.floor(Math.random() * 90000) + 10000}</strong></p>
          <p>${currentLang === 'ar' ? 'سيقوم فريقنا بتأكيد حجزك عبر الواتساب أو الإيميل خلال 10 دقائق.' : 'Our team will confirm your booking via WhatsApp or Email within 10 minutes.'}</p>
        </div>
      `;
    }, 1500);
  });
});
