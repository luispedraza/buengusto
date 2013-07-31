#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from bg_base import *
from bg_data import *
import logging
from google.appengine.api import images

class MainHandler(BaseHandler):
	def get(self):
		self.render("main.html")

class AboutHandler(BaseHandler):
	def get(self):
		self.render("about.html")

class ProductsHandler(BaseHandler):
	def get(self):
		self.render("products.html")

class ShopHandler(BaseHandler):
	def get(self):
		self.render("shop.html")

class AdminHandler(BaseHandler):
	def get(self):
		result = {}
		all_categories = Category.all()
		for c in all_categories:
			result[c.key().name()] = {
			"key": "%s" %c.key(),
			"description": c.description, 
			"products": {}}
		all_products = Product.all()
		for p in all_products:
			pname = p.key().name()
			cname = p.category.key().name()
			logging.info(cname)
			result[cname]["products"][pname] = {
			"key": "%s" %p.key(),
			"description": p.description,
			"price": p.price}
		logging.info(result)
		self.render("admin.html", products=result)
	def post(self):
		req_type = self.request.get("type")
		name = self.request.get("name")
		description = self.request.get("description")
		logging.info(description)
		image = self.request.get("image") or None
		if image:
			image = db.Blob(images.resize(image, 200, 200))
		if(req_type == "category"):
			category = Category.get_or_insert(name)
			category.description = description
			category.image = image
			category.put()
		elif(req_type == "product"):
			logging.info("es un producto")
			product = Product.get_or_insert(name)
			product.description = description
			product.image = image
			category = self.request.get("category")
			if not category:
				return
			product.category = db.Key(category)
			price = self.request.get("price")
			if not price:
				return
			product.price = float(price)
			product.put()
		self.get()

class ApiHandler(BaseHandler):
	def get(self):
		pass
class ImageHandler(webapp2.RequestHandler):
	def get(self):
		product = db.get(self.request.get("img_id"))
		if product.image:
			self.response.headers['Content-Type'] = 'image/png'
			self.response.out.write(product.image)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/admin', AdminHandler),
	('/about', AboutHandler),
	('/products', ProductsHandler),
	('/shop', ShopHandler),
	('/img', ImageHandler),
	('/api', ApiHandler)
], debug=True)
