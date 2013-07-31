from google.appengine.ext import db

class Category(db.Model):
	description = db.TextProperty()
	image = db.BlobProperty()

class Product(db.Model):
	description = db.TextProperty()
	category = db.ReferenceProperty(Category)
	image = db.BlobProperty()
	price = db.FloatProperty()