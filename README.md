# maildown

Some days I just want to send some goddam emails using markdown and get the work done, this package doesn't do anything but send markdown/plaintext emails, support very little configuration, don't expect too much, if missing feature, add it yourself.

# example

```python
from maildown import MailMan

s = {'server':'smtp.exmail.qq.com','user':'batman@gmail.com', 'password': '123456'}

man = MailMan(s)

man.send_mail(to='timfeirg@qq.com')
```

# features

are very little, supports markdown, attachments, everything may not work as expected.

# install

* clone and `sudo pip2 install ./maildown`.
* requires [pandoc](http://johnmacfarlane.net/pandoc/installing.html)


tested using python 2.7.6, doesn't support python3.
