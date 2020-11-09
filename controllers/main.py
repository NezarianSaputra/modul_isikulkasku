from odoo.addons.website_sale.controllers.main import WebsiteSale


class Shop(http.Controllers):
		
	@http.route('/sale/support', type='http', website=True)
		def sale_support(self, **kwargs):
		return "Heloo, World"
    	# controller ini hanya untuk merender form
    	# return request.render('tutorial_controller.sale_support')
    
    # @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
    # def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
    #     sale_order = request.website.sale_get_order(force_create=True)
    #     if sale_order.state != 'draft':
    #         request.session['sale_order_id'] = None
    #         sale_order = request.website.sale_get_order(force_create=True)
    #     sale_order._cart_update(
    #         product_id=int(product_id),
    #         add_qty=add_qty,
    #         set_qty=set_qty,
    #         attributes=self._filter_attributes(**kw),
    #     )
    #     return request.redirect("/shop/cart")

    # def _filter_attributes(self, **kw):
    #     return {k: v for k, v in kw.items() if "attribute" in k}