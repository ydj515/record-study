# Linux shared folder
* rocky os 8.9 기준으로 작성
* firewalld를 사용하고있지않는다는 가정하에 작성
* vmware 에서 `scsi controller`를 사용하면 스토리지를 mount와 umount를 계속적으로 해줘야하기에 이와같은 NFS 폴더 세팅을 진행한다.

### Prerequisites
- rocky os 8.9
- nfs-utils
- nfs4-acl-tools
- master pc *1, client pc * n 및 NFS 세팅을 위한 rpm 파일

### rpm download
nfs master pc및 client pc에 필요한 rpm 파일준비
```bash
sudo dnf download --resolve nfs-utils nfs4-acl-tools
```

### rpm install
위에서 다운로드 받은 rpm 파일 설치
```bash
sudo rpm -Uvh *.rpm
```

### 시스템 등록 및 시작
```bash
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
```

### master pc 공유 폴더 설정
1. master pc에서 client pc와 공유될 폴더를 생성
```bash
mkdir /data/shared
cmod 666 /data/shared
```

2. master pc 에서 아래와 같이 파일을 수정
```bash
$ sudo vi /etc/exports

# 아래의 내용을 기입
/data/shared       *(rw,sync,no_root_squash)
```

3. exports 파일을 세팅

```bash
sudo exportfs -arv
```

### client pc 공유 폴더 설정
1. 공유될 폴더 생성
```bash
sudo mkdir /data/shared
```

2. NFS 서버가 제공하는 모든 공유 디렉토리의 목록을 확인
```bash
showmount -e {server ip}
```

3. master pc의 path를 client pc의 경로에 마운트
```bash
sudo mount -t nfs {server ip}:{master_pc_storage_path} {client_storage_path}

# 이 예시에서는 아래와 같다
sudo mount -t nfs {server ip}:/data/shared /data/shared
```

4. 마운트 설정 파일 수정
```bash
sudo vi /etc/fstab

# 아래의 내용을 기입
{server ip}:/data/shared /data/shared nfs defaults 0 0
```

5. 시스템이 재부팅되더라도 마운트를 유지하기 위해 아래의 명령어를 실행
```bash
sudo mount -a
```

6. 마운트가 잘 되었는지 확인

```bash
df -Th | grep shared
```

# 유의사항
master pc와의 connection이 끊긴다면 공유 폴더에 read가 바로 안되기에 이 점 유의하여야 한다.