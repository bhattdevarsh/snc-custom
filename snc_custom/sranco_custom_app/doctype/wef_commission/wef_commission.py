# Copyright (c) 2022, Genirex pvt ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WEFCommission(Document):
	def validate(self):
		self.updated_by = frappe.session.user