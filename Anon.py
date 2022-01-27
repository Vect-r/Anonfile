import os
import requests as req
import json as jsn
import collections


#Author: Mitesh Vaid
#Developed in Python 3.9.6
#Version: 0.1 Stable 
#Currently in BETA

"""
Created on Wed Jan 26 16:07:18 2022

@author: Mitesh
"""

"""
Decription: AnonFile Python API for Uploading files to the server and Getting Status Response Code & Verify IDs 
"""

class AnonFile:
    def __init__(self):
        self.Error_CODES={
            10:"ERROR_FILE_NOT_PROVIDED",
            11:"ERROR_FILE_EMPTY",
            12:"ERROR_FILE_INVALID",
            20:"ERROR_USER_MAX_FILES_PER_HOUR_REACHED",
            21:"ERROR_USER_MAX_FILES_PER_DAY_REACHED",
            22:"ERROR_USER_MAX_BYTES_PER_HOUR_REACHED",
            23:"ERROR_USER_MAX_BYTES_PER_DAY_REACHED",
            30:"ERROR_FILE_DISALLOWED_TYPE",
            31:"ERROR_FILE_SIZE_EXCEEDED",
            32:"ERROR_FILE_BANNED",
            40:"STATUS_ERROR_SYSTEM_FAILURE"
        }
        #Url for sending file through POST request
        self.POSTurl="https://api.anonfiles.com/upload"
        #fetching info about file exist or not through their UIDs
        self.GETurl="https://api.anonfiles.com/v2/file/id/info"
        
    @property
    def SendResp(self):
        try:
            return {a.replace('data_',''):b for a,b in self.__flat(self.__SendJSON).items()}
        except:
            raise NameError("Plz First Execute Send function")
            
    @property
    def SendStatus(self):
        try:
            return self.SendResp['status']
        except:
            raise NameError("Plz First Execute Send function")
        
    @property
    def SendRespCode(self):
        try:
            return self.__POST.status_code
        except:
            raise NameError("Plz First Execute Send function.")
            
    @property
    def InfoResp(self):
        try:
            return {a.replace('data_',''):b for a,b in self.__flat(self.__GETJSON).items()}
        except:
            raise NameError("Plz First Execute Info function.")
    
    @property
    def InfoIDExists(self):
        try:
            return self.__GETJSON['status']
        except:
            raise NameError("Plz First Execute Info function.")
    
    def __flat(self,d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(self.__flat(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
            
    def Send(self,file):
        if os.path.exists(file)==True:
            self.File=file
            files={'file':open(self.File,'rb')}
            self.__POST=req.post(self.POSTurl,files=files)
            self.__SendJSON=jsn.loads(self.__POST.content)
            return self.SendResp
        else:
            raise FileNotFoundError('Invalid File Path')
            
    def SaveRespJSON(self,fname):
        if fname.endswith('.json')==False and type(fname)==str:
            fname=fname+'.json'
            with open(fname,'w') as jsnfile:
                jsn.dump(self.SendResp,jsnfile,indent=4)
            jsnfile.close()
        else:
            raise TypeError('fname must must be str.')  
        
    
    def SaveRespTxt(self,fname):
        with open(fname,'w') as txtfile:
            for a,b in self.SendResp.items():
                txtfile.write(f"{a} : {b}\n")
        txtfile.close()
    
    def InfoID(self,id):
        if type(id)!=str:
            raise TypeError('must be str')
        else:
            self.ID=id
            self.__GET=req.get(self.GETurl.replace('id',id))
            self.__GETJSON=jsn.loads(self.__GET.content)
            return self.InfoResp