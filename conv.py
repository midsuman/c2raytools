#Various values and functions to deal with unit conversions regarding file types

import const
import numpy as np
import utils 

#Conversion factors and other stuff relating to C2Ray simulations
boxsize=114.0
LB=boxsize/const.h
nbox_fine=6144

M_box      = const.rho_matter*(LB*const.Mpc)**3 # mass in box (g, not M0)
M_grid     = M_box/(float(nbox_fine)**3)

#conversion factor for the velocity (sim units to km/s)
lscale = (LB)/float(nbox_fine)*const.Mpc # size of a cell in cm, comoving
tscale = 2.0/(3.0*np.sqrt(const.Omega0)*const.H0/const.Mpc*1.e5) # time scale, when divided by (1+z)2
velconvert = lambda z: lscale/tscale*(1.0+z)/1.e5

def set_sim_constants(boxsize_cMpc):
	'''This method will set the values of relevant constants depending on the simulation
	boxsize_cMpc is the box size in cMpc/h
	It can be 37, 64, 114 or '''
	global boxsize, LB, nbox_fine, M_box, M_grid, lscale, tscale, velconvert

	#hf.print_msg('Setting constants for boxsize=%.3f cMpc' % boxsize_cMpc)
	boxsize = boxsize_cMpc
	LB = boxsize/const.h	
	#First argument is added by me
	if utils.flt_comp(boxsize, 500.):
		utils.print_msg('Setting conversion factors for 500/h Mpc box')
		nbox_fine = 13824
	elif utils.flt_comp(boxsize, 425.):
		utils.print_msg('Setting conversion factors for 425/h Mpc box')
		nbox_fine = 10976
	elif utils.flt_comp(boxsize, 114.):
		utils.print_msg('Setting conversion factors for 114/h Mpc box')
		nbox_fine = 6144
	elif utils.flt_comp(boxsize, 64.):
		utils.print_msg('Setting conversion factors for 64/h Mpc box')
		nbox_fine = 3456
	elif utils.flt_comp(boxsize, 37.):
		utils.print_msg('Setting conversion factors for 37/h Mpc box')
		nbox_fine = 2048
	else:
		raise Exception('Invalid boxsize (%.3f cMpc)' % boxsize_cMpc)

	M_box      = const.rho_matter*(LB*const.Mpc)**3 # mass in box (g, not M0)
	M_grid     = M_box/(float(nbox_fine)**3)
	lscale = (LB)/float(nbox_fine)*const.Mpc # size of a cell in cm, comoving
	tscale = 2.0/(3.0*np.sqrt(const.Omega0)*const.H0/const.Mpc*1.e5) # time scale, when divided by (1+z)2
	velconvert = lambda z: lscale/tscale*(1.0+z)/1.e5
