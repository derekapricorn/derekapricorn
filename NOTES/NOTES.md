# Study Notes
***
Use **Ctl+Sft+m** to turn on markdown preview in Atom.
## Algorithms for Interview

### Common Data Structure

#### Heap
Heap is a collection of implementations such as **priorityQueue** in Java and **heapq** in python. They are both min Heap by default. Heap is best used to dynamically find the Min/Max of a set. functions: `heapq.heappush(h, item)`, `heapq.heappoll(h, item)`, `heapq.heapify(list)`. `heap[0]` is the min of the heap.

#### Heap vs. Stack
Objects provide facilities for polymorphism, are passed by reference (or more accurately have references passed by value), and are allocated from the heap. Conversely, primitives are immutable types that are passed by value and are often allocated from the stack.

### Common Templates
#### Single pointer
Shift pointer and check at each index if condition is met.
- strStr

#### Combination/Permutation Template
- Use DFS. Need to review DFS
- Common template: subset

#### Binary Search
When to use:
- when having XXXOOOO situation, and need to find the last index (or the first) that meets a condition.
- when a list can be partitioned by certain characteristics, i.e. slope increases/decreases.
Sometimes need to draw a graph for simply illustrate.




***
## HTML&CSS

### Basic Concepts
- HTML id's should be used sparingly because each element can only have one id and each page can only have one id.
- classes can be used more flexibily - each element can have multiple classes and each class can be used on multiple classes. Use of classes is preferred over that of id's.
- CSS properties to
    - italicize text: `font-style: italic;`
    - underline text: `text-decoration: underline;`
    - uppercase: `text-transform: uppercase;`
    - bold text: `font-weight: bold;`
    - add border: `border-style: dashed;`
    - make cursor pointer on hover: `cursor: pointer;`
    - box shadow: `box-shadow: 10px 10px grey;` (10pxs are horizontal and vertical shadows)
    - font family: `font-family: "arial", "serif"`; The broswer renders in priority from left to right
    - rounded border corners: `border-radius: 5px;`
    - `backgorund-image: url($linkToImage);`
- ways to express color:
    1. `background-color: rgb(255,0,255);`
    2. `background-color: #ff00ff;`
- semantic elements are a lot more informative than just plain _div_
    - `box-sizing: border-box;` contians content, padding and border
    - By default, headers have large fonts and margins, but no padding
    - The width of block elements is as big as the parent element allows. The height of block element take as little height as possible.
    - **inline elements** (such as span, p) are content-based, i.e. can only be as wide as the content inside the box is allowed. Cannot set width and height of inline elements. You can add margin and padding to inline elements but they only push other elements horizontally not vertically. **inline-block** takes on the layout behaviors of an inline element with the sizing behaviors of a block element.
    - _anonymous boxes_ are elements created from tabs, spaces and newlines in HTML.
    - `aside` element represents a side bar
- Positioning
    - **Relative positioning** moves the item to a position relative to where it's supposed to be originally. The neighboring items are not affected.
    - **z-index** resolves the overlapping issue by assigning weights to overlapping items. The one with the highest weight will be visible to user.
    - **document** aka DOM is the whole page, **viewport** aka **window** is the visible part of the DOM.
    - Three types of positioning: ![positioning](positioning.png) Items being absolutely positioned are ignored from the normal flow. Absolute positioning is rarely used and considered the last resort.
    - text alignment:
        - `text-align: center`: align center horizontally
        - `vertical-align: text-top/middle/top`: different alignment options
        - `display: inline-block` creates many possible glitches for alignment. Better not use.
    - **floats**
        - different kind of flow from normal flow
        - floats stack on one another in the order that they appear in HTML
        - Regardless of float: left or float: right, all floats respect each other's space
        - Floated elements stay within their containers width, but not their height.
        - to clear float, define `clearfix:after` at the parent box such that the float effect will be cleared after being used.
    - overflow
        - used when child box is larger than parent box
        - `overflow: visible, scroll, hidden, auto`
