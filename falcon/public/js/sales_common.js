frappe.ui.form.on(cur_frm.doctype, {
	setup: function(frm) {
		cur_frm.set_query('uom', 'items', function() {
			return {
				query: "falcon.api.get_item_uoms",
			};
		});
	}
});