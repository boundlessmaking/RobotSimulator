import math
import numpy as np
class ConfigRobot(object):
	"""docstring for ConfigRobot"""
	def __init__(self):
		super(ConfigRobot, self).__init__()
		self.d=[89.2, -135.7, 130.4, 0]
		self.a=[0, 300, 383, 60.04]
		self.alpha = math.pi/180*np.array([-90, 0, 0, 0])
		self.q_init = math.pi/180*np.array([0, 0, 0, 0])
		
	def get_q_init(self):
		return self.q_init