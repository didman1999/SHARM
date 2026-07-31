// Comprehensive Hotel Data for Transfer Booking
const sharmHotels = [
  {
    areaEn: "Airport",
    basePrice: 10,
    areaAr: "المطار",
    hotels: [
      { en: "Sharm El Sheikh International Airport", ar: "مطار شرم الشيخ الدولي" }
    ]
  },
  {
    areaEn: "Naama Bay",
    basePrice: 15,
    areaAr: "خليج نعمة",
    hotels: [
      { en: "Movenpick Resort Sharm El Sheikh", ar: "منتجع موفنبيك شرم الشيخ" },
      { en: "Novotel Sharm El-Sheikh", ar: "نوفوتيل شرم الشيخ" },
      { en: "Maritim Jolie Ville Resort & Casino", ar: "منتجع وكازينو ماريتيم جولي فيل" },
      { en: "Tropitel Naama Bay Hotel", ar: "فندق تروبيتل نعمة باي" },
      { en: "Stella Di Mare Beach Hotel & Spa", ar: "فندق وسبا ستيلا دي ماري بيتش" },
      { en: "Gafy Resort Aqua Park", ar: "منتجع غافي أكوا بارك" },
      { en: "Marina Sharm Hotel", ar: "فندق مارينا شرم" },
      { en: "Naama Bay Hotel & Resort", ar: "فندق ومنتجع نعمة باي" },
      { en: "Lido Sharm Hotel", ar: "فندق ليدو شرم" },
      { en: "Ghazala Beach Hotel", ar: "فندق غزالة بيتش" },
      { en: "Ghazala Gardens Hotel", ar: "فندق غزالة جاردنز" },
      { en: "Cataract Layalina Resort", ar: "منتجع كتاركت ليالينا" },
      { en: "Fayrouz Resort", ar: "منتجع فيروز" },
      { en: "Camel Dive Club & Hotel", ar: "فندق وكاميل دايف كلوب" },
      { en: "Sharm Dreams Resort", ar: "منتجع شرم دريمز" },
      { en: "Xperience Kiroseiz Premier", ar: "اكسبرينس كيروسيز بريمير" },
      { en: "Solymar Naama Bay", ar: "سوليمار نعمة باي" },
      { en: "Fantazia Hotel", ar: "فندق فانتازيا" },
      { en: "Oonas Dive Club", ar: "اوناس دايف كلوب" },
      { en: "Eden Rock Hotel", ar: "فندق ايدن روك" },
      { en: "Falcon Naama Star Hotel", ar: "فندق فالكون نعمة ستار" }
    ]
  },
  {
    areaEn: "SOHO Square / Sharks Bay",
    basePrice: 20,
    areaAr: "ميدان سوهو / خليج القرش",
    hotels: [
      { en: "Savoy Sharm El Sheikh", ar: "سافوي شرم الشيخ" },
      { en: "Four Seasons Resort Sharm El Sheikh", ar: "منتجع فور سيزونز شرم الشيخ" },
      { en: "Concorde El Salam Hotel", ar: "فندق كونكورد السلام" },
      { en: "Sierra Sharm El Sheikh", ar: "سيرا شرم الشيخ" },
      { en: "Sunrise Arabian Beach Resort", ar: "منتجع صن رايز أرابيان بيتش" },
      { en: "Grand Oasis Resort", ar: "منتجع جراند أواسيز" },
      { en: "Sultan Gardens Resort", ar: "منتجع سلطان جاردنز" },
      { en: "Xperience Sea Breeze Resort", ar: "منتجع اكسبرينس سي بريز" },
      { en: "Coral Beach Resort Tiran", ar: "منتجع كورال بيتش تيران" },
      { en: "Sharks Bay Umbi Diving Village", ar: "قرية أسماك القرش أمبي للغوص" },
      { en: "Royal Savoy Sharm El Sheikh", ar: "رويال سافوي شرم الشيخ" },
      { en: "DoubleTree by Hilton Sharks Bay", ar: "دبل تري من هيلتون خليج القرش" },
      { en: "Domina Coral Bay", ar: "دومينا كورال باي" },
      { en: "Pyramisa Beach Resort", ar: "منتجع بيراميزا بيتش" }
    ]
  },
  {
    areaEn: "Nabq Bay",
    basePrice: 25,
    areaAr: "خليج نبق",
    hotels: [
      { en: "Rixos Premium Seagate", ar: "ريكسوس بريميوم سيجيت" },
      { en: "Rixos Sharm El Sheikh", ar: "ريكسوس شرم الشيخ" },
      { en: "Rixos Radamis Sharm El Sheikh", ar: "ريكسوس راداميس شرم الشيخ" },
      { en: "Steigenberger Alcazar", ar: "شتيجنبرجر ألكازار" },
      { en: "Cleopatra Luxury Resort", ar: "منتجع كليوباترا الفاخر" },
      { en: "Charmillion Club Aqua Park", ar: "تشارميليون كلوب أكوا بارك" },
      { en: "Charmillion Sea Life Resort", ar: "منتجع تشارميليون سي لايف" },
      { en: "Charmillion Gardens Aqua Park", ar: "تشارميليون جاردنز أكوا بارك" },
      { en: "Barcelo Tiran Sharm", ar: "بارسيلو تيران شرم" },
      { en: "Jaz Mirabel Beach", ar: "جاز ميرابل بيتش" },
      { en: "Jaz Mirabel Resort", ar: "منتجع جاز ميرابل" },
      { en: "Coral Sea Holiday Resort", ar: "منتجع كورال سي هوليداي" },
      { en: "Coral Sea Waterworld", ar: "كورال سي ووتر وورلد" },
      { en: "Rehana Royal Beach Resort", ar: "منتجع ريحانة رويال بيتش" },
      { en: "Rehana Sharm Resort", ar: "منتجع ريحانة شرم" },
      { en: "Amwaj Oyoun Resort & Casino", ar: "منتجع وكازينو أمواج عيون" },
      { en: "Parrotel Aqua Park Resort", ar: "منتجع باروتيل أكوا بارك" },
      { en: "Parrotel Beach Resort", ar: "منتجع باروتيل بيتش" },
      { en: "Aurora Oriental Resort", ar: "منتجع أورورا أورينتال" },
      { en: "Sea Beach Aqua Park Resort", ar: "منتجع سي بيتش أكوا بارك" },
      { en: "Magic World Sharm", ar: "ماجيك وورلد شرم" },
      { en: "Nubian Village", ar: "قرية النوبة" },
      { en: "Nubian Island", ar: "جزيرة النوبة" }
    ]
  },
  {
    areaEn: "Hadaba & Ras Um Sid",
    basePrice: 20,
    areaAr: "الهضبة ورأس أم سيد",
    hotels: [
      { en: "Renaissance Sharm El Sheikh Golden View", ar: "رينيسانس شرم الشيخ جولدن فيو" },
      { en: "Sunrise Montemare Resort", ar: "منتجع صن رايز مونتيماري" },
      { en: "Sunrise Diamond Beach Resort", ar: "منتجع صن رايز دايموند بيتش" },
      { en: "Albatros Aqua Park", ar: "الباتروس أكوا بارك" },
      { en: "Albatros Aqua Blu", ar: "الباتروس أكوا بلو" },
      { en: "Jaz Fanara Resort", ar: "منتجع جاز فنارة" },
      { en: "Reef Oasis Beach Resort", ar: "منتجع ريف أواسيس بيتش" },
      { en: "Sentido Reef Oasis Senses", ar: "سينتيدو ريف أواسيس سينسيس" },
      { en: "Safir Sharm Waterfalls Resort", ar: "منتجع سفير شرم ووترفولز" },
      { en: "Monte Carlo Sharm Resort & Spa", ar: "منتجع وسبا مونت كارلو شرم" },
      { en: "Royal Monte Carlo", ar: "رويال مونت كارلو" },
      { en: "Il Mercato Hotel & Spa", ar: "فندق وسبا إل ميركاتو" },
      { en: "Amphoras Beach", ar: "أمفوراس بيتش" },
      { en: "Amphoras Blu", ar: "أمفوراس بلو" },
      { en: "Amphoras Aqua", ar: "أمفوراس أكوا" },
      { en: "Queen Sharm Resort", ar: "منتجع كوين شرم" },
      { en: "Faraana Reef Resort", ar: "منتجع الفراعنة ريف" },
      { en: "Dive Inn Resort", ar: "منتجع دايف إن" },
      { en: "Sharm Resort", ar: "منتجع شرم" },
      { en: "Sharm Plaza", ar: "شرم بلازا" }
    ]
  },
  {
    areaEn: "Montazah & Ras Nasrani",
    basePrice: 22,
    areaAr: "المنتزه ورأس نصراني",
    hotels: [
      { en: "Baron Resort Sharm El Sheikh", ar: "منتجع بارون شرم الشيخ" },
      { en: "Baron Palms Resort (Adults Only)", ar: "منتجع بارون بالمز (للبالغين فقط)" },
      { en: "Coral Sea Sensatori", ar: "كورال سي سينساتوري" },
      { en: "Jaz Belvedere", ar: "جاز بيلفيدير" },
      { en: "Pickalbatros Palace Sharm", ar: "بيكالباتروس بالاس شرم" },
      { en: "Albatros Laguna Vista", ar: "الباتروس لاجونا فيستا" },
      { en: "Cyrene Grand Hotel", ar: "فندق سايرين جراند" },
      { en: "Melia Sharm Resort", ar: "منتجع ميليا شرم" },
      { en: "Ivy Cyrene Island Hotel", ar: "فندق آيفي سايرين آيلاند" }
    ]
  },
  {
    areaEn: "Old Market & Sharm El Maya",
    basePrice: 20,
    areaAr: "السوق القديم وشرم المايا",
    hotels: [
      { en: "Iberotel Palace", ar: "إيبروتل بالاس" },
      { en: "Albatros Sharm Resort", ar: "منتجع الباتروس شرم" },
      { en: "Seti Sharm Resort", ar: "منتجع سيتي شرم" },
      { en: "Turquoise Beach Hotel", ar: "فندق تركواز بيتش" },
      { en: "Aida Hotel", ar: "فندق عايدة" }
    ]
  },
  {
    areaEn: "Other Destinations",
    basePrice: 30,
    areaAr: "وجهات أخرى",
    hotels: [
      { en: "Other Hotel (Not listed)", ar: "فندق آخر (غير مدرج)" },
      { en: "Custom Destination / Private Villa", ar: "وجهة مخصصة / فيلا خاصة" }
    ]
  }
];
