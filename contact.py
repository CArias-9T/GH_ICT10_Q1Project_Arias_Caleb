from pyscript import display

# variables for contacts

restaurant_name = 'Overloaded'
owner_name = 'Caleb Arias'
year_established = 2023
business_address = '3 Eisenhower St, San Juan City, 1503 Metro Manila'
has_delivery = True
phone_number = '+63 9444181143'
business_hours = ['9:00 AM', '8:00 PM']
business_email = 'arias.cm@obmontessori.edu.ph'
tax_rate = 0.12


#header
display(f"{restaurant_name}, a restaurant by {owner_name}!", target='ownername')
display(f"• Est. {year_established} •", target='established')

#contacts

display(f"{business_address}", target='businessaddress')
display(f"{phone_number}", target='phonenumber')
display(f"{business_email}", target='businessemail')


#footer

display(f"Caleb Arias | 10-Topaz | We are open around {business_hours[0]} to {business_hours[1]}!", target='footer')