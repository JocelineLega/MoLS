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
<li>Output: Excel file called <tt>weatherfile.xlsx</tt>, placed in the <tt>weather_pathname</tt> directory, containing the
same information as the input file plus an additional column corresponding to predictions for the number of gravid female mosquitoes.</li>
<li>Example: <tt>Run_Model.py</tt> reads <tt>Test_Data.csv</tt> and creates an Excel file called <tt>Test_Data.xlsx</tt> in the
<tt>Weather</tt> directory.
</ul>
