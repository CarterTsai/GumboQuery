
GumboQuery
------------
GumboPlus is an implementation of python of Gumbo to provide rich operate interface.

## Requirements
* [Gumbo-parser][1]
* [BeautifulSoup 3.2.1][2]
* Python 2.7
* [pip 1.2.1][3]

## Install Gubmo

    1. git clone https://github.com/google/gumbo-parser.git      
    2. ./autogen.sh 
    3. ./configure      
    4. make 
    5. sudo make install    
    
## To install the python bindings 
    
    1. sudo python setup.py install
    2. sudo pip install BeautifulSoup
    
## Example

    from lib.GetElement import GumboQuery
    q = GumboQuery('<div><a>123</a><div class="gg">gg</div><div id="dd">dd</div></div>')
    
    You can do 
    q.query('div') // query element
    q.query('.gg') // query class
    q.query('#dd') // query id
    
    // set url to parse 
    q.setUrl("http://www.google.com")
    // set Html source 
    q.setHtml("<div><h1>333</h1></div>")


## Testing Website
http://sports.yahoo.com/nba/utah-jazz-toronto-raptors-2013110928/


## Contact
If you have found a bug or a question, email me at <hamming1@gmail.com>


  [1]: https://github.com/google/gumbo-parser
  [2]: http://www.crummy.com/software/BeautifulSoup/
  [3]: https://pypi.python.org/pypi/pip
