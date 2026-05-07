from flask import jsonify, request
from service import app, db
from service.models import Account

@app.route("/accounts", methods=["GET"])
def list_accounts():
    accounts = Account.query.all()
    return jsonify([a.serialize() for a in accounts])


@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()

    account = Account(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(account)
    db.session.commit()

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    }), 201

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):

    account = Account.query.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()

    account.name = data["name"]
    account.email = data["email"]

    db.session.commit()

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    })

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):

    account = Account.query.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    })


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):

    account = Account.query.get(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    db.session.delete(account)
    db.session.commit()

    return jsonify({"message": "Account deleted"})