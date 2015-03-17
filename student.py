from openerp.osv import osv, fields
from datetime import date
import datetime
import re


class student_ragistration(osv.osv):
    _name = "student_reg_rec"
   
    _columns = {
        'state': fields.selection(
                [('new', 'New'),('approve', 'Approve'),('confirmed', 'Confirmed')], 'Status'),
		'seq_id_a' : fields.char("Sequence", readonly=True),
		'student_id' : fields.char("Student Id"),
		'student_fname' : fields.char("Name"),
		'student_mname' : fields.char(" "),
		'student_lname' : fields.char(" "),
		'sex' : fields.selection([('m','Male'),('f','Female')],"Gender"),
		'mob_no' : fields.char("Mobile No."),
		'street': fields.char('Address'),
        'street2': fields.char(' '),
        'zip': fields.char(' ', change_default=True, size=24),
        'city': fields.char(" "),
        'state_id': fields.many2one("state_reg", ' '),
        'country_id': fields.many2one('country_reg', ' '),
		'date_of_birth': fields.date("DOB"),
		'email' : fields.char("Email Id"),
		'age': fields.char("Age"),
#------------------parents information address--------------------------------
		'parent_fname' : fields.char("Name"),
		'parent_mname' : fields.char(" "),
		'parent_lname' : fields.char(" "),
		'parent_occupation' : fields.char("Occupation"),
		'sex_' : fields.selection([('m','Male'),('f','Female')],"Gender"),
		'pmob_no' : fields.char("Mobile No."),
		'pstreet': fields.char('Address'),
        'pstreet2': fields.char(' '),
        'pzip': fields.char(' ', change_default=True, size=24),
        'pcity': fields.char(" "),
        'pstate_id': fields.many2one("state_reg", ' '),
        'pcountry_id': fields.many2one('country_reg', ' '),
		'pdate_of_birth': fields.date("DOB"),
		'pEmail Id' : fields.char("Email Id"),
#---------------------------
		'course_name' :fields.selection([('mca',"MCA"),('btech','BTECH')],"Course"),
		'branch_name' : fields.selection([("cs","CS"),('it',"IT"),('me','ME')],"Branch"),
#---------------------------------------------------------------------------------------------------------
       #shoplist = ['apple', 'mango', 'carrot', 'banana']	

}
 
    _defaults = {
		'state': 'new',
		'seq_id_a':"Sequence#"
		}

    def create(self, cr, user, vals, context=None):
     vals['seq_id_a'] =\
     self.pool.get('ir.sequence').get(cr, user, 'rec_seq')
     return super(student_ragistration, self).create(cr, user, vals, context)

    def mymod_new(self, cr, uid, ids):
     #print"------------"
     #self.write(cr, uid, ids, { 'state' : 'new' })
     return True


    def mymod_approve(self, cr, uid, ids):
     print"------------"
     self.write(cr, uid, ids, { 'state' : 'approve' })
     return True

    def mymod_confirmed(self, cr, uid, ids):
     self.write(cr, uid, ids, { 'state' : 'confirmed' })
     return True
#---------------methods for constraints-------------------
    def mob_no_cons(self, cr, uid, ids, context=None):
     record = self.browse(cr, uid, ids, context=context)
     print "``````````````````````````````````````", context
     for data in record:
      if len(data.mob_no) <10:
        return False	
      return True

    _constraints = [
     (mob_no_cons, 'Error: You have entered an invalid mobile number', ['mob_no']),
      ]  

    def onchange_email(self, cr, uid, ids, email):
     if email:
      if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
       return True
      else:
       raise osv.except_osv('Invalid Email',"Please enter a valid email address")  

    def onchange_zip_code(self, cr, uid, ids, zip): 
     if zip: 
      if len(zip)==6: 
       return True 
      else: 
         raise osv.except_osv('Invalid zip_code Code',"Please enter a valid zip_code Code")



    '''def onchange_getage_id(self,cr,uid,ids,date_of_birth,context=None):
        current_date=datetime.now()
        current_year=current_date.year
        birth_date = parser.parse(date_of_birth)
        current_age=current_year-birth_date.year
        val = {
            'age':current_age
        }
        return {'value': val}'''






  #-----------------other relational classes----------------
class student_state(osv.osv):
    _name = "state_reg"
    _rec_name='State Name'
    _columns = {
		'State Name':fields.char(""),
}
class student_country(osv.osv):
    _name = "country_reg"
    _rec_name='Country Name'
    _columns = {
		'Country Name':fields.char(""),
}
#--------------------------------------------------
    
    
