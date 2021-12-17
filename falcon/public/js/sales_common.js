frappe.ui.form.on(cur_frm.doctype, {
	setup: function(frm) {

		cur_frm.set_query("uom", "items", function(doc, cdt, cdn) {
			const row = locals[cdt][cdn];
			return {
				query: "falcon.api.get_item_uoms",
				filters: {
					'item_code': row.item_code
				}
			}
		});
	}
});