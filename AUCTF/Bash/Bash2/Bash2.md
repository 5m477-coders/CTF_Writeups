# Bash: Bash2 writeup

- Access with ssh:
> - `ssh challenges.auctf.com -p 30040 -l level2`
> - pwd: `auctf{W3lcoM3_2_da_C7F}`

- 1st Check:
```
level2@0eac6d832fac:~$ ls -alrt
-r-xr-x--- 1 level3 level2  110 Apr  1 21:25 random_dirs.sh
-r--r----- 1 level3 level3   22 Apr  1 21:25 flag.txt
level2@0eac6d832fac:~$ id
uid=1001(level2) gid=1001(level2) groups=1001(level2)
level2@0eac6d832fac:~$ cat random_dirs.sh
#!/bin/bash
x=$RANDOM
base64 flag.txt > /tmp/$x
function finish {
	rm  /tmp/$x
}
trap finish EXIT
sleep 15
```

- So `random_dirs.sh` will run generate a random number and encrypt flag file in base64, redirected to that random number as a file under /tmp. It then deletes it after 15 seconds.

- So, if we run the `random_dirs.sh` script as level2, it will just give us `Permission Denied` as we can't access the flag (so we can't base64 it).

- Check allowed commands as sudo for level2 user:
```
level2@0eac6d832fac:~$ sudo -l
Matching Defaults entries for level2 on 0eac6d832fac:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User level2 may run the following commands on 0eac6d832fac:
    (level3) NOPASSWD: /home/level2/random_dirs.sh
```

- So we can use sudo to run the script as level3 without it's password.
```
level2@0eac6d832fac:~$ sudo -u level3 /home/level2/random_dirs.sh
<sits for 15 seconds>
```

- If we access to the random file before deleted:
```
level2@0eac6d832fac:/tmp$ echo YXVjdGZ7ZzB0dEBfbXV2X2Zhczd9Cg== | base64 -d
```

- Flag: `auctf{g0tt@_muv_fas7}`