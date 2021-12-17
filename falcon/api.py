# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.contacts.doctype.address.address import get_address_display


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_item_uoms(doctype, txt, searchfield, start, page_len, filters):
	cond = ''
	if filters and filters.get('item_code'):
		item_code = filters.get('item_code')
		cond = "and item.item_code = '%s'" % item_code
	print(cond,'cond'*100)
	return frappe.db.sql("""select  uom.uom from `tabUOM Conversion Detail` uom
			inner join `tabItem` item
			where item.name=uom.parent
			{cond}
			order by uom.uom limit %(start)s, %(page_len)s"""
			.format(cond=cond), {
				'start': start, 'page_len': page_len
			})



@frappe.whitelist()
def get_customers_address(customer_name):
	address_field=frappe.db.get_value('Customer', customer_name, 'customer_primary_address')
	if address_field:
		return get_address_display(address_field)
	else:
		return