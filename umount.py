import pandas as pd 

umount = pd.DataFrame(columns = ['Command','NL Queries'])

umount = umount.append({'Command':'umount /mnt','NL Queries':['Unmount /mnt from the file system.','Remove /mnt from the file system.','Detach /mnt from the file system.']},ignore_index=True)
umount = umount.append({'Command':'umount -l /mnt','NL Queries':['Detach /mnt from the file system as soon as all processes using it are done.','Remove /mnt from file system once it is done being used by operating system.']},ignore_index=True)

print umount


