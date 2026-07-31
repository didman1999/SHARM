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

  const pickupNow = document.getElementById('pickupNow');
  const pickupDate = document.getElementById('pickupDate');
  const pickupTime = document.getElementById('pickupTime');

  const currentLang = document.documentElement.lang === 'ar' ? 'ar' : 'en';

  // --- NEW: Parse URL parameters for vehicle ---
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
    directionInputs.forEach(rad => { if (rad.checked) direction = rad.value; });

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

  // Now Checkbox logic
  if (pickupNow) {
    pickupNow.addEventListener('change', () => {
      if (pickupNow.checked) {
        pickupDate.disabled = true;
        pickupDate.required = false;
        pickupDate.value = '';
        pickupTime.disabled = true;
        pickupTime.required = false;
        pickupTime.value = '';
      } else {
        pickupDate.disabled = false;
        pickupDate.required = true;
        pickupTime.disabled = false;
        pickupTime.required = true;
      }
    });
  }

  // 5. Form Submission (Send to WhatsApp)
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let vehicle = selectedCarData ? (currentLang === 'ar' ? selectedCarData.nameAr : selectedCarData.nameEn) : 'Taxi';

    let tripType = 'One-way';
    document.querySelectorAll('input[name="trip_type"]').forEach(r => { if (r.checked) tripType = r.parentElement.textContent.trim(); });

    const pickup = pickupInput.value;
    const dropoff = dropoffInput.value;
    const pass = document.getElementById('passengers').value;
    const lugg = document.getElementById('luggage').value;
    const flight = document.getElementById('flightNo').value || (currentLang === 'ar' ? 'غير محدد' : 'N/A');

    let dateTimeStr = '';
    let arDateTimeStr = '';
    if (pickupNow && pickupNow.checked) {
      dateTimeStr = 'NOW (ASAP)';
      arDateTimeStr = 'حالا (في أسرع وقت)';
    } else {
      dateTimeStr = `${pickupDate.value} at ${pickupTime.value}`;
      arDateTimeStr = `${pickupDate.value} الساعة ${pickupTime.value}`;
    }

    let returnStr = '';
    let arReturnStr = '';
    let tripTypeVal = 'one_way';
    document.querySelectorAll('input[name="trip_type"]').forEach(r => { if (r.checked) tripTypeVal = r.value; });
    if (tripTypeVal === 'round_trip') {
      const rDate = document.getElementById('returnDate').value;
      const rTime = document.getElementById('returnTime').value || (currentLang === 'ar' ? 'أي وقت' : 'Any');
      returnStr = `\n🔄 Return: ${rDate} at ${rTime}`;
      arReturnStr = `\n🔄 العودة: ${rDate} الساعة ${rTime}`;
    }

    let message = '';
    if (currentLang === 'ar') {
      message = `*طلب حجز توصيلة جديد* 🚖
🚗 السيارة: ${vehicle}
🔄 نوع الرحلة: ${tripType}
📍 من: ${pickup}
📍 إلى: ${dropoff}
📅 التاريخ والوقت: ${arDateTimeStr}${arReturnStr}
👥 الركاب: ${pass}
🧳 الحقائب: ${lugg}
✈️ رقم الرحلة: ${flight}`;
    } else {
      message = `*New Transfer Booking* 🚖
🚗 Vehicle: ${vehicle}
🔄 Type: ${tripType}
📍 From: ${pickup}
📍 To: ${dropoff}
📅 Date & Time: ${dateTimeStr}${returnStr}
👥 Passengers: ${pass}
🧳 Luggage: ${lugg}
✈️ Flight No: ${flight}`;
    }

    const encodedMsg = encodeURIComponent(message);
    const whatsappUrl = `https://wa.me/201515682365?text=${encodedMsg}`;

    // Redirect to WhatsApp
    window.open(whatsappUrl, '_blank');

    // Optionally change button text to indicate success
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    btn.innerHTML = currentLang === 'ar' ? 'تم تحويلك للواتساب ✅' : 'Redirected to WhatsApp ✅';
    setTimeout(() => { btn.innerHTML = originalText; }, 5000);
  });
});
