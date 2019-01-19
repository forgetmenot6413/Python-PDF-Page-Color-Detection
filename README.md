# Python Colored Page Detector for PDFs exported from Google Docs
This tool is a simple python script that uses GhostScript to detect the colored pages exported from Google Docs.

Side Note : My work is based on another project however it's previous state has given me false results on PDF's that is exported from Google Docs

Link to the other project my work based and improved on : http://www.tor.eu/?p=763

## Method
In the script we take CMYK values for each page with GhostScript
As far as I have observed in Google Docs exported PDFs we can see that even the black & white pages have CMYK values different than 0. It's clear that not only 0 is a sign of black & white page only. So we conclude that CMYK values with values higher than 0 in a page doesn't necessarily mean it is colored.

Let's deep dive in to the approach I have used a little bit with two examples for each case

An example for the detection would be

```
C : 0.29866 M : 0.29882 Y : 0.29882 K : 0.30026
```

Judging by the difference of K with other values (CMY) we can conclude that the page has colored items.

```
C : 0.01777 M : 0.01777 Y : 0.01777 K : 0.01777
```

Again when we compare the CMYK values if they are equal to each other like in this case we can conclude that page is compromised of black color.
