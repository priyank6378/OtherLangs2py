# OtherLangs2py
This is python package which is used to run functions defined in other languages using python.  

### Current Supported Languages
- JavaScript
  
```
from others2py import js_py

coderunner = js_py.JS_PY(<filename>)
output = coderunner.run(<function_name>, <args>)
```
