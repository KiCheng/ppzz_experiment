# ppzz_experiment

## 摄像头管理后台
https://iot.krzhibo.com/merchant/

## 小车配置
执行下面的命令启动jupyter notebook服务：
```shell
jupyter notebook --allow-root
```

在自己的电脑中输入服务地址，比如`http://192.168.3.238:8889/`，密码为`mobinets`。

进入`/Rosmaster/Samples`目录的代码文件下，进入例程。

代码中注意将串口信息进行修改：
```python
bot = Rosmaster(com="/dev/ttyUSB1")
```

串口信息默认是 USB0 或 USB1，可以通过`dmesg | grep tty`查找最下方的 ch341 串口信息，在上方代码修改。

