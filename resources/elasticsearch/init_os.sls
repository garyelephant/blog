# 安装Elasticsearch之前需要先对操作系统做参数调优
# 适用于只安装Elasticsearch的服务器

# tune Max Open File Descriptors to 50k
# Increase RLIMIT_MEMLOCK to prevent failing to lock memory
os_limits:
  cmd.run:
    - name: |
        cp /etc/security/limits.conf /etc/security/limits.conf.bak
        cat /etc/security/limits.conf | grep -v "elasticsearch" > /tmp/system_limits.conf
        echo "elasticsearch      hard    nofile      80000" >> /tmp/system_limits.conf
        echo "elasticsearch      soft    nofile      80000" >> /tmp/system_limits.conf
        echo "elasticsearch soft memlock unlimited" >> /tmp/system_limits.conf
        echo "elasticsearch hard memlock unlimited" >> /tmp/system_limits.conf
        mv /tmp/system_limits.conf /etc/security/limits.conf

# tune vm.swappiness to 1
# configure the maximum map count
os_sysctl:
  cmd.run:
    - name: |
        cp /etc/sysctl.conf /etc/sysctl.conf.bak
        cat /etc/sysctl.conf | grep -v "vm\.swappiness" | grep -v "vm\.max_map_count" > /tmp/system_sysctl.conf
        echo "vm.swappiness = 1" >> /tmp/system_sysctl.conf
        echo "vm.max_map_count=262144" >> /tmp/system_sysctl.conf
        mv /tmp/system_sysctl.conf /etc/sysctl.conf

# take in fact right now
take_in_fact_right_now:
  cmd.run:
    - name: |
        sysctl -w vm.swappiness=1
        sudo swapoff -a
        sudo swapon -a
        sysctl -w vm.max_map_count=262144
