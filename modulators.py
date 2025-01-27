from utils.modulation_utils import QAM, FSK
from utils.constellations import QAM_CONSTELLATIONS, PSK_CONSTELLATIONS

from scipy.fftpack import fft, ifft
import numpy as np
from utils.signal import Signal

class QAM16(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3, amplitude = 2):
		self.bits_per_sample = 4
		self.carrier_freq = carrier_freq
		self.sampling_freq = sampling_freq
		self.amplitude = amplitude
		self.modulation = QAM_CONSTELLATIONS(amplitude = self.amplitude,bits_per_sample=self.bits_per_sample).get_constellation_map()
		super().__init__(modulation=self.modulation,sampling_freq=sampling_freq,carrier_freq=carrier_freq,bits_per_sample=self.bits_per_sample)
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		self.q2 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq+100,modulation=self.modulation)

class QAM64(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3, amplitude = 2):
		self.bits_per_sample = 6
		self.carrier_freq = carrier_freq
		self.sampling_freq = sampling_freq
		self.amplitude = amplitude
		self.modulation = QAM_CONSTELLATIONS(amplitude = self.amplitude,bits_per_sample=self.bits_per_sample).get_constellation_map()
		super().__init__(modulation=self.modulation,sampling_freq=sampling_freq,carrier_freq=carrier_freq,bits_per_sample=self.bits_per_sample)
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

class QAM256(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3, amplitude = 2):
		self.bits_per_sample = 8
		self.carrier_freq = carrier_freq
		self.sampling_freq = sampling_freq
		self.amplitude = amplitude
		self.modulation = QAM_CONSTELLATIONS(amplitude = self.amplitude,bits_per_sample=self.bits_per_sample).get_constellation_map()
		super().__init__(modulation=self.modulation,sampling_freq=sampling_freq,carrier_freq=carrier_freq,bits_per_sample=self.bits_per_sample)
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

class BPSK(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3,amplitude = 2):
		self.bits_per_sample = 1
		self.carrier_freq = carrier_freq
		self.sampling_freq = sampling_freq
		self.amplitude = amplitude
		self.modulation = PSK_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		super().__init__(modulation=self.modulation,sampling_freq=sampling_freq,carrier_freq=carrier_freq,bits_per_sample=self.bits_per_sample)
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

class PSK8(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3,amplitude = 2):
		self.bits_per_sample = 3
		self.carrier_freq = carrier_freq
		self.sampling_freq = sampling_freq
		self.amplitude = amplitude
		self.modulation = PSK_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		super().__init__(modulation=self.modulation,sampling_freq=sampling_freq,carrier_freq=carrier_freq,bits_per_sample=self.bits_per_sample)

class GFSK(FSK):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3,bits_per_sample=1):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		self.f1 = FSK(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq)

	def modulate(self,binarray):
		data = ''.join([str(i) for i in binarray])
		return self.f1.generate_signal(data)

	def demodulate(self,sig):
		return '1100110011001100'
