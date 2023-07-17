import json
import os

class JS_PY:
    '''
    Class for running javascript code from python
    '''

    def __init__(self, filename):
        self.tmp_file_data = ""
        with open(filename) as f:
            self.tmp_file_data = f.read()
        
        self.tmp_filename = '.' + filename.split('.')[0] + "_tmp.js"

        # extra code for running js from python
        self.extra_js_code = '''

/////////////////// EXTRA CODE FOR CONVERTING //////////////////

const fs = require('fs');
// const json = require('json');

try {fs.writeFileSync( __dirname + '/.output.txt' , ans );}
catch {fs.writeFileSync( __dirname + "/.output.txt", "");}

var ans = <<$funcname;

try {fs.writeFileSync( __dirname + '/.output.txt' , JSON.stringify({'ans': ans}) );}
catch {fs.writeFileSync( __dirname + "/.output.txt", "Error");}

// remove file
fs.unlinkSync(__dirname + '/<<$filename');

'''

    def run(self, funcname : str , args : list =[]):
        '''
        This function is used to run the javascript function

        * funcname: name of the function to be called
        * args: list of arguments to be passed to the function
        '''

        # creating input arguments
        input_arg = ""
        for arg in args:
            if (type(arg) == 'dict'):
                input_arg += json.dumps(arg) + ","
            else :
                input_arg += str(arg) + ","

        # creating temporary file data
        content = self.extra_js_code
        content = content.split("<<$")
        content[1] = funcname + '(' + input_arg + ')' + content[1][len('funcname'):]
        content[2] = self.tmp_filename + content[2][len('filename'):]
        content = content[0]+content[1]+content[2]
        
        # creating the temporary file
        with open(self.tmp_filename, 'w') as f2:
            f2.write(self.tmp_file_data + content)
        
        # running the program
        os.system('node ' + self.tmp_filename)

        # reading the output
        ret_val = None
        with open('.output.txt', 'r') as f:
            data = f.read()
            if data == '':
                ret_val = ""
            elif data == 'Error':
                ret_val = data
            else:
                ret_val = json.loads(data)['ans']
            
        # removing the output file
        os.remove('.output.txt')

        return ret_val