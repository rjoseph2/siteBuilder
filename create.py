import os
import glob
import re
import shutil
class creator :
    root = ""
    template = ""
    location = ""

    content = ""
    tplTowrite = ""
    keys={};
    contentDict={};
    propertyFName = "key.property"
    


    def  __init__(self):
        fileExp = "./*.txt"
        txtFiles = self.readfileList(fileExp)
        print len(txtFiles);
        self.readKeys()
        
        
        
        for sourcetxt in txtFiles:
            #print sourcetxt
            self.processSource(sourcetxt);
            #print self.keys
            self.readTemplateAndApply();
            #print  self.tplTowrite;
            #print self.keys
            #print 'risto'
            self.writeToFileTest(self.tplTowrite);
            #self.tplTowrite=""
            self.fileCopy();


    def readKeys(self):
        propery = open('key.property', 'r')
        for line in propery.readlines():
           self.keys[line.strip()]=''
           if "pattern" in line:
                pattern = line.split(':')
                if(len(pattern) >2):
                    tplkey = pattern[1] + ':' +pattern[2]
                else:
                    tplkey = pattern[1]
                self.keys['pattern'] = tplkey;

    def readfileList(self, fileExp):
        return glob.glob(fileExp)

    def fileCopy(self):
        root = self.root
        files = self.readfileList("./temp*.html")
        
        for f in files:
            pathArray = f.split("_")
            path = ""
            filename =""
            for a in pathArray:
                if "temp" == a:
                    a = ""
                else:
                    path = os.path.join(path, a)
                    if "html" in a:
                        filename = a;
            print path;
            realpath = path.replace("temp", root);
            path = realpath.replace(filename,"")
            if not  os.path.exists(path):
                os.mkdir(path)
            shutil.copyfile(f, realpath)
            


    def writeToFileTest(self,content):
        self.root = self.keys['root']
        tofile = self.keys['tofilename']
        topath = self.keys['tofilepath']
        tmppath = "temp_"

        for to in topath.split("/"):
            tmppath = tmppath + to + "_"

        tmpFileName = tmppath+tofile;
        f = self.readFile(tmpFileName,'w');
        f.write(content);
        f.close();
    
    def readFile(self,filepath,fmode):
        f = open(filepath,fmode) 
        return f;

    def processSource(self,sourcetxt):
        sorceFile = self.readFile(sourcetxt,"r");
        contentStart = False
        readTill = "notttthing"
        contetntName = ""

        for line in sorceFile.readlines():
            
            if readTill  in line:
                contentStart = False
                self.contentDict[contetntName] = self.content
                self.keys[contetntName] = self.content
                self.content = ""
                

            elif True == contentStart and  readTill not in line  :
                self.content = self.content + line;
                

            elif bool(re.search('^#[a-zA-Z1-9]*:',line)) and line.strip() != '' :
                tplkey = line.split(':')[0].replace("\n","") + ":" 
                tplkey = tplkey.replace("#","").replace(":","")
                self.keys[tplkey] = line.split(':')[1].replace("\n","")
                

            elif  "{{content" in line:
                contentStart =True;
                readTill = line.split('-')[0]+"-end"
                #print readTill
                contetntName = line.split('-')[0]
                contetntName = contetntName.replace("{","")
                #val = self.keys[tplkey]  
                #print line 
                #print val
        sorceFile.close();

    def readTemplateAndApply(self):
        self.tplTowrite = ""
        
        mainfolder = self.keys['root']
        templateName = self.keys['template']
        template = self.readFile(os.path.join('.',mainfolder,templateName),"r")

        for line in template.readlines():
            #print line;
            if bool(re.search("{{[a-zA-Z1-9]*}}",line)):
                
                totalTplKeys = line.count("{{")
                pattern = re.compile(r'{{[a-zA-Z1-9]*}}')
                for match in pattern.finditer(line):
                    tplkey = match.group(0);
                    key = tplkey.replace("{", "").replace("}", "")
                    if 'cssfiles' not in tplkey and 'scriptfiles' not in tplkey:
                        line = line.replace(tplkey, self.keys[key])

                    elif 'cssfiles'  in tplkey:
                        cssContent = self.generateCss(self.keys['csspath'], self.keys['cssfiles'])
                        print tplkey
                        line = line.replace(tplkey, cssContent)

                    elif 'scriptfiles'  in tplkey:
                        jsContent = self.generateScript(self.keys['scriptpath'], self.keys['scriptfiles'])
                        line = line.replace(tplkey, jsContent)
                     
                self.tplTowrite = self.tplTowrite + line;
                
               
            else:
                self.tplTowrite = self.tplTowrite + line;

       
    def generateCss(self, csspath, cssfiles):
        css = cssfiles.split(",")
        cssContent =""
        for cs in css:
           cssContent = cssContent +'\n\t <link rel="stylesheet" href="' + os.path.join(csspath, cs)+'" media="screen">'
        return cssContent

    def generateScript(self,scriptPath, scriptFiles):
        scripts = scriptFiles.split(",")
        scriptsContent =""
        for script in scripts:
           scriptsContent = scriptsContent +'\n\t <script src="' + os.path.join(scriptPath, script)+'"></script>'
        return scriptsContent      

    def printGlobal(self):
        print self.root
        print self.template
        print self.location

        print self.title
        print self.metadecription
        print self.meta

        print self.csspath
        print self.css
        print self.jspath

        print self.script
        print self.mainMenu
        print self.siteMenu

        print "/////////////////////"

creat = creator();