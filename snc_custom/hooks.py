from . import __version__ as app_version

app_name = "snc_custom"
app_title = "SRANCO Custom App"
app_publisher = "Genirex pvt ltd"
app_description = "SRANCO Custom App"
app_icon = "fa-solid fa-book"
app_color = "grey"
app_email = "sales@genirex.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/snc_custom/css/snc_custom.css"
# app_include_js = "/assets/snc_custom/js/snc_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/snc_custom/css/snc_custom.css"
# web_include_js = "/assets/snc_custom/js/snc_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "snc_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "snc_custom.install.before_install"
# after_install = "snc_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "snc_custom.uninstall.before_uninstall"
# after_uninstall = "snc_custom.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "snc_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {/
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }

	"Quotation": {
		"on_submit": "snc_custom.custom_hooks.quotation.on_submit"
	},
	"Item": {
		"after_insert": "snc_custom.custom_hooks.item.create_todo"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"snc_custom.tasks.all"
# 	],
# 	"daily": [
# 		"snc_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"snc_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"snc_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"snc_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "snc_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "snc_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "snc_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"snc_custom.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
