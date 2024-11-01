from app import create_app
import os
# from flask_migrate import Migrate


app = create_app(os.getenv('app_env') or 'dev')
# migrate = Migrate(movies_app, db)

if __name__ == '__main__':
    # movies_app.run(debug=True)
    print(app)
    app.run(host="0.0.0.0", port=5000)
