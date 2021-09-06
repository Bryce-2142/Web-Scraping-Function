# Written by David Johnson, University of Utah. This code or derived code
# cannot be publicly distributed without permission.

import urllib.request
import time
import datetime

# Look in text for a string between start_marker and end_marker.
# Will return the location of where start_marker begins in the string
# and the location of where the end_marker begins. Will give a value
# of -1 for either start or end when that marker is not found.
def find_text_between_markers(text, start_marker, end_marker):
    start_location = text.find(start_marker)
    end_location = text.find(end_marker, start_location)
    return (start_location, end_location)
    
# Opens the web page and returns the html as a string.
def get_html_page(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

# Finds all the text between the start and end markers.
# Returns a list of each occurrence.
def find_marked_text(text, start_marker, end_marker):
    found_text = []
    start = 0
    end = 0
    while start != -1 and end != -1:
        (start, end) = find_text_between_markers(text, start_marker, end_marker)
        if start != -1 and end != -1:
            phrase = text[start+len(start_marker):end]
            found_text.append(phrase)
            text = text[end+len(end_marker):]
    return found_text

# This main function drives the overall program. It opens a page and
# searches for paragraph markers.
def main():
    temperatures = []
    times = []
    for item in range(0,10):
        from datetime import datetime
        str(datetime.now())
        
    
    # Set the page to examine
        url = "http://forecast.weather.gov/MapClick.php?lat=40.76031000000006&lon=-111.88821999999999#.WelF6mhSxPZ"
    # Get the html text for that page
        html = get_html_page(url)
    # Find all text between the start and end marker
        
        found_text = find_marked_text(html, '<p class="myforecast-current-lrg">','&deg;F</p>')
        times.append(datetime.now())
        temp = found_text[0]
        temperatures.append(temp)
        print(temperatures)
        time.sleep(1200)
        #30 minutes is 1800, but for times sake i used 1200 for 20 minutes
        
      
    with open ("temperatures.csv","w") as f:
            f.write("Temperatures,Times \n")
            for item in range(0,10):
                f.write(str(temperatures[item]) + "," + str(times[item]) + '\n')
          
         #https://plot.ly/~bryce20202/1/   
main()
