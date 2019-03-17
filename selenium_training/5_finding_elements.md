## Understanding DOM and elements
Document object Model

## Finding Elements
###Finding element by ID and Name

find_element_by_id()
find_element_by_name()
find_element_by_xpath()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_tag_name()
find_element_by_class_name()
find_element_by_css_selector()

We have find_elements_by_AAA() => this return a list of elements

find_element(By.XPATH, "xpath expression")
find_elements(By.XPATH, "xpath expression")
Attributes available for "By"
- ID = "id"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- NAME = "name"
- TAG_NAME = "tag name"
-CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"

1. Point to an element and inspect element. The element will contain an attribute "id".
2. Check if that id is unique acrosst the DOM.

element = driver.find_element_by_id()


## Static and dynamic elements:

Static elemenets are those whose attributes do not change across each refresh, but the attributes of the dynamic elements changes across refresh

 url = https://www.yahoo.com/
For Notifiactions feature, id=yui_3_18_0_3_1552823247290_1052
After refresh id = yui_3_18_0_3_1552823446350_814


## find_element methods
## Find the list of elements

##Finding elements by CSS selector:
tag[attribute="value"]

id & class
# -> id
. -> class

id based CSS selector - for input text box
input[id='name']
#name
input#name

Class based CSS Selector  => for input text box
input[class='display']
.display
input.display

Appending classes
.class1.class2.class3

class = "display first_choice inline0-style"

.display.first_choice,inline0-style

