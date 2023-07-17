# OtherLangs2py
This is python module which is used to run functions from other languages from python.

### Current Supported Languages
- JavaScript
  
        ```
        from others2py import js_py

        coderunner = js_py.JS_PY(<filename>)
        output = coderunner.run(<function_name>, <args>)
        ```
        ```