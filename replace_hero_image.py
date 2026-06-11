
import base64

# Read the HTML file
with open(r"c:\Users\Wajiz.pk\OneDrive\Documents\Desktop\abc\muskan_portfolio-1 (1).html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Read the new image and convert to base64
with open(r"c:\Users\Wajiz.pk\OneDrive\Documents\Desktop\abc\pic1.jpg", "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode('utf-8')

# Create the new src attribute
new_src = f"data:image/jpeg;base64,{base64_image}"

# Find and replace the hero-photo's src
# First, let's find the line with hero-photo
old_img_tag = html_content.split('class="hero-photo" src="')[1].split('"')[0]
new_html_content = html_content.replace(old_img_tag, new_src)

# Write back the updated HTML
with open(r"c:\Users\Wajiz.pk\OneDrive\Documents\Desktop\abc\muskan_portfolio-1 (1).html", "w", encoding="utf-8") as f:
    f.write(new_html_content)

print("Successfully replaced the hero image!")

