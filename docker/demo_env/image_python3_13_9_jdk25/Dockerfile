FROM python:3.13.9

# 安装 openssh-server sudo vim locales(语言包)  
RUN apt-get update && apt-get install -y openssh-server sudo locales 

# 创建sshd的目录
# RUN sudo chown root:root /; mkdir /var/run/sshd/
RUN mkdir -p /var/run/sshd 

# 配置时区
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
    echo "Asia/Shanghai" > /etc/timezone  

# 配置中文语言包，否则jenkis调用的时候会出中文乱码
RUN sed -i 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen && \  
    locale-gen && \  
    update-locale LANG=zh_CN.UTF-8 LANGUAGE=zh_CN:zh LC_ALL=zh_CN.UTF-8 


# 配置root账号的访问权限，如果不需要root账户可以不配，建议不配
# RUN (echo nokia123;echo nokia123)|passwd root
# RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# 把自己定义的环境变量拷贝到root环境中
COPY .bashrc /root/.bashrc

# 安装java和node,已经提前下载并解压到了image目录下了
# ARG JAVA_JDK=openlogic-openjdk-jre-8u402-b06-linux-x64
# ARG NODEJS=node-v18.16.0-linux-x64
# COPY $JAVA_JDK /usr/local/$JAVA_JDK
# COPY $NODEJS /usr/local/$NODEJS
# 设置java和node的执行权限，如果不执行可能会提示权限不足的问题
# RUN chmod 777 "/usr/local/$NODEJS/bin/node"
# RUN chmod 777 "/usr/local/$JAVA_JDK/bin/java"

# 添加一个账号：ute
RUN useradd -m -s /bin/bash ute
# 设置ute密码
RUN echo 'ute:nokia123' | chpasswd
# 加到sudo的组里，如果不加，ute执行不了sudo命令
RUN usermod -aG sudo ute
# # 配置sudo -i不用输入密码
RUN echo 'ute   ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# 修改ute账号的home目录的权限，否则ute账号不能写入
# RUN sudo chown -R ute:ute /home/ute

# 切换到ute用户
USER ute
# 拷贝自己定义的环境变量到ute的home目录
COPY .bashrc /home/ute/.bashrc
# RUN sudo chown ute:ute /home/ute/.bashrc
# 配置wget代理，下包不需要代理，这里的proxy都是空
COPY .wgetrc /home/ute/.wgetrc
# RUN sudo chown ute:ute /home/ute/.wgetrc
# 配置git
COPY .gitconfig /home/ute/.gitconfig
# RUN sudo chown ute:ute /home/ute/.gitconfig
# 配置.ssh
# COPY .ssh /home/ute/.ssh
# RUN sudo chown ute:ute /home/ute/.ssh
# COPY .Xauthority /home/ute/.Xauthority

# 拷贝pip库
COPY requirements.txt /home/ute/requirements.txt
# 安装pip库
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install pip-tools --proxy=http://10.144.1.10:8080 && \
    pip install -r /home/ute/requirements.txt --upgrade


# 配置ute账号的权限
RUN sudo chown -R ute:ute /home/ute/.bashrc /home/ute/.gitconfig

# 切换到root账户，开启sshd服务，如果不开启，容器不能保持运行状态
USER root
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]