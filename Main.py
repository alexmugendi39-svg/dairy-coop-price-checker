
"""
Dairy Co-op Price Checker - WEB version for Vercel
Same logic as dairy_calculator.py, but as a website.
Farmers open the link on phone, type name + litres, see total.
CLI file dairy_calculator.py is still there for offline use.
"""
from flask import Flask, request, render_template_string

app = Flask(__name__)

def get_current_price():
    try:
        with open("price.txt", "r") as f:
            return float(f.read().strip())
    except:
        return 55.0

def calculate_payment(litres, price):
    return litres * price

HTML = """
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kiambu Dairy Co-op - Price Checker</title>
<style>
body{font-family:system-ui,sans-serif;max-width:520px;margin:30px auto;padding:0 16px;background:#f6f7f9}
.card{background:#fff;padding:24px;border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.07)}
h1{margin:0 0 4px;font-size:24px} p{color:#555}
.price{background:#e8f5e9;padding:12px;border-radius:10px;text-align:center;font-weight:700;font-size:18px;margin:16px 0}
label{display:block;margin:14px 0 4px;font-weight:600}
input{width:100%;padding:12px;box-sizing:border-box;border:1px solid #ddd;border-radius:10px;font-size:16px}
button{background:#0a7a42;color:#fff;border:0;padding:14px;border-radius:10px;width:100%;font-size:16px;font-weight:700;margin-top:18px;cursor:pointer}
.result{background:#e8f5e9;padding:16px;border-radius:10px;margin-top:18px}
.result b{font-size:22px}
small{color:#777}
.error{background:#fde8e8;padding:12px;border-radius:10px;margin-top:16px}
</style></head><body>
<div class="card">
<h1>🐄 Kiambu Dairy Co-op</h1>
<p>Price Checker — enter your name and litres supplied today.</p>
<div class="price">Today's Price: KES {{ price:.2f }} / litre</div>
<form method="post" action="/calculate">
<label>Farmer Name</label><input type="text" name="name" placeholder="e.g. Wanjiru" required>
<label>Litres Supplied Today</label><input type="number" name="litres" step="0.1" min="0.1" placeholder="e.g. 12.5" required>
<button type="submit">Calculate My Payment →</button>
</form>
{% if error %}<div class="error">❌ {{ error }}</div>{% endif %}
{% if result %}
<div class="result">
Farmer: <b>{{ result.name }}</b><br>
Litres: {{ result.litres }}<br>
Price: KES {{ price:.2f }}/litre<br>
Total Owed: <b>KES {{ "%.2f"|format(result.total) }}</b><br><br>
<small>Please collect payment from the co-op office. Thank you!</small>
</div>
{% endif %}
<p><small>Manager: to change price, edit <code>price.txt</code> in GitHub (e.g. 55.0 → 60.0) and redeploy. No code change needed.</small></p>
</div></body></html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML, price=get_current_price(), result=None, error=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    price = get_current_price()
    name = request.form.get("name", "").strip()
    litres_raw = request.form.get("litres", "").strip()
    if not name:
        return render_template_string(HTML, price=price, result=None, error="Name is required.")
    try:
        litres = float(litres_raw)
        if litres <= 0:
            raise ValueError()
    except ValueError:
        return render_template_string(HTML, price=price, result=None, error="Please enter a valid number for litres. Example: 12.5")
    total = calculate_payment(litres, price)
    return render_template_string(HTML, price=price, result={"name": name, "litres": litres, "total": total}, error=None)

@app.route("/health")
def health():
    return {"status": "ok", "price": get_current_price()}

if __name__ == "__main__":
    app.run(debug=True)
