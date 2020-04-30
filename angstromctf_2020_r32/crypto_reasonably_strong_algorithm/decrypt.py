from Crypto.Util.number import inverse

n = 126390312099294739294606157407778835887 
e = 65537 
c = 13612260682947644362892911986815626931
p = 9336949138571181619
q = 13536574980062068373

phi = (p-1)*(q-1)

d = inverse(e,phi)

m = pow(c, d, n)
print hex(m)[2:-1].decode('hex')

#online compiler with Crypto Model: https://ideone.com/mq9OYk
#actf{10minutes}