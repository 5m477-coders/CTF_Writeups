# Bash: Bash4 writeup

- Access SSH ```ssh challenges.auctf.com -p 30040 -l level4```.

- On the Box:
```
level4@5a2276bbe718:~$ ls -alrt
-r-xr-x--- 1 level5 level4  209 Apr  1 21:25 print_file.sh
-r--r----- 1 level5 level5   25 Apr  1 21:25 flag.txt

level4@5a2276bbe718:~$ sudo -l
Matching Defaults entries for level4 on 5a2276bbe718:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User level4 may run the following commands on 5a2276bbe718:
    (level5) NOPASSWD: /home/level4/print_file.sh

level4@5a2276bbe718:~$ sudo -u level5 ./print_file.sh flag.txt
auctf{FunKy_P3rm1ssi0nZ}
```

- Flag: `auctf{FunKy_P3rm1ssi0nZ}`