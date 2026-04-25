import easyocr
import os

# First, show all files in photos folder
print("📁 Files in 'photos' folder:")
print("-" * 40)

if os.path.exists("photos"):
    files = os.listdir("photos")
    for f in files:
        print(f"   {f}")
    print("-" * 40)
else:
    print("   ❌ 'photos' folder not found!")
    exit()

# Find first image file
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
image_file = None

for f in files:
    if f.lower().endswith(image_extensions):
        image_file = os.path.join("photos", f)
        break

if not image_file:
    print("❌ No image files found in photos folder!")
    exit()

print(f"\n🔍 Reading: {image_file}\n")

reader = easyocr.Reader(['en'], gpu=False, verbose=False)
results = reader.readtext(image_file)

print("=" * 60)
print("ALL TEXT FOUND BY OCR:")
print("=" * 60)

for (bbox, text, confidence) in results:
    print(f"   '{text}' ({confidence:.0%})")

print("=" * 60)
print("\nFULL COMBINED TEXT:")
print("=" * 60)
full_text = " ".join([r[1] for r in results])
print(full_text)
print("=" * 60)