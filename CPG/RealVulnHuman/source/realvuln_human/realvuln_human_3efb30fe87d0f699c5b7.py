db.session.add(transaction)

                # Update balances
                users[sender].balance -= Decimal(str(amount))
                users[receiver].balance += Decimal(str(amount))

        db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True, port=5000)
