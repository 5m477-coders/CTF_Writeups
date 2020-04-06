# Web: gg no re writeup

- Really nothing... in `http://challenges.auctf.com:30022`

![mt(0)](https://user-images.githubusercontent.com/57829161/78539621-87f99980-77fb-11ea-9cec-19fb9b12bd65.png)


- Try to explore the parent directory of the server by adding the `/api` in the address bar:

![mt(1)](https://user-images.githubusercontent.com/57829161/78539632-8b8d2080-77fb-11ea-8681-552d936dbd16.png)


- Let's check the `final.php`:

![mt(2)](https://user-images.githubusercontent.com/57829161/78539636-8e881100-77fb-11ea-9821-03d43ea16bef.png)


- Do the curl request and get the flag `curl -d "flag"  http://challenges.auctf.com:30022/api/final.php`:

![mt(flag)](https://user-images.githubusercontent.com/57829161/78539641-90ea6b00-77fb-11ea-8b39-09f1ba1c6b42.png)

Flag: auctf{1_w@s_laZ_w1t_dis_0N3}