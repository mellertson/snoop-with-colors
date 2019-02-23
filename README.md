**Snoop with Color**<BR>
<BR>
This program uses ```tcpdump``` to snoop for network traffic
and colorizes its output using ```grep``` and user provided
color codes on the command line.
<BR>

**Usage**<BR>
```python Application.py <inbound_color_code> <outbound_color_code>```

**Example**<BR>
The following example will colorize output from 'tcpdump' with outbound
traffic colored red, and inbound traffic colored blue.<BR>
<BR>
```python Application.py 34 31```

This example produces the following output.<BR>
![Image of example output](https://user-images.githubusercontent.com/1175253/53277755-d1a02700-36c2-11e9-94bf-1b6f42f02fb0.png)


**Foreground Color Codes** <BR>
The following are just a few color codes to get you started.<BR>
<BR>
In version 1.0, any single color code, supported by the user's terminal,
can be specified as either of the command line arguments

![Image of foreground colors](https://user-images.githubusercontent.com/1175253/53277761-e086d980-36c2-11e9-9307-5762c73e7800.png)

<BR>

**Note:** For a full list of foreground, background and other color codes, I highly recommend
[Flozz' MISC >> bash:tip_colors_and_formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting).

<BR> 

**Dependencies**

- Python 2.7

