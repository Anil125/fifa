from datetime import datetime, timedelta
import time
from openerp.osv import fields, osv


class sale_order(osv.osv):
	#_name = "sale.order"
    _inherit = "crm.lead"
    _description = "editing opportunity"
 

    _columns = {
		'state_lead': fields.selection(
                [('new', 'New'),('opportunity', 'Opportunity'),('dead', 'Dead')],'Status'),
        'function1' :fields.char("job Title"),
		'categories' :fields.many2one('res.partner.category',"Categories"),
		'lead_source' : fields.many2one('crm.tracking.medium',"Lead Source"),
		'user_id':fields.many2one('res.users','Sals Executive'),
		'section_id' : fields.many2one('crm.case.section',"sales Team"),
		'compny_id' : fields.many2one('res.company',"Company"),
		'priority_ids' : fields.selection([('vl','very low'),('l','Low'),('m','Medium'),('h','high'),('vh','very high')],"Priority"),
		'active_id' : fields.boolean("Active"),
		'brand_id' : fields.many2one('sale.brand',"Brand"),
	}	
    def cancel_case(self, cursor, user, ids, context=None):
        #print "Hello, I created my first button"
        return self.write(cursor, user, ids, {'state': 'opportunity'})

	

class sale_order_brand(osv.osv):
    _name = "sale.brand"
    _description = "editing opportunity"
    _rec_name = "name_id" 


    _columns = {
        'name_id' : fields.char("Name",required=True),
	    'type_id' : fields.selection([('r','Radio'),('t','TV'),('d','Digital')],"Type",required=True),
        'companyid' : fields.many2one('res.company',"Company",required=True),
	}	
	
