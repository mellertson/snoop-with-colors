**Snoop with Color**<BR>
<BR>
This program uses 'tcpdump' and 'grep' to snoop for network traffic
and colorizes its output using command line arguments, specified
by the user.
<BR>
<BR>

**Usage**<BR>
python Application.py <inbound_color_code> <outbound_color_code>

**Example**<BR>
The following example will colorize output from 'tcpdump' wiht outbound
traffic colored red, and inbound traffic colored blue.<BR>
<BR>
```python Application.py 34 31```

<BR>

**Foreground Color Codes** <BR>
The following are just a few color codes to get you started.<BR>
<BR>
In version 1.0, any single color code, supported by the user's terminal,
can be specified as either of the command line arguments

![Image of foreground colors](https://raw.githubusercontent.com/mellertson/snoop_with_colors/master/foreground-colors.png)

<BR>
<BR>
For a full list of foreground, background and other color codes, I highly recommend
[Flozz' MISC >> bash:tip_colors_and_formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting).

