import random

def guess_the_number():
    # Random son tanlash
    son = random.randint(1, 100)
    
    # Harakatlar soni
    harakatlar = 0
    
    while True:
        # Foydalanuvchi tomonidan son kiritish
        user_input = input("Qaysi sonni taxmin qilasiz? (1-100): ")
        
        # Foydalanuvchi tomonidan son kiritilmaganligi uchun tekshirish
        if not user_input.isdigit():
            print("Iltimos, son kiritishingiz kerak.")
            continue
        
        # Foydalanuvchi tomonidan son kiritilganligi uchun tekshirish
        user_input = int(user_input)
        
        # Foydalanuvchi tomonidan son kiritilganligi uchun tekshirish
        if user_input < 1 or user_input > 100:
            print("Iltimos, 1 dan 100 gacha son kiritishingiz kerak.")
            continue
        
        # Harakatlar soni oshish
        harakatlar += 1
        
        # Taxmin qilingan sonni tekshirish
        if user_input < son:
            print("Taxmin qilingan son sizning taxmin qilingan sonidan katta.")
        elif user_input > son:
            print("Taxmin qilingan son sizning taxmin qilingan sonidan kichkina.")
        else:
            print(f"Tabriklayman! Siz {son} sonini {harakatlar} harakatda topdingiz.")
            break

guess_the_number()
