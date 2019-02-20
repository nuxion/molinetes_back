from molinetes import create_app

app = create_app({'SECRET_KEY': 'dev'})

if __name__ == '__main__':
    app.run()
