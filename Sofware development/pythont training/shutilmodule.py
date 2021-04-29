'''We will be doing a quick revision on shell utility (shutil) module'''

import shutil
#i want to create a xztar archive and extract it to C:\Users\chidalu craving\Desktop\py directory
shutil.make_archive('myfile','xztar'); #make an archive of xztar format
shutil.unpack_archive('myfile.tar.xz',format='xztar',extract_dir=r'C:\Users\chidalu craving\Desktop\py'); #unpack the format in a certain dirctory


