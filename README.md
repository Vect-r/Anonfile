# AnonFile
## Description 
#### Anonfile Python is an API Built on Python3 for Uploading file on the site Anonfile.com and getting info about the file id currently exists or not.
#### 

## Status 
#### Currently this API is still in BETA Version

## How to Use 

#### Import 
`from Anon import AnonFile`

#### - Declaring API into a Var
`p=AnonFile()`

#### - Send/Upload 
`p.Send('filename')`

#### - Get Send Response
`p.SendResp`

#### - Sending Info Request
`p.InfoID('id') #must be in string`

#### - Response of Info Request
`p.InfoResp`
