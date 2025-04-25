import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from matplotlib import colormaps
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches



potentials = ["GAP","linearACE","MACE","MTP-26","nonlinearACE","NNP"]
labels     = ["GAP","linear ACE","MACE","MTP","nonlinear ACE","HDNNP"]

colors     = ["#e9162d","#8f2be7","#fb4fd9","#007bd8","#00e1da","#f28200",]#"#8f2be7""#007bd8"
linestyle  = ["--","-.",":","-","--","-.",":","-"]
structures  = ["coesite.dat","cristobalite.dat","moganite.dat","quartz.dat","stishovite.dat","tridymite.dat"]
cryst       = ["coesite",r"$\alpha$-cristobalite","moganite",r"$\alpha$-quartz","stishovite","monoclinic tridymite"]
num_atoms   = [48, 12, 36, 9, 6, 144]

ref_energy = np.min(np.loadtxt("dft_ref/quartz.dat")[:,0])/3

print(ref_energy)

fig, axs = plt.subplots(2,3,figsize=(17*cm,18*cm),sharex=True,sharey=True)

for i in range(0,len(potentials)):
	count=0
	
	axins = axs[i%2,i%3].inset_axes([0.4,0.35,0.55,0.62],xlim=(30,50),ylim=(-10,60))
	
	for s in structures:
		dataPOT = np.loadtxt(potentials[i]+"/"+s)
		dataDFT = np.loadtxt("dft_ref/"+s)
		
		axs[i%2,i%3].plot(dataPOT[:,0],dataPOT[:,1]*1000,color=colors[count],label=cryst[count])
		axs[i%2,i%3].scatter(dataDFT[:,1]/(num_atoms[count]/3),(dataDFT[:,0]/(num_atoms[count]/3)-ref_energy)*1000,edgecolor=colors[count],s=10,facecolor="None")
		
		axs[i%2,i%3].set_xlim(20,50)
		axs[i%2,i%3].set_ylim(-50,700)
		
		axins.plot(dataPOT[:,0],dataPOT[:,1]*1000,color=colors[count])
		axins.scatter(dataDFT[:,1]/(num_atoms[count]/3),(dataDFT[:,0]/(num_atoms[count]/3)-ref_energy)*1000,edgecolor=colors[count],s=5,facecolor="None")

		count+=1

	axs[i%2,i%3].set_title(labels[i])
	if i%2==1:
		axs[i%2,i%3].set_xlabel(r"Volume ($\AA^3$/SiO$_2$)")
	if i%3==0:
		axs[i%2,i%3].set_ylabel(r"$\Delta$E (meV/SiO$_2$)")
	
axs[1,1].legend(loc="upper center",bbox_to_anchor=(0.5,-0.12),ncol=3,frameon=False)

plt.subplots_adjust(bottom=0.11,top=0.97,right=0.99,left=0.08,hspace=0.1,wspace=0.07)
plt.savefig("SiO_energy_volume.png",dpi=600)
