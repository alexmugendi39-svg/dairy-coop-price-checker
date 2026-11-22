Kiambu Dairy Co-op - Payment Calculator v1.0
Simple tool for 30 farmer members. Farmer enters name + litres, sees total owed at today's price.

What you get
dairy_calculator.py - the tool
price.txt - weekly price, edit this to change price
No internet needed, no website needed
How to run (for farmers / staff)
Make sure Python is installed: python --version
Open terminal in this folder
Run: python dairy_calculator.py
Type farmer name, press Enter
Type litres, press Enter
How to change price each week (for manager)
Open price.txt
Delete old number, type new price. Example: 60.0
Save. Done. No code to touch.
Example output
Kiambu Dairy Co-op Payment Calculator
--------------------------------------
Current buying price: KES 55.00 per litre

Farmer name: Wanjiru
Litres supplied today: 12.5

Farmer : Wanjiru
Litres : 12.5
Price  : KES 55.00/litre
Total  : KES 687.50
Test cases passed
Wanjiru, 12.5 litres -> KES 687.50
Kamau, 20 litres -> KES 1,100.00
Achieng, 8 litres -> KES 440.00
Invalid: litres = "abc" -> shows clean error, does not crash
Invalid: litres = 0 / -5 -> shows "must be greater than zero"
Invalid: empty name -> shows "Name is required"
What is NOT in v1.0
No payment history / log - this is a separate add-on (see Stage 6)
No database
Price
KES 8,000 | 50% upfront, 50% on delivery

