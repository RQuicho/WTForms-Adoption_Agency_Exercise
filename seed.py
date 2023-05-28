from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Clear any existing data in tables
Pet.query.delete()

# Add sample data
p1 = Pet(name='Eeyore', species='donkey', photo_url='https://wallpapercave.com/wp/womqvTH.jpg', age=5, notes='pessimistic, gloomy, and depressed')
p2 = Pet(name='Piglet', species='pig', photo_url='https://womenwriteaboutcomics.com/wp-content/uploads/2017/01/Piglet.jpg', age=2, notes='timid, brave, friendly', available=0)
p3 = Pet(name='Kanga', species='kangaroo', photo_url='https://clipartspub.com/images/pooh-clipart-kanga-8.jpg', age=10, notes='hospitable, gentle', available=1)
p4 = Pet(name='Rabbit', species='rabbit', age=10, notes='stubborn, helpful, loyal')

db.session.add_all([p1, p2, p3, p4])
db.session.commit()

