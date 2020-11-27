import dropbox

access_token = "--get access token from ur dropbox--"

dbx = dropbox.Dropbox(access_token)

uploadFile = open("C:/Users/user/Downloads/Annie's VS/Python/sample.txt","rb").read()

dbx.files_upload(uploadFile, "/sample.txt", mode=dropbox.files.WriteMode.overwrite)
