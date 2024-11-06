import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Input phone number
mobileNo = input("Number: ")
mobileNo = phonenumbers.parse(mobileNo)

# Display timezone, carrier, and geocoder information
print("Timezone: ", timezone.time_zones_for_number(mobileNo))  # Corrected here
print("Carrier: ", carrier.name_for_number(mobileNo, "en"))
print("Geocoder: ", geocoder.description_for_number(mobileNo, "en"))

# Check if the number is valid and possible
print("Valid Mobile Number:", phonenumbers.is_valid_number(mobileNo))
print("Checking the possibility of number:", phonenumbers.is_possible_number(mobileNo))
