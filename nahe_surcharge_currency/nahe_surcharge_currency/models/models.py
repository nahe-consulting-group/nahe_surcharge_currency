# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PricelistItem(models.Model):
	_inherit = "product.pricelist.item"

	price_surcharge_currency_id = fields.Many2one('res.currency', 'Currency', store=True)

	def _compute_price(self, price, price_uom, product, quantity=1.0, partner=False):
		"""Compute the unit price of a product in the context of a pricelist application.
		The unused parameters are there to make the full context available for overrides.
		"""
		self.ensure_one()
		convert_to_price_uom = (lambda price: product.uom_id._compute_price(price, price_uom))
		if self.compute_price == 'fixed':
			price = convert_to_price_uom(self.fixed_price)
		elif self.compute_price == 'percentage':
			price = (price - (price * (self.percent_price / 100))) or 0.0
		else:
			# complete formula
			price_limit = price
			price = (price - (price * (self.price_discount / 100))) or 0.0
			if self.price_round:
				price = tools.float_round(price, precision_rounding=self.price_round)

			if self.price_surcharge:
				price_surcharge = convert_to_price_uom(self.price_surcharge)
				if self.price_surcharge_currency_id:
					if self.price_surcharge_currency_id != self.currency_id:
						date = self._context.get('date') or fields.Date.today()
						date = fields.Date.to_date(date)
						price_surcharge = self.price_surcharge_currency_id._convert(price_surcharge, self.currency_id, self.env.company, date, round=False)
						price += price_surcharge
				else:
					price += price_surcharge

			if self.price_min_margin:
				price_min_margin = convert_to_price_uom(self.price_min_margin)
				price = max(price, price_limit + price_min_margin)

			if self.price_max_margin:
				price_max_margin = convert_to_price_uom(self.price_max_margin)
				price = min(price, price_limit + price_max_margin)
		return price
