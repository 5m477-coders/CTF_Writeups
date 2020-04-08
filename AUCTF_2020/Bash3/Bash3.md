# Bash: Bash3 writeup

- Access with ssh:
> - `ssh challenges.auctf.com -p 30040 -l level3`
> - pwd: `auctf{g0tt@_muv_fas7}`

- We have another script that we can't run it:
```
level3@5a2276bbe718:~$ ls -alrt
-r-xr-x--- 1 level4 level3  179 Apr  1 21:25 passcodes.sh
-r--r----- 1 level4 level4   30 Apr  1 21:25 flag.txt
```
- Checking sudo rules:
```
level3@5a2276bbe718:~$ sudo -l
Matching Defaults entries for level3 on 5a2276bbe718:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User level3 may run the following commands on 5a2276bbe718:
    (level4) NOPASSWD: /home/level3/passcodes.sh
```

- So we can `sudo -u level4 <script>` again. Looking at the script:
```
level3@5a2276bbe718:~$ cat passcodes.sh
#!/bin/bash

x=$RANDOM
echo "Input the random number."
read input

if [[ "$input" -eq "$x" ]]
then
	echo "AWESOME sauce"
	cat flag.txt
else
	echo "$input"
	echo "$x try again"
fi
```

- So there's a RANDOM number we need to guess in order to get the flag output. We can brute force this easily, by just hardcoded a number within the $RANDOM function’s range, and then running until we happen to match:
```
while true; do sudo -u level4 /home/level3/passcodes.sh < /tmp/.lul | grep -A1 AWES && break; done
AWESOME sauce
auctf{wut_r_d33z_RaNdom_numz}
```

- Flag: `auctf{wut_r_d33z_RaNdom_numz}`