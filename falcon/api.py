# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_item_uoms(doctype, txt, searchfield, start, page_len, filters):
	cond = ''
	if filters and filters.get('item_code'):
		item_code = filters.get('item_code')
		cond = " item.item_code = '%s'" % item_code

	return frappe.db.sql("""select  uom.uom from `tabUOM Conversion Detail` uom
			inner join `tabItem` item
			where item.name=uom.parent
			where {cond}
			order by name limit %(start)s, %(page_len)s"""
			.format(cond=cond), {
				'start': start, 'page_len': page_len
			})
