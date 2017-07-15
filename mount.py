import pandas as pd 

mount = pd.DataFrame(columns = ['Command','NL Queries'])

mount = mount.append({'Command':'mount -t iso9660 -o ro /dev/cdrom /mnt','NL Queries':['Add /dev/cdrom which is of iso9660 file type to /mnt directory with read only access.','Mount /dev/cdrom folder on /mnt folder. It should only have read only priviledge. The /dev/cdrom is of iso9660 type.']},ignore_index=True)
mount = mount.append({'Command':'mount -l -t ext2','NL Queries':['Show all mounted filesystems of type ext2.','List all mounted ext2 filesystems.','How do I check which ext2 type file systems are mounted on.']},ignore_index=True)
mount = mount.append({'Command':'mount -M /mydata /mnt/','NL Queries':['Access /mydata from /mnt/','How do I see content of /mydata on /mnt/?','Move /mydata  to /mnt.']},ignore_index=True)

print mount


