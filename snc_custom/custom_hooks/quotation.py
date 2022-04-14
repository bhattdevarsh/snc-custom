import frappe
from frappe import _
def on_submit(self, method):
    for item in self.items:
        if not item.tn_number: #Throw error if TN Number not entered
            frappe.throw(_("TN Number Does not Mentioned at the line {}!",item.idx))
        if frappe.db.exists("Item", "tn_number"): #Skip If TN Already Exists in Item
            continue
        frappe.db.set_value("Item", item.item_code, "tn_number", item.tn_number)