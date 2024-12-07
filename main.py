from manim import *
from manim import rate_functions
import numpy as np

class DrawHeart(Scene):
	def construct(self):
		# Setup axes
		axes = Axes(
			x_range = [-np.sqrt(3), np.sqrt(3)],
			y_range = [-2, 2],
			axis_config = {"include_numbers": False},
		)
		
		# Setup k value, this will increase to draw the heart
		k_value = ValueTracker(0)
		K_VALUE_MAX = 100

		# Tell manim to always redraw the function as the k_value increases
		heart = always_redraw(
			lambda: FunctionGraph(
				lambda x: self.heart_function(x, k_value.get_value()),
				x_range = [-np.sqrt(3), np.sqrt(3)], # DO NOT CHANGE
				color = RED
			)
		)

		# Draw the axes and the initial graph when k = 0
		self.play(Write(axes))
		self.play(Write(heart))

		# For 10 seconds, increase k to 100
		self.play(
			k_value.animate.set_value(100),
			run_time = 6,
			rate_func = rate_functions.ease_in_out_sine	
		)


	def heart_function(self, x, k):
		"""
		Important note:
		- The function only returns a real number when |x| <= sqrt(3) and the input range
		    is assumed to be between the range, if outside, nan will be returned
		"""
		return np.cbrt(np.square(x)) + 0.9 * np.sin(k * x) * np.sqrt(3 - np.square(x))