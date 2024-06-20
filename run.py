from app import create_app

app = create_app()

if __name__ == "__main__":
    reload = True
   
    app.run(debug=reload)