
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
    q = GumboQuery("<div class="show">2</div>")
    tag = q.query(".show")
    print tag[0].contents[0]
    # 2 will  print on terminal
    
## Testing Website
http://sports.yahoo.com/nba/utah-jazz-toronto-raptors-2013110928/


## Contact
If you have found a bug or a question, email me at <hamming1@gmail.com>


  [1]: https://github.com/google/gumbo-parser
  [2]: http://www.crummy.com/software/BeautifulSoup/
  [3]: https://pypi.python.org/pypi/pip
