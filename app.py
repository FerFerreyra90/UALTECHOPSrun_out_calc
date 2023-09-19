from flask import Flask, request, render_template
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_out_calc():
    if request.method == "POST":
        limit_type = request.form.get("limit_type")
        limit = int(request.form.get("limit"))
        current_date = datetime.now()
        if limit_type == "day":
            expiration_date = current_date + timedelta(days=limit)
        elif limit_type == "month":
            expiration_date = current_date + relativedelta(months=limit)
        elif limit_type == "year":
            expiration_date = current_date + relativedelta(years=limit)
        else:
            return "Invalid input"
        return render_template("resultado.html", expiration_date=expiration_date.strftime("%Y-%m-%d"))
    return render_template("formulario.html")
if __name__ == "__main__":
    app.run(debug=True)