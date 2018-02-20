# langton-ants
a modified implementation of Langton's Ants Model

USAGE: no arguments necessary, just run 'python langAnt.py'

Adaptations to note:
	-Wraparound: rather than clipping, this model can be thought of as a globe, since the map wraps around in all directions 
	-Dual Breed Ants: A certain proportion of ants will be 'true' Langton's Ants, and the rest will be inversed Langton's Ants
		-'true' ants appear red, and turn left on white and right on black
		-'inverse' ants appear blue, and turn right on white and left on black

There are several variables that can be modified in langAnt.py to toggle the model:
	(these are all located near the top of the file, followed by a "toggle value" comment)
	
	-width: width of environment (gets slow over 100, but is still functional if you're patient!)
	-height: height of environment (ditto above)
	-populationSize: number of ants (ditto above)
	-proportionTrueLangtons: the proportion of ants which are 'true' Langton's Ants (should be in range [0,1])
	 
