import re

#accept input & strip unnecessary part
url = input("URL: ").strip()

<<<<<<< HEAD
#check input to match set format
=======
#conditional statement to
>>>>>>> 9432319 (add comments)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:" , matches.group(1))
