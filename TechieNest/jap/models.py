from django.db import models
from django.contrib.auth.models import User

class TrainingRegistrationForm(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, blank = False)
	email = models.EmailField(max_length = 250, blank = False)
	contact_no = models.CharField(max_length = 10, blank = False)
	hometown = models.CharField(max_length = 50, blank = False)
	ss = '-- select state --'
	an = 'Andaman & Nicobar Island'
	ap = 'Arunachal Pradesh'
	#do the same as above for all the choices listed below
	state_choices = (
			(ss, '-- select state --'),(an, 'Andaman & Nicobar Island'),(ap, 'Arunachal Pradesh'),(anp, 'Andra Pradesh'),(a, 'Assam'),('Bihar'),
			(cd, 'Chandigarh'),(ct, 'Chattisgarh'),(d, 'Delhi'),(dn, 'Dadra & Nagar Haveli'),(dd, 'Daman & Diu'),(g, 'Goa'),
			(gj, 'Gujarat'),(h, 'Haryana'),(hp, 'Himachal Pradesh'),(jk, 'Jammu & Kashmir'),(j, 'Jharkhand'),(k, 'Karnataka'),
			(kr, 'Kerela'),(l, 'Lakshadweep'),(mp, 'Madhya Pradesh'),(m, 'Maharashtra'),(ma, 'Manipur'),(me, 'Meghalaya'),
			(mi, 'Mizoram'),(n, 'Nagaland'),(p, 'Pondicherry'),(o, 'Odisha'),(p, 'Punjab'),(r, 'Rajasthan'),
			(s, 'Sikkim'),(tn, 'Tamil Nadu'),(tr, 'Tripura'),(te, 'Telangana'),(up, 'Uttar Pradesh'),(uk, 'Uttarakhand'),
			(uc, 'Uttaranchal'),(wb, 'West Bengal'),
		)
	state = models.CharField(max_length = 100, choices = state_choices, default = ss)
	college = models.CharField(max_length = 100, blank = False)
	branch = models.CharField(max_length = 100, blank = False)
	current_semester_choices = (
			('-- current semester --'),('1'),('2'),('3'),('4'),('5'),
			('6'),('7'),('8'),('Passout'),
		)
	current_semester = models.CharField(max_length = 50, choices = current_semester_choices, default = '-- current semester --')
	registration_for_choices = (
			('-- select registration for --'),('Summer industrial internship/training program'),('Winter industrial internship/training program'),
			('Regular training program'),('Weekend training program'),('Job assurance program'),
		)
	registration_for = models.CharField(max_length =100, choices = registration_for_choices, default = '-- select registration for --')
	previous_exp_choices = (
			('-- select --'),('SITP'),('WITP'),('Workshop'),('Internship'),('Others'),
		)
	previous_exp = models.CharField(max_length = 200, choices = previous_exp_choices, default = '-- select --')
	how_did_you_know = models.CharField(max_length = 200)
	techienest_contactperson = models.CharField(max_length = 10)
