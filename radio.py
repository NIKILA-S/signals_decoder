from utils.data_utils import dataUtils
from utils.signal import Signal
from utils.graph_utils import graphUtils, graphData
from utils.file_utils import fileUtils
from modulators import *

class Radio(QAM,dataUtils,graphUtils,graphData,fileUtils):
	def __init__(self,bits_per_sample=1,sampling_freq=10,carrier_freq=50):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		super().__init__(sampling_freq=sampling_freq,bits_per_sample=bits_per_sample,carrier_freq=carrier_freq)
		self.QAM16 = QAM16
		self.QAM64 = QAM64
		self.QAM256 = QAM256
		self.BPSK = BPSK
		self.PSK8 = PSK8
		self.GFSK = GFSK

	def get_sig_from_file(self,filetype,filepath,channel=None):
		sampling_freq = self.sampling_freq
		duration = 1
		sigarray = []
		if filetype == 'wav':
			sampling_freq, duration, sigarray = self.read_from_wav(filepath,channel)
		elif filetype == 'iq':
			sampling_freq, duration, sigarray = self.read_from_iq(filepath)
		s = Signal(total_time=duration,sampling_freq=sampling_freq)
		s.signal = sigarray
		return s

	def save_sig_to_file(self,filetype,filepath,sig):
		if filetype == 'wav':
			self.save_to_wav(sig,filepath)
		elif filetype == 'iq':
			signal = sig.signal
			duration = sig.total_time
			sampling_freq = sig.sampling_freq
			self.save_to_iq(signal,sampling_freq,duration,filepath)

if __name__ == '__main__':
	#DEBUGGING
	r = Radio()
	d = dataUtils()
	data = d.str_to_binarray('hello there, general kenobi')
	#data = [0,0,1,1,0,1,0,1]
	qam16 = r.QAM16(sampling_freq=10,carrier_freq=20)
	s = qam16.modulate(data)
	#r.save_sig_to_file('wav','mod.wav',s)
	#s = r.get_sig_from_file('wav','mod.wav',channel='left')
	print(d.binarray_to_string(qam16.demodulate(s)))
	graphUtils().plot_constellation([qam16.get_sig_constellation(s),qam16.get_constellations()],mods=True)
	s.amplify(1.5,'baseband')
	x, y1, y2, y3 = s.get_time_domain()
	g1 = graphData(x,y1,'time','amplitude')
	#x, a, p = s.get_frequency_domain()
	g2 = graphData(x,y2,'freq','amplitude')
	g3 = graphData(x,y3,'freq','phase')
	graphUtils.plot_wave([g1,g2,g3])
