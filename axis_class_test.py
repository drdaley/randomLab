import oneoverX 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
spine_dict = {'t':'top','r':'right','l':'left','b':'bottom'}
class ax_handler_class:
	def __init__(self,axis,xmin,xmax,ymin,ymax,h_spines,inv_bool=False,ma_tick_defs={},mi_tick_defs={},tick_label_defs={},datasets='',plot_now=False):
		self.axis = axis
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		self.h_spines = h_spines
		self.inv_bool = inv_bool
		#self.tick.locs = tick.locs
		self.ma_tick_defs = ma_tick_defs
		self.mi_tick_defs = mi_tick_defs
		self.tick_label_defs = tick_label_defs
		self.ds_array = datasets
		self.hide_spines()
		self.make_lims()
		self.make_ticks()
		self.make_ticklabels()
		if plot_now: self.plot()
		else:pass
	def hide_spines(self):
		for s in self.h_spines:
			self.axis.spines[spine_dict[s]].set_visible(False)
	def make_lims(self):
		if self.inv_bool: self.axis.set_xscale('oneoverX')
		else: pass
		self.axis.set_xlim(self.xmin,self.xmax)
		self.axis.set_ylim(self.ymin,self.ymax)	
	def make_ticks(self):
		if 'l' in self.ma_tick_defs.keys():
			self.axis.set_yticks(self.ma_tick_defs['l'],minor=False)
			self.axis.set_yticks(self.mi_tick_defs['l'],minor=True)
			self.axis.tick_params(axis='y',which='both', left=True)
		elif 'r' in self.ma_tick_defs.keys():
			self.axis.set_yticks(self.ma_tick_defs['r'],minor=False)
			self.axis.set_yticks(self.mi_tick_defs['r'],minor=True)
			self.axis.tick_params(axis='y',which='both', right=True)
		if 't' in self.ma_tick_defs.keys():
			self.axis.set_xticks(self.ma_tick_defs['t'],minor=False)
			self.axis.set_xticks(self.mi_tick_defs['t'],minor=True)
			self.axis.tick_params(axis='x',which='both', top=True)
		elif 'b' in self.ma_tick_defs.keys():
			self.axis.set_xticks(self.ma_tick_defs['b'],minor=False)
			self.axis.set_xticks(self.mi_tick_defs['b'],minor=True)
			self.axis.tick_params(axis='x',which='both', bottom=True)
	def make_ticklabels(self):	
		if 'l' in self.tick_label_defs.keys():
			self.axis.tick_params(axis='y', which=self.tick_label_defs['l'], labelleft=True)
		if 'r' in self.tick_label_defs.keys():
			self.axis.tick_params(axis='y', which=self.tick_label_defs['r'], labelright=True)
		if 't' in self.tick_label_defs.keys():
			self.axis.tick_params(axis='x', which=self.tick_label_defs['t'], labeltop=True)
		if 'b' in self.tick_label_defs.keys():
			self.axis.tick_params(axis='x', which=self.tick_label_defs['b'], labelbottom=True)
	
	def plot(self):
		for y_data in self.ds_array[1:]:
			self.axis.plot(self.ds_array[0],y_data)

# begin main block
if __name__ == '__main__':
	
	#fig = plt.figure(figsize=(3.5,3))
	#data = np.array(np.loadtxt(os.path.join('..','data','redox','sample1_MOM2catPhPhFc','nir_ox1','abs_Absorbance_00005.txt'),skiprows=17,unpack=True))
	#data1 = np.array(np.loadtxt(os.path.join('..','data','redox','sample1_MOM2catPhPhFc','nir_ox1','abs_Absorbance_00007.txt'),skiprows=17,unpack=True))
	#data2 = np.concatenate((data,data1), axis=0)
	#print(data2)
	# make the grid and figure
	gs1 = gridspec.GridSpec(1,3,width_ratios=[1,1,1],left=0.05, right=0.99)
	fig = plt.figure(figsize=(7,4))
	
	axis_number_one = fig.add_subplot(gs1[0]) 
	axis_number_two = fig.add_subplot(gs1[1]) 
	axis_number_three = fig.add_subplot(gs1[2]) 
	data1 = np.array(np.loadtxt(os.path.join('..','data','redox','sample1_MOM2catPhPhFc','nir_ox1','abs_Absorbance_00004.txt'),skiprows=17,unpack=True))
	data2 = np.array(np.loadtxt(os.path.join('..','data','redox','sample1_MOM2catPhPhFc','nir_ox1','abs_Absorbance_00005.txt'),skiprows=17,unpack=True))
	data3 = np.array(np.loadtxt(os.path.join('..','data','redox','sample1_MOM2catPhPhFc','nir_ox1','abs_Absorbance_00007.txt'),skiprows=17,unpack=True))
	a1 = ax_handler_class(axis_number_one,1000,2000,-1,2,'tr',inv_bool=False,ma_tick_defs={'b':list(range(1200,1600,200))},mi_tick_defs={'b':list(range(1200,1600,10))},tick_label_defs={'b':()},datasets=data1,plot_now=True)
	a2 = ax_handler_class(axis_number_two,1000,2000,-1,2,'tr',inv_bool=False,ma_tick_defs={'b':list(range(1200,1600,200))},mi_tick_defs={'b':list(range(1200,1600,10))},tick_label_defs={'b':()},datasets=data2,plot_now=True)
	a3 = ax_handler_class(axis_number_three,1000,2000,-1,2,'tr',inv_bool=False,ma_tick_defs={'b':list(range(1200,1600,200))},mi_tick_defs={'b':list(range(1000,1600,10))},tick_label_defs={'b':()},datasets=data3,plot_now=True)
  
	
	#a1.axis.plot(data[0],data[1])
	plt.show()