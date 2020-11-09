# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _
 
# nama class bebas asalkan extends ke class Model
class Modul_IsiKulkasku(models.Model):
 # _inherit digunakan jika kita akan mengoveride model yang sudah ada
 # model sale.order terdapat di module sale bawaan Odoo
 # jika model tidak tersedia / belum terinstall akan menyebabkan error
 _inherit = 'sale.order'
 
 # buat kolom database dengan nama makelar, type data varchar dan wajik diisi
 # type data lainnya akan dijelaskan pada tulisan yang lain
 makelar = fields.Char("Makelar", required=True)