import datetime

README_PATH = "README.md"
BADGE_URL = "https://tryhackme-badges.s3.amazonaws.com/khyr.png"

def update_readme():
    # Generate the current timestamp
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    cache_busted_url = f"{BADGE_URL}?timestamp={timestamp}"

    # Read the README.md content
    with open(README_PATH, "r") as file:
        content = file.read()

    # Replace the placeholder with the updated URL
    updated_content = content.replace("https://tryhackme-badges.s3.amazonaws.com/khyr.png?timestamp=<!-- TIMESTAMP -->", cache_busted_url)

    # Write the updated content back to README.md
    with open(README_PATH, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()