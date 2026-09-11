
from PIL import Image, ImageEnhance
from pathlib import Path


# -------------------------
# پوشه‌های ورودی و خروجی
# -------------------------
input_folder = Path("input")
output_folder = Path("output")

# اگر output وجود نداشت، بساز
output_folder.mkdir(exist_ok=True)


# -------------------------
# تنظیمات ثابت
# -------------------------

# اندازه جدید
new_size = (1280, 720)

# محدوده Crop
# left, top, right, bottom
crop_box = (340, 160, 940, 560)


# -------------------------
# دریافت تنظیمات از کاربر
# -------------------------

print("=" * 50)
print("       IMAGE PROCESSOR")
print("=" * 50)

# Brightness
while True:
    try:
        brightness_value = float(
            input("Brightness (1.0 = normal): ")
        )

        if brightness_value > 0:
            break

        print("Brightness must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


# Contrast
while True:
    try:
        contrast_value = float(
            input("Contrast (1.0 = normal): ")
        )

        if contrast_value > 0:
            break

        print("Contrast must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


print("\nStarting image processing...")
print("-" * 50)


# -------------------------
# پردازش تصاویر
# -------------------------

processed_count = 0

for image_path in input_folder.iterdir():

    # فقط فایل‌ها را پردازش کن
    if image_path.is_file():

        try:
            # -------------------------
            # باز کردن تصویر
            # -------------------------
            image = Image.open(image_path)

            print(f"Processing: {image_path.name}")
            print(f"Original size: {image.size}")

            # -------------------------
            # Resize
            # -------------------------
            resized_image = image.resize(new_size)

            print(f"Resized size: {resized_image.size}")

            # -------------------------
            # Crop
            # -------------------------
            cropped_image = resized_image.crop(crop_box)

            print(f"Cropped size: {cropped_image.size}")

            # -------------------------
            # Brightness
            # -------------------------
            brightness = ImageEnhance.Brightness(cropped_image)
            bright_image = brightness.enhance(brightness_value)

            # -------------------------
            # Contrast
            # -------------------------
            contrast = ImageEnhance.Contrast(bright_image)
            final_image = contrast.enhance(contrast_value)

            # -------------------------
            # تبدیل به RGB
            # -------------------------
            if final_image.mode != "RGB":
                final_image = final_image.convert("RGB")

            # -------------------------
            # مسیر خروجی
            # -------------------------
            output_path = output_folder / f"{image_path.stem}.jpg"

            # -------------------------
            # ذخیره
            # -------------------------
            final_image.save(
                output_path,
                "JPEG",
                quality=95
            )

            print(f"Saved: {output_path}")
            print("-" * 50)

            processed_count += 1

        except Exception as error:
            print(f"Error processing {image_path.name}: {error}")
            print("-" * 50)


# -------------------------
# نتیجه نهایی
# -------------------------

print("\nProcessing completed!")
print(f"Images processed: {processed_count}")

