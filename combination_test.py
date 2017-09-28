from __future__ import unicode_literals
import oneoverX 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

colorwheel =('#ff3300','#ffa700','#f0ff00','#6fff00','#00ffec','#0051ff','#5600ff','#f000ff','#ff00a7')
symbolwheel = ('o','+','x','^')
if __name__ == '__main__':
  gs1 = gridspec.GridSpec(3,7,width_ratios=[5769, 4725,4354,5769, 4725,4354,4000],height_ratios=[1,1,1],left=0.05, right=0.99)
  fig = plt.figure(figsize=(7,4))
  RTA_axb1 = fig.add_subplot(gs1[0]) 
  RTA_axt1 = RTA_axb1.twiny()
  RTA_axb2 = fig.add_subplot(gs1[1]) 
  RTA_axt2 = RTA_axb2.twiny()
  RTA_axb3 = fig.add_subplot(gs1[2])
  RTA_axt3 = RTA_axb3.twiny()
  RTA_axb4 = fig.add_subplot(gs1[7])
  RTA_axt4 = RTA_axb4.twiny()
  RTA_axb5 = fig.add_subplot(gs1[8])
  RTA_axt5 = RTA_axb5.twiny()
  RTA_axb6 = fig.add_subplot(gs1[9])
  RTA_axt6 = RTA_axb6.twiny()
  RTA_axb7 = fig.add_subplot(gs1[14])
  RTA_axt7 = RTA_axb7.twiny()
  RTA_axb8 = fig.add_subplot(gs1[15])
  RTA_axt8 = RTA_axb8.twiny()
  RTA_axb9 = fig.add_subplot(gs1[16])
  RTA_axt9 = RTA_axb9.twiny()
  #axb4 = fig.add_subplot(gs1[3])
  RTA_axlt1 = fig.add_subplot(gs1[6])
  RTA_axlt1.set_xscale('log')
  #RTA_axlt1.set_yscale('logit')
  RTA_axlt2 = fig.add_subplot(gs1[13])
  RTA_axlt3 = fig.add_subplot(gs1[20])
  RTA_axlt2.set_xscale('log')
  #RTA_axlt2.set_yscale('logit')
  RTA_axlt3.set_xscale('log')
  #RTA_axlt3.set_yscale('logit')
  RTA_axb4.set_ylabel('ΔAbs (mA)', fontsize=8)
  RTA_axb8.set_xlabel('wavelength (nm)', fontsize=7)
  RTA_axt2.set_xlabel('wavenumber (1/cm)', fontsize=7)
  RTA_axlt3.set_xlabel('t (s)', fontsize=7)
  #gs1.tight_layout(fig, h_pad=None, w_pad=None)
  
  all_RTA_ax = [RTA_axb1,RTA_axb2,RTA_axb3,RTA_axb4,RTA_axb5,RTA_axb6,RTA_axb7,RTA_axb8,RTA_axb9,RTA_axt1,RTA_axt2,RTA_axt3,RTA_axt4,RTA_axt5,RTA_axt6,RTA_axt7,RTA_axt8,RTA_axt9,RTA_axlt1,RTA_axlt2,RTA_axlt3]
  # End Axis definition block
  
  LD_axb1 = fig.add_subplot(gs1[3]) 
  LD_axt1 = LD_axb1.twiny()
  LD_axb2 = fig.add_subplot(gs1[4]) 
  LD_axt2 = LD_axb2.twiny()
  LD_axb3 = fig.add_subplot(gs1[5])
  LD_axt3 = LD_axb3.twiny()
  LD_axb4 = fig.add_subplot(gs1[10])
  LD_axt4 = LD_axb4.twiny()
  LD_axb5 = fig.add_subplot(gs1[11])
  LD_axt5 = LD_axb5.twiny()
  LD_axb6 = fig.add_subplot(gs1[12])
  LD_axt6 = LD_axb6.twiny()
  LD_axb7 = fig.add_subplot(gs1[17])
  LD_axt7 = LD_axb7.twiny()
  LD_axb8 = fig.add_subplot(gs1[18])
  LD_axt8 = LD_axb8.twiny()
  LD_axb9 = fig.add_subplot(gs1[19])
  LD_axt9 = LD_axb9.twiny()
  #axb4 = fig.add_subplot(gs1[3])
  
  #axb1.set_ylabel('ΔAbs (mA)', fontsize=8)
  LD_axb8.set_xlabel('wavelength (nm)', fontsize=7)
  LD_axt2.set_xlabel('wavenumber (1/cm)', fontsize=7)
  
  
  all_LD_ax = [LD_axb1,LD_axb2,LD_axb3,LD_axb4,LD_axb5,LD_axb6,LD_axb7,LD_axb8,LD_axb9,LD_axt1,LD_axt2,LD_axt3,LD_axt4,LD_axt5,LD_axt6,LD_axt7,LD_axt8,LD_axt9]
  # Begin stats
  RTA_ax_xlims = {RTA_axb1:(400,520),RTA_axb2:(540,725),RTA_axb3:(900,1480),RTA_axt1:(25000.0, 19230.76923076923),RTA_axt2:(18518.51851851852, 13793.103448275862),RTA_axt3:(11111.111111111111, 6756.756756756757),
              RTA_axb4:(400,520),RTA_axb5:(540,725),RTA_axb6:(900,1480),RTA_axt4:(25000.0, 19230.76923076923),RTA_axt5:(18518.51851851852, 13793.103448275862),RTA_axt6:(11111.111111111111, 6756.756756756757),
              RTA_axb7:(400,520),RTA_axb8:(540,725),RTA_axb9:(900,1480),RTA_axt7:(25000.0, 19230.76923076923),RTA_axt8:(18518.51851851852, 13793.103448275862),RTA_axt9:(11111.111111111111, 6756.756756756757),RTA_axlt1:(2.90E-02,5.50E+03),RTA_axlt2:(2.90E-02,5.50E+03),RTA_axlt3:(2.90E-02,5.50E+03)}
  
  RTA_ax_ylims = {RTA_axb1:(-0.005,0.01),RTA_axb2:(-0.005,0.01),RTA_axb3:(-0.005,0.01),RTA_axt1:0,RTA_axt2:0,RTA_axt3:0,
              RTA_axb4:(-0.0075,0.015),RTA_axb5:(-0.0075,0.015),RTA_axb6:(-0.0075,0.015),RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,
              RTA_axb7:(-0.0075,0.015),RTA_axb8:(-0.0075,0.015),RTA_axb9:(-0.0075,0.015),RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:(-0.005,0.01),RTA_axlt2:(-0.0075,0.015),RTA_axlt3:(-0.0075,0.015)}
  RTA_ax_matick= {RTA_axb1:0,RTA_axb2:0,RTA_axb3:0,RTA_axt1:(20000,24001,2000),RTA_axt2:(14000,18518,2000),RTA_axt3:(8000,11000,2000),
              #RTA_axb1:(400,521,40),RTA_axb2:(540,725,40),RTA_axb3:(900,1480,240),RTA_axt1:(20000,24001,2000),RTA_axt2:(14000,18518,2000),RTA_axt3:(8000,11000,2000),
              RTA_axb4:0,RTA_axb5:0,RTA_axb6:0,RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,
              #RTA_axb4:(400,521,40),RTA_axb5:(540,725,40),RTA_axb6:(900,1480,240),RTA_axt4:(20000,24001,2000),RTA_axt5:(14000,18518,2000),RTA_axt6:(8000,11000,2000),
              #RTA_axb7:(400,521,40),RTA_axb8:(540,725,40),RTA_axb9:(900,1480,240),RTA_axt7:(20000,24001,2000),RTA_axt8:(14000,18518,2000),RTA_axt9:(8000,11000,2000)}
              RTA_axb7:(400,521,40),RTA_axb8:(560,725,60),RTA_axb9:(900,1480,240),RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  RTA_ax_mitick= {RTA_axb1:(400,521,10),RTA_axb2:(540,725,10),RTA_axb3:(900,1480,10),RTA_axt1:(25000, 19230,-500),RTA_axt2:(13500,18500,500),RTA_axt3:(11000, 6756,-500),
              RTA_axb4:(400,521,10),RTA_axb5:(540,725,10),RTA_axb6:(900,1480,10),RTA_axt4:(25000, 19230,-500),RTA_axt5:(13793,18500,500),RTA_axt6:(11000, 6756,-500),
              RTA_axb7:(400,521,10),RTA_axb8:(540,725,10),RTA_axb9:(900,1480,10),RTA_axt7:(25000, 19230,-500),RTA_axt8:(13793,18500,500),RTA_axt9:(11000, 6756,-500),RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  RTA_ax_inv_bool = {RTA_axb1:1,RTA_axb2:1,RTA_axb3:1,RTA_axt1:0,RTA_axt2:0,RTA_axt3:0,
                RTA_axb4:1,RTA_axb5:1,RTA_axb6:1,RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,
                RTA_axb7:1,RTA_axb8:1,RTA_axb9:1,RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  RTA_y_bool = {RTA_axb1:1,RTA_axb2:0,RTA_axb3:0,RTA_axt1:0,RTA_axt2:0,RTA_axt3:0,RTA_axb4:1,RTA_axb5:0,RTA_axb6:0,RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,RTA_axb7:1,RTA_axb8:0,RTA_axb9:0,RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  RTA_tx_bool= {RTA_axb1:0,RTA_axb2:0,RTA_axb3:0,RTA_axt1:1,RTA_axt2:1,RTA_axt3:1,RTA_axb4:0,RTA_axb5:0,RTA_axb6:0,RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,RTA_axb7:0,RTA_axb8:0,RTA_axb9:0,RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  RTA_bx_bool= {RTA_axb1:0,RTA_axb2:0,RTA_axb3:0,RTA_axt1:0,RTA_axt2:0,RTA_axt3:0,RTA_axb4:0,RTA_axb5:0,RTA_axb6:0,RTA_axt4:0,RTA_axt5:0,RTA_axt6:0,RTA_axb7:1,RTA_axb8:1,RTA_axb9:1,RTA_axt7:0,RTA_axt8:0,RTA_axt9:0,RTA_axlt1:0,RTA_axlt2:0,RTA_axlt3:0}
  spine_dict = {'t':'top','r':'right','l':'left','b':'bottom'}
  RTA_h_spine= {RTA_axb1:'tbr',RTA_axb2:'tblr',RTA_axb3:'tlrb',RTA_axt1:'br',RTA_axt2:'blr',RTA_axt3:'blr',
            RTA_axb4:'trb',RTA_axb5:'tlrb',RTA_axb6:'tlrb',RTA_axt4:'brt',RTA_axt5:'blrt',RTA_axt6:'blrt',
            RTA_axb7:'tr',RTA_axb8:'tlr',RTA_axb9:'tlr',RTA_axt7:'brt',RTA_axt8:'blrt',RTA_axt9:'bltr',
            RTA_axlt1:'tr',RTA_axlt2:'tr',RTA_axlt3:'tr'}

  #dataget
  RTA_ML0x1,RTA_ML0y1,RTA_ML0y2,RTA_ML0y3,RTA_ML0y4,RTA_ML0y5,RTA_ML0y6,RTA_ML0y7= np.loadtxt('nb_rep_TA_proc.txt',delimiter='\t', skiprows=1, unpack=True)
  RTA_ML1x1,RTA_ML1y1,RTA_ML1y2,RTA_ML1y3,RTA_ML1y4,RTA_ML1y5= np.loadtxt('ph_rep_TA_proc.txt',delimiter='\t', skiprows=1, unpack=True)
  RTA_ML2x1,RTA_ML2y1,RTA_ML2y2,RTA_ML2y3,RTA_ML2y4,RTA_ML2y5,RTA_ML2y6,RTA_ML2y7= np.loadtxt('phph_rep_TA_proc.txt',delimiter='\t', skiprows=1, unpack=True)
  RTA_ML0ltxNIR,RTA_ML0lty1,dummy1,RTA_ML0lty2,dummy2,RTA_ML0ltxVIS,RTA_ML0lty3,dummy3,RTA_ML0lty4,dummy4,RTA_ML0lty5,dummy5 = np.loadtxt('nb_repKin.txt',delimiter='\t', skiprows=1, unpack=True)
  RTA_ML1ltxNIR,RTA_ML1lty1,dummy1,RTA_ML1lty2,dummy2,RTA_ML1ltxVIS,RTA_ML1lty3,dummy3,RTA_ML1lty4,dummy4,RTA_ML1lty5,dummy5 = np.loadtxt('ph_repKin.txt',delimiter='\t', skiprows=1, unpack=True)
  RTA_ML2ltxNIR,RTA_ML2lty1,dummy1,RTA_ML2lty2,dummy2,RTA_ML2ltxVIS,RTA_ML2lty3,dummy3,RTA_ML2lty4,dummy4,RTA_ML2lty5,dummy5 = np.loadtxt('phph_repKin.txt',delimiter='\t', skiprows=1, unpack=True)
  #RTA_ML1ltx
  #RTA_ML1ltx
  LD_ax_xlims = {LD_axb1:(400,520),LD_axb2:(540,725),LD_axb3:(900,1480),LD_axt1:(25000.0, 19230.76923076923),LD_axt2:(18518.51851851852, 13793.103448275862),LD_axt3:(11111.111111111111, 6756.756756756757),
              LD_axb4:(400,520),LD_axb5:(540,725),LD_axb6:(900,1480),LD_axt4:(25000.0, 19230.76923076923),LD_axt5:(18518.51851851852, 13793.103448275862),LD_axt6:(11111.111111111111, 6756.756756756757),
              LD_axb7:(400,520),LD_axb8:(540,725),LD_axb9:(900,1480),LD_axt7:(25000.0, 19230.76923076923),LD_axt8:(18518.51851851852, 13793.103448275862),LD_axt9:(11111.111111111111, 6756.756756756757)}
  
  LD_ax_ylims = {LD_axb1:(-0.005,0.01),LD_axb2:(-0.005,0.01),LD_axb3:(-0.005,0.01),LD_axt1:0,LD_axt2:0,LD_axt3:0,
              LD_axb4:(-0.0075,0.015),LD_axb5:(-0.0075,0.015),LD_axb6:(-0.0075,0.015),LD_axt4:0,LD_axt5:0,LD_axt6:0,
              LD_axb7:(-0.0075,0.015),LD_axb8:(-0.0075,0.015),LD_axb9:(-0.0075,0.015),LD_axt7:0,LD_axt8:0,LD_axt9:0}
  LD_ax_matick= {LD_axb1:0,LD_axb2:0,LD_axb3:0,LD_axt1:(20000,24001,2000),LD_axt2:(14000,18518,2000),LD_axt3:(8000,11000,2000),
              #LD_axb1:(400,521,40),LD_axb2:(540,725,40),LD_axb3:(900,1480,240),LD_axt1:(20000,24001,2000),LD_axt2:(14000,18518,2000),LD_axt3:(8000,11000,2000),
              LD_axb4:0,LD_axb5:0,LD_axb6:0,LD_axt4:0,LD_axt5:0,LD_axt6:0,
              #LD_axb4:(400,521,40),LD_axb5:(540,725,40),LD_axb6:(900,1480,240),LD_axt4:(20000,24001,2000),LD_axt5:(14000,18518,2000),LD_axt6:(8000,11000,2000),
              #LD_axb7:(400,521,40),LD_axb8:(540,725,40),LD_axb9:(900,1480,240),LD_axt7:(20000,24001,2000),LD_axt8:(14000,18518,2000),LD_axt9:(8000,11000,2000)}
              LD_axb7:(400,521,40),LD_axb8:(560,725,60),LD_axb9:(900,1480,240),LD_axt7:0,LD_axt8:0,LD_axt9:0}
  LD_ax_mitick= {LD_axb1:(400,521,10),LD_axb2:(540,725,10),LD_axb3:(900,1480,10),LD_axt1:(25000, 19230,-500),LD_axt2:(13500,18500,500),LD_axt3:(11000, 6756,-500),
              LD_axb4:(400,521,10),LD_axb5:(540,725,10),LD_axb6:(900,1480,10),LD_axt4:(25000, 19230,-500),LD_axt5:(13793,18500,500),LD_axt6:(11000, 6756,-500),
              LD_axb7:(400,521,10),LD_axb8:(540,725,10),LD_axb9:(900,1480,10),LD_axt7:(25000, 19230,-500),LD_axt8:(13793,18500,500),LD_axt9:(11000, 6756,-500)}
  LD_ax_inv_bool = {LD_axb1:1,LD_axb2:1,LD_axb3:1,LD_axt1:0,LD_axt2:0,LD_axt3:0,
                LD_axb4:1,LD_axb5:1,LD_axb6:1,LD_axt4:0,LD_axt5:0,LD_axt6:0,
                LD_axb7:1,LD_axb8:1,LD_axb9:1,LD_axt7:0,LD_axt8:0,LD_axt9:0}
  LD_y_bool = {LD_axb1:1,LD_axb2:0,LD_axb3:0,LD_axt1:0,LD_axt2:0,LD_axt3:0,LD_axb4:1,LD_axb5:0,LD_axb6:0,LD_axt4:0,LD_axt5:0,LD_axt6:0,LD_axb7:1,LD_axb8:0,LD_axb9:0,LD_axt7:0,LD_axt8:0,LD_axt9:0}
  LD_tx_bool= {LD_axb1:0,LD_axb2:0,LD_axb3:0,LD_axt1:1,LD_axt2:1,LD_axt3:1,LD_axb4:0,LD_axb5:0,LD_axb6:0,LD_axt4:0,LD_axt5:0,LD_axt6:0,LD_axb7:0,LD_axb8:0,LD_axb9:0,LD_axt7:0,LD_axt8:0,LD_axt9:0}
  LD_bx_bool= {LD_axb1:0,LD_axb2:0,LD_axb3:0,LD_axt1:0,LD_axt2:0,LD_axt3:0,LD_axb4:0,LD_axb5:0,LD_axb6:0,LD_axt4:0,LD_axt5:0,LD_axt6:0,LD_axb7:1,LD_axb8:1,LD_axb9:1,LD_axt7:0,LD_axt8:0,LD_axt9:0}
  spine_dict = {'t':'top','r':'right','l':'left','b':'bottom'}
  LD_h_spine= {LD_axb1:'tbr',LD_axb2:'tblr',LD_axb3:'tlrb',LD_axt1:'br',LD_axt2:'blr',LD_axt3:'blr',
            LD_axb4:'trb',LD_axb5:'tlrb',LD_axb6:'tlrb',LD_axt4:'brt',LD_axt5:'blrt',LD_axt6:'blrt',
            LD_axb7:'tr',LD_axb8:'tlr',LD_axb9:'tlr',LD_axt7:'brt',LD_axt8:'blrt',LD_axt9:'bltr'}
  LD_ML0x1,LD_ML0y1,LD_ML0x2,LD_ML0y2= np.loadtxt('nb_densities.txt',delimiter='\t', unpack=True)
  LD_ML1x1,LD_ML1y1,LD_ML1x2,LD_ML1y2= np.loadtxt('ph_densities.txt',delimiter='\t', unpack=True)
  LD_ML2x1,LD_ML2y1,LD_ML2x2,LD_ML2y2= np.loadtxt('phph_densities.txt',delimiter='\t', unpack=True)
  for ax in all_RTA_ax:
    # Set inversion
    if RTA_ax_inv_bool[ax]: 
      ax.set_xscale('oneoverx')
      #ax.invert_xaxis()
    else: pass
    # Hide spines
    for l in RTA_h_spine[ax]:
      ax.spines[spine_dict[l]].set_visible(False)
    # Set limits
    
    ax.set_xlim(RTA_ax_xlims[ax][0],RTA_ax_xlims[ax][1])
    if RTA_ax_inv_bool[ax]: 
      ax.invert_xaxis()
    if type(RTA_ax_ylims[ax]) is tuple:
      ax.set_ylim(RTA_ax_ylims[ax][0],RTA_ax_ylims[ax][1])
      ax.hlines(0,RTA_ax_xlims[ax][0],RTA_ax_xlims[ax][1],linestyles='dotted')
    else:pass
    if RTA_y_bool[ax]: 
      ax.tick_params(axis='y', which='major', labelleft=True, left=True,labelsize=7)
      #ax.set_yticks((-0.01,0,0.02),minor=False)
      ax.set_yticklabels([' ',' 0',' '])
    elif not RTA_y_bool[ax]:
      ax.tick_params(axis='y', which='major', labelleft=False, left=False)
    
    if ax in RTA_ax_matick.keys():
      if type(RTA_ax_matick[ax]) is tuple:
        ax.set_xticks(list(range(RTA_ax_matick[ax][0],RTA_ax_matick[ax][1],RTA_ax_matick[ax][2])),minor=False)
        ax.set_xticks(list(range(RTA_ax_mitick[ax][0],RTA_ax_mitick[ax][1],RTA_ax_mitick[ax][2])),minor=True)
      if type(RTA_ax_matick[ax]) is not tuple:
        ax.tick_params(axis='x',which='major', labelbottom=False,labeltop=False,top=False,bottom=False)
        ax.tick_params(axis='x',which='minor', labelbottom=False,labeltop=False,top=False,bottom=False)
    # Give tick locations
    ax.tick_params(axis='x', which='minor',labelbottom=False)
    
    if RTA_bx_bool[ax]:
      ax.tick_params(axis='x',which='major', labelbottom=True,labelsize=6)
    #if ax_inv_bool[ax]:
    #  ax.invert_xaxis()
    if RTA_tx_bool[ax]:
      ax.tick_params(axis='x', which='minor', top=True)
      ax.tick_params(axis='x',which='major',top=True, labeltop=True,labelsize=6)
    
    print('cycle')
  for ax in all_LD_ax:
    # Set inversion
    if LD_ax_inv_bool[ax]: 
      ax.set_xscale('oneoverx')
      #ax.invert_xaxis()
    else: pass
    # Hide spines
    for l in LD_h_spine[ax]:
      ax.spines[spine_dict[l]].set_visible(False)
    # Set limits
    
    ax.set_xlim(LD_ax_xlims[ax][0],LD_ax_xlims[ax][1])
    if LD_ax_inv_bool[ax]: 
      ax.invert_xaxis()
    if type(LD_ax_ylims[ax]) is tuple:
      ax.set_ylim(LD_ax_ylims[ax][0],LD_ax_ylims[ax][1])
      ax.hlines(0,LD_ax_xlims[ax][0],LD_ax_xlims[ax][1],linestyles='dotted')
    else:pass
    if LD_y_bool[ax]: 
      ax.tick_params(axis='y', which='major', labelleft=True, left=True,labelsize=7)
      ax.set_yticks((-0.01,0,0.02),minor=False)
      ax.set_yticklabels([' ',' 0',' '])
    elif not LD_y_bool[ax]:
      ax.tick_params(axis='y', which='major', labelleft=False, left=False)
    #
    if type(LD_ax_matick[ax]) is tuple:
      ax.set_xticks(list(range(LD_ax_matick[ax][0],LD_ax_matick[ax][1],LD_ax_matick[ax][2])),minor=False)
      ax.set_xticks(list(range(LD_ax_mitick[ax][0],LD_ax_mitick[ax][1],LD_ax_mitick[ax][2])),minor=True)
    if type(LD_ax_matick[ax]) is not tuple:
      ax.tick_params(axis='x',which='major', labelbottom=False,labeltop=False,top=False,bottom=False)
      ax.tick_params(axis='x',which='minor', labelbottom=False,labeltop=False,top=False,bottom=False)
    # Give tick locations
    ax.tick_params(axis='x', which='minor',labelbottom=False)
    
    if LD_bx_bool[ax]:
      ax.tick_params(axis='x',which='major', labelbottom=True,labelsize=6)
    #if ax_inv_bool[ax]:
    #  ax.invert_xaxis()
    if LD_tx_bool[ax]:
      ax.tick_params(axis='x', which='minor', top=True)
      ax.tick_params(axis='x',which='major',top=True, labeltop=True,labelsize=6)
  ML0_LD_labels = ['1.006±0.06 ps','140.3±   20 ps']
  ML1_LD_labels = ['1.347±0.04 ps','   628±   44 ps']
  ML2_LD_labels = ['1.484±0.04 ps','1,019±   51 ps']
  for ax in (LD_axb1,LD_axb2,LD_axb3):
    ax.plot(LD_ML0x1,LD_ML0y1,lw=0.75,label=ML0_LD_labels[0])
    ax.plot(LD_ML0x1,LD_ML0y2,lw=0.75,label=ML0_LD_labels[1])
  for ax in (LD_axb4,LD_axb5,LD_axb6):
    ax.plot(LD_ML1x1,LD_ML1y1,lw=0.75,label=ML1_LD_labels[0])
    ax.plot(LD_ML1x1,LD_ML1y2,lw=0.75,label=ML1_LD_labels[1])
  for ax in (LD_axb7,LD_axb8,LD_axb9):
    ax.plot(LD_ML2x1,LD_ML2y1,lw=0.75,label=ML2_LD_labels[0])
    ax.plot(LD_ML2x1,LD_ML2y2,lw=0.75,label=ML2_LD_labels[1])
  LD_axb8.legend(fontsize=6,ncol=1,frameon=False,handlelength=0.5,handleheight=0.15)
  LD_axb5.legend(fontsize=6,ncol=1,frameon=False,handlelength=0.5,handleheight=0.15)
  LD_axb2.legend(fontsize=6,ncol=1,frameon=False,handlelength=0.5,handleheight=0.15)
  #RTA_ML0_yvals = [RTA_ML0y1,RTA_ML0y2,RTA_ML0y3,RTA_ML0y4,RTA_ML0y5,RTA_ML0y6,RTA_ML0y7]
  RTA_ML0_yvals = [RTA_ML0y1,RTA_ML0y2,RTA_ML0y3,RTA_ML0y5,RTA_ML0y6,RTA_ML0y7]
  #RTA_ML0_labels = ['152fs','585fs','1.54ps','2.24ps','7.78ps','116ps',	'669ps']
  RTA_ML0_labels = ['152fs','585fs','1.54ps','7.78ps','116ps',	'669ps']
  RTA_ML1_yvals = [RTA_ML1y1,RTA_ML1y2,RTA_ML1y3,RTA_ML1y4,RTA_ML1y5]
  #RTA_ML1_labels=['284fs','965fs','2.87ps','308ps','1.55ns']
  RTA_ML1_labels=['284fs','965fs','2.87ps','308ps','1.55ns']
  RTA_ML2_yvals = [RTA_ML2y1,RTA_ML2y2,RTA_ML2y3,RTA_ML2y5,RTA_ML2y6,RTA_ML2y7]
  #RTA_ML2_yvals = [RTA_ML2y1,RTA_ML2y2,RTA_ML2y3,RTA_ML2y4,RTA_ML2y5,RTA_ML2y6,RTA_ML2y7]
  RTA_ML2_labels=['343fs','626fs',	'1.08ps',	'116ps',	'906ps','2.25ns']
  #RTA_ML2_labels=['343fs','626fs',	'1.08ps',	'3.11ps',	'116ps',	'906ps','2.25ns']
  RTA_ML0_LTyvalsNIR = [RTA_ML0lty1,RTA_ML0lty2]
  RTA_ML0_LTyvalsVIS = [RTA_ML0lty3,RTA_ML0lty4,RTA_ML0lty5]
  RTA_ML1_LTyvalsNIR = [RTA_ML1lty1,RTA_ML1lty2]
  RTA_ML1_LTyvalsVIS = [RTA_ML1lty3,RTA_ML1lty4,RTA_ML1lty5]
  RTA_ML2_LTyvalsNIR = [RTA_ML2lty1,RTA_ML2lty2]
  RTA_ML2_LTyvalsVIS = [RTA_ML2lty3,RTA_ML2lty4,RTA_ML2lty5]
  RTA_axlt1.set_xticks([0.1,1,10,100,1000],minor=False)
  RTA_axlt1.set_xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]+list(range(1,10,1))+list(range(10,100,10))+list(range(100,1000,100)),minor=True)
  RTA_axlt1.tick_params(axis='x',which='both',bottom=True,direction='inout')
  RTA_axlt2.set_xticks([0.1,1,10,100,1000],minor=False)
  RTA_axlt2.set_xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]+list(range(1,10,1))+list(range(10,100,10))+list(range(100,1000,100)),minor=True)
  RTA_axlt2.tick_params(axis='x',which='both',bottom=True,direction='inout')
  RTA_axlt3.set_xticks([0.1,1,10,100,1000],minor=False)
  RTA_axlt3.set_xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]+list(range(1,10,1))+list(range(10,100,10))+list(range(100,1000,100)),minor=True)
  RTA_axlt3.tick_params(axis='x',which='both',bottom=True,direction='in')
  RTA_axlt3.tick_params(axis='x',which='major',labelbottom=True,labelsize=6)
  RTA_axlt3.set_xticklabels(['','1 ps','','','1 ns'],minor=False)
  print([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]+list(range(1,10,1))+list(range(10,100,10))+list(range(100,1000,100)))
  for ax in (RTA_axb1,RTA_axb2,RTA_axb3):
    for i,vals in enumerate(RTA_ML0_yvals):
      ax.plot(RTA_ML0x1,vals,colorwheel[i],lw=0.5,label=RTA_ML0_labels[i])
      
  for ax in (RTA_axb4,RTA_axb5,RTA_axb6):
    for i,vals in enumerate(RTA_ML1_yvals):
      ax.plot(RTA_ML1x1,vals,colorwheel[i],lw=0.5,label=RTA_ML1_labels[i])
  for ax in (RTA_axb7,RTA_axb8,RTA_axb9):
    for i,vals in enumerate(RTA_ML2_yvals):
      ax.plot(RTA_ML2x1,vals,colorwheel[i],lw=0.5,label=RTA_ML2_labels[i])
  for i,val in enumerate(RTA_ML0_LTyvalsNIR):
    RTA_axlt1.plot(RTA_ML0ltxNIR, val,lw=0.25 )#'+', markersize=0.5)
  for i,val in enumerate(RTA_ML0_LTyvalsVIS):
    RTA_axlt1.plot(RTA_ML0ltxVIS, val,lw=0.25)# '+', markersize=0.5)
  for i,val in enumerate(RTA_ML0_LTyvalsNIR):
    RTA_axlt2.plot(RTA_ML1ltxNIR, val,lw=0.25 )#'+', markersize=0.5)
  for i,val in enumerate(RTA_ML0_LTyvalsVIS):
    RTA_axlt2.plot(RTA_ML1ltxVIS, val,lw=0.25)# '+', markersize=0.5)  
  for i,val in enumerate(RTA_ML0_LTyvalsNIR):
    RTA_axlt3.plot(RTA_ML2ltxNIR, val,lw=0.25 )#'+', markersize=0.5)
  for i,val in enumerate(RTA_ML0_LTyvalsVIS):
    RTA_axlt3.plot(RTA_ML2ltxVIS, val,lw=0.25)# '+', markersize=0.5)  
  RTA_axb2.legend(fontsize=6,ncol=2,frameon=False,handlelength=0.5,handleheight=0.15,columnspacing=0.25)
  RTA_axb5.legend(fontsize=6,ncol=2,frameon=False,handlelength=0.5,handleheight=0.15,columnspacing=0.25)
  RTA_axb8.legend(fontsize=6,ncol=2,frameon=False,handlelength=0.5,handleheight=0.15,columnspacing=0.25)
  plt.savefig('gloop1.png',dpi=720)