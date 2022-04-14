import frappe
from frappe import _
def create_todo(self, method):
	if self.is_sample:
		return
	doc = frappe.new_doc("ToDo")
	doc.priority = "High"
	doc.owner = "Administrator"
	doc.description = "New Item Created <a target='_blank' href={}>{}</a> by {}, Please Update The Commission Master under WEF Commission".format(self.get_url() ,self.item_code, self.owner)
	doc.insert()
	doc.save()
	frappe.msgprint("New ToDo Created Against {} to update WEF Commission".format(doc.owner))