<h1>Mosquito Landscape Simulation</h1>

This suite of codes predicts <i>Ae. aegypti</i> abundance in a given location, using time series for temperature, precipitation, and
relative humidity as input. It is provided here as a Python library.
<ul><li>Main program: MoLS<br />
Arguments:
<ol><li><tt>weather_pathname</tt> (string): directory where input file is located</li>
<li><tt>weatherfile</tt> (string): name of weather data file in csv format, without the .csv extension</li></ol></li>
<li>Format of input file (<tt>weatherfile.csv</tt>): <br />
9 columns showing (1) year; (2) month; (3) day; (4) maximum temperature; (5) minimum temperature; (6) precipitation in mm; (7)
average temperature; (8) precipitation in cm; (9) relative humidity.<br />
Note: only columns 7-9 are used.<br />
Template: see example in <tt>Weather</tt> subdirectory</li>
<li>Output: overwrites <tt>weatherfile.csv</tt>; removes the header and adds a 10th column corresponding to predictions for the number of gravid female mosquitoes.</li>
<li>Example: <tt>Run_Model_v2.py</tt> reads <tt>Test_Data_IO.csv</tt> in the <tt>Weather</tt> directory and replaces it with the same information, without the header and with an additional 10th column for the predicted number of gravid females.
</ul>
