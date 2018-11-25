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
	anp = 'Andra Pradesh'
	a = 'Assam'
	b = 'Bihar'
	cd = 'Chandigarh'
	ct = 'Chattisgarh'
	d = 'Delhi'
	dn = 'Dadra & Nagar Haveli'
	dd = 'Daman & Diu'
	g = 'Goa'
	gj = 'Gujarat'
	h = 'Haryana'
	hp = 'Himachal Pradesh'
	jk = 'Jammu & Kashmir'
	j = 'Jharkhand'
	k = 'Karnataka'
	kr = 'Kerela'
	l = 'Lakshadweep'
	mp = 'Madhya Pradesh'
	m = 'Maharashtra'
	ma = 'Manipur'
	me = 'Meghalaya'
	mi = 'Mizoram'
	n = 'Nagaland'
	p = 'Pondicherry'
	o = 'Odisha'
	p = 'Punjab'
	r = 'Rajasthan'
	s = 'Sikkim'
	tn = 'Tamil Nadu'
	tr = 'Tripura'
	te = 'Telangana'
	up = 'Uttar Pradesh'
	uk = 'Uttarakhand'
	uc = 'Uttaranchal'
	wb = 'West Bengal'
	state_choices = (
			(ss, '-- select state --'),(an, 'Andaman & Nicobar Island'),(ap, 'Arunachal Pradesh'),(anp, 'Andra Pradesh'),(a, 'Assam'),(b ,'Bihar'),
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
	scs = '-- current semester --'
	one = '1'
	two = '2'
	three = '3'
	four = '4'
	five = '5'
	six = '6'
	seven = '7'
	eight = '8'
	passout = 'Passout'
	current_semester_choices = (
			(scs, '-- current semester --'),(one, '1'),(two, '2'),(three, '3'),(four, '4'),(five, '5'),
			(six, '6'),(seven, '7'),(eight, '8'),(passout, 'Passout'),
		)
	current_semester = models.CharField(max_length = 50, choices = current_semester_choices, default = '-- current semester --')
	srf = '-- select registration for --'
	winter = 'Winter industrial internship/training program'
	summer =  'Summer industrial internship/training program'
	regular = 'Regular training program'
	week = 'Weekend training program'
	jap = 'Job assurance program'
	registration_for_choices = (
			(srf, '-- select registration for --'),(summer, 'Summer industrial internship/training program'),(winter, 'Winter industrial internship/training program'),
			(regular, 'Regular training program'),(week, 'Weekend training program'),(jap, 'Job assurance program'),
		)
	registration_for = models.CharField(max_length =100, choices = registration_for_choices, default = '-- select registration for --')
	spe = '-- select --'
	sitp = 'SITP'
	witp = 'WITP'
	wor = 'Workshop'
	inte = 'Internship'
	oth = 'Others'
	previous_exp_choices = (
			(spe, '-- select --'),(sitp, 'SITP'),(witp, 'WITP'),(wor, 'Workshop'),(inte, 'Internship'),(oth, 'Others'),
		)
	previous_exp = models.CharField(max_length = 200, choices = previous_exp_choices, default = spe)
	how_did_you_know = models.CharField(max_length = 200)
	techienest_contactperson = models.CharField(max_length = 10)
