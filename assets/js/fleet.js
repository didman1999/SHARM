const fleetDatabase = {
  categories: [
    {
      id: "standard",
      titleEn: "Standard Class",
      titleAr: "الدرجة الاقتصادية",
      descriptionEn: "Comfortable and reliable vehicles for everyday travel.",
      descriptionAr: "سيارات مريحة وموثوقة للتنقلات اليومية.",
      cars: [
        {
          id: "std_1",
          nameEn: "Hyundai Elantra",
          nameAr: "هيونداي النترا",
          price: 15,
          pax: 3,
          bags: 2,
          featuresEn: "AC • Free WiFi",
          featuresAr: "تكييف • إنترنت مجاني",
          img: "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "std_2",
          nameEn: "Toyota Corolla",
          nameAr: "تويوتا كورولا",
          price: 15,
          pax: 3,
          bags: 2,
          featuresEn: "AC • Free WiFi",
          featuresAr: "تكييف • إنترنت مجاني",
          img: "https://images.unsplash.com/photo-1550355291-bbee04a92027?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "std_3",
          nameEn: "Kia Cerato",
          nameAr: "كيا سيراتو",
          price: 15,
          pax: 3,
          bags: 2,
          featuresEn: "AC • Free WiFi",
          featuresAr: "تكييف • إنترنت مجاني",
          img: "https://images.unsplash.com/photo-1563720360172-67b8f3dce741?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "std_4",
          nameEn: "Standard Minivan",
          nameAr: "ميني فان اقتصادي",
          price: 25,
          pax: 7,
          bags: 5,
          featuresEn: "AC • Family Friendly",
          featuresAr: "تكييف • مناسب للعائلات",
          img: "https://images.unsplash.com/photo-1590634639912-88f5799971db?auto=format&fit=crop&q=80&w=600"
        }
      ]
    },
    {
      id: "business",
      titleEn: "Business Class",
      titleAr: "درجة رجال الأعمال",
      descriptionEn: "Premium vehicles with extra legroom and luxury features.",
      descriptionAr: "سيارات مميزة بمساحات أوسع ورفاهية أعلى.",
      cars: [
        {
          id: "bus_1",
          nameEn: "Mercedes E-Class",
          nameAr: "مرسيدس E-Class",
          price: 40,
          pax: 3,
          bags: 3,
          featuresEn: "AC • WiFi • Water",
          featuresAr: "تكييف • إنترنت • مياه مجانية",
          img: "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "bus_2",
          nameEn: "BMW 5 Series",
          nameAr: "بي إم دبليو الفئة الخامسة",
          price: 40,
          pax: 3,
          bags: 2,
          featuresEn: "AC • WiFi • Leather",
          featuresAr: "تكييف • إنترنت • مقاعد جلد",
          img: "https://images.unsplash.com/photo-1555353540-64580b51c258?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "bus_3",
          nameEn: "Luxury SUV (Prado)",
          nameAr: "لاند كروزر برادو",
          price: 50,
          pax: 5,
          bags: 4,
          featuresEn: "AC • 4WD • Spacious",
          featuresAr: "تكييف • دفع رباعي • مساحة واسعة",
          img: "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "bus_4",
          nameEn: "Business Minibus",
          nameAr: "ميني باص سياحي مميز",
          price: 60,
          pax: 12,
          bags: 10,
          featuresEn: "AC • Reclining Seats",
          featuresAr: "تكييف • مقاعد مريحة",
          img: "https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&q=80&w=600"
        }
      ]
    },
    {
      id: "vip",
      titleEn: "VIP Class",
      titleAr: "درجة الـ VIP",
      descriptionEn: "The ultimate luxury experience. Professional chauffeurs and high-end amenities.",
      descriptionAr: "أقصى درجات الفخامة. سائقون محترفون وخدمات راقية.",
      cars: [
        {
          id: "vip_1",
          nameEn: "VIP Limousine",
          nameAr: "VIP ليموزين",
          price: 80,
          pax: 4,
          bags: 3,
          featuresEn: "AC • WiFi • Mini-bar",
          featuresAr: "تكييف • إنترنت • ضيافة",
          img: "https://images.unsplash.com/photo-1503376760-36fd41d11640?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "vip_2",
          nameEn: "Mercedes S-Class",
          nameAr: "مرسيدس S-Class",
          price: 100,
          pax: 3,
          bags: 2,
          featuresEn: "Ultimate Luxury",
          featuresAr: "رفاهية مطلقة",
          img: "https://images.unsplash.com/photo-1620882744747-0e6d61a33719?auto=format&fit=crop&q=80&w=600"
        },
        {
          id: "vip_3",
          nameEn: "Mercedes V-Class VIP",
          nameAr: "مرسيدس V-Class فاخرة",
          price: 120,
          pax: 6,
          bags: 6,
          featuresEn: "Luxury Van • Massage Seats",
          featuresAr: "فان فاخر • كراسي مساج",
          img: "https://images.unsplash.com/photo-1610444349386-db30800c4368?auto=format&fit=crop&q=80&w=600"
        }
      ]
    }
  ]
};

// Helper function to find a car by ID
function getFleetCarById(carId) {
  for (const category of fleetDatabase.categories) {
    for (const car of category.cars) {
      if (car.id === carId) return car;
    }
  }
  return null;
}
