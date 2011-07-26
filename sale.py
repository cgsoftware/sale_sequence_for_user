# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv

class sale_order(osv.osv):
  _inherit="sale.order"

  
  _defaults = {
                'name': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'sale.order'+ 
                obj.pool.get('res.users').read(cr, uid, uid, ['name'], context=context)['name']),
                                                                                      

                }


   

sale_order()

