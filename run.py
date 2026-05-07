from service import app, db
from service.models import Account

with app.app_context():
    db.create_all()

app.run(host="0.0.0.0", port=5000)