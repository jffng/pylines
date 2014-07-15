
from ghost import Ghost

url = "http://www.ebay.com/"
gh = Ghost()

# We load the main page of ebay
page, resources = gh.open(url, wait_onload_event=True)

# Full the main bar and click on the search button
gh.set_field_value("#gh-ac", "plane")
gh.click("#gh-btn")

# Wait for the next page
gh.wait_for_selector("#e1-15")

# Save the image of the screen
gh.capture_to("plane.png")