- Responsive design
    - device returns **dip** (device independent pixel) instead of hardware pixels.
    -  `<meta name="viewport" content="width=device-width, initial-scale=1">` makes dip# the same as CSS pixel#.
    - to prevent _img/embed/object/video_ elements from overflowing from the container, use `max-width: 100%`;
    - tap target (buttons, nav, a) should be bigger than average figure. Make it `min-width: 48px; min-height:48px;`
    - media query: add a link to reference media attribute: `<link rel="" media="screen and (min-width: 500px)" href="somesheet.css">` or add media type:
    ```
	    @media screen and (min-width: 500px) {
	    	body {
	    	some statement;
	    }
    ```
    Most commonly used criteria are min-width and max-width. Don't use min-device-width because it doesn't allow for resizing.
    - breakpoints are decided based on the content by trial and error.
    - flex containers
        - `display: flex` and `flex-wrap: wrap`







### Figure
A good template to insert a figure is as follows:
```
<!-- Figure with figcaption -->
<figure>
  <img
  src="https://developer.cdn.mozilla.net/media/img/mdn-logo-sm.png"
  alt="An awesome picture">
  <figcaption>MDN Logo</figcaption>
</figure>
<p></p>
```
### Form
- Input types: button, text, radio... More details can be found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
***

## Network Basics

### Terminology
- Packet: network traffic unit, a short message with sender and recipient info.
- port: a server has many ports. Common ones are 22 for SSH, 80 for HTTP. Port _1-1023_ are for local root user who can use `sudo` and _1024-65535_ are for external clients. One port can only be listened by one process at a time using `nc`, but programs can use threads to process multiple ports
- IP address: each computer connected to Internet has a unique IP address. Local host IP address is _127.0.0.1_.
- TCP: transmission control protocol
    - a layer below HTTP
    - It’s like a two-way road
    - only a client can initiate a connection but either ends can drop a connection by using _EOF_
- Layering ![layering](network_layering.png)
### Some useful commands
- `ping -c3 8.8.8.8`. Here we try to get three lines of response from IP address 8.8.8.8 that is a server of Google
- `sudo lsof -i` lists programs that are listening on the network
- `nslookup $webpage` finds out the IP address of a certain website.
- `printf` prints formatted text. Compare with `echo`.
- `nc` stands for netcat. It connects to a port and send a string over
- `|` stands for pipe. `left | right` means take the output of _left_ and feed it into the input of _right_.
- `>` is the shell redirecting operator. `$content > example.txt` will send the output to the text file named _example.txt_.
***
## Python
## Some nice libraries
- webbrowser: interact with web browser using Python
- turtle: draw some patterns on screen
- twilio: send text
- [Python built-in library](https://docs.python.org/2/library/functions.html). Don't have to import any library.
    - open: used to open a text file
- urllib
    - urllib.urlopen(URL): create an object for opening the url
    - url object can read response:
        - obj.read() : this returns a string. Don’t forget to close the connection: obj.close()

## OOP
- `__init__`
    - double underscore means the function is reserved and special for Python always contain self —> the instance being created.
- class variable
    - shared with all the functions of the class. Use all uppercase to define class variable because it is unlikely to change. All built-in classes have `__doc__`, which can be be created by “””content””” at the beginning of the class
    - `__name__`: name of the class
    - `__module__`: name of the module where the class resides.
- Inheritance
    - To define child class:
    ```
    class Child(
        	def class Child(Parent):
        		def __init__(self, parentX, parentY, childX):
        			self.__init__(ParentX, ParentY)
        			self.childX = childX
    ```
    - If the child has conflicting methods with the parent, the child functions override parent methods.

### README.md
A README file usually contains the following parts:
1. project name
2. description
3. optional: links to external documentation
4. install instruction
5. common usage or known bugs
6. Contributions
7. License
***
