**Snoop with Color**<BR>
<BR>
This program uses 'tcpdump' and 'grep' to snoop for network traffic
and colorizes its output using command line arguments, specified
by the user.
<BR>
<BR>

**Usage:**<BR>
python Application.py <inbound_color_code> <outbound_color_code>

**Example:**<BR>
The following example will colorize output from 'tcpdump' wiht outbound
traffic colored red, and inbound traffic colored blue.
python Application.py 34 31

In version 1.0, any single color code, supported by the user's terminal,
can be specified as either of the command line arguments.

**Color Codes**<BR>
To make your life a little easier, I've includes some of the more common
color codes here. For a full list I highly recommend
[Flozz' MISC >> bash:tip_colors_and_formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting).
<BR>
<BR>
**Foreground Color Codes** <BR>
The following are just a few color codes to get your started.


<p>30<span style="color:black"> will output a line using black text</span></p>
<p>31<span style="color:red"> will output a line using red text</span></p>
<p>32<span style="color:green"> will output a line using green text</span></p>
<p>33<span style="color:yellow"> will output a line using green text</span></p>
<p>34<span style="color:blue"> will output a line using green text</span></p>
