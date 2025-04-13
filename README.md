# Triển Khai Các Dịch Vụ Lên Kubernetes

## Mô Tả Dự Án

Dự án này cung cấp các cấu hình để triển khai một hệ thống ứng dụng đa dịch vụ hoàn chỉnh trên Kubernetes. Hệ thống này bao gồm:

*   **MySQL:** Cơ sở dữ liệu quan hệ.
*   **phpMyAdmin:** Giao diện web để quản lý cơ sở dữ liệu MySQL.
*   **N8N:** Công cụ tự động hóa quy trình làm việc.
*   **Docker Registry:** Kho chứa Docker riêng tư.

Hệ thống này được thiết kế để dễ dàng triển khai, mở rộng và quản lý, phù hợp cho việc học tập, phát triển và triển khai các ứng dụng thực tế.

## Mục Lục

## Điều Kiện Tiên Quyết

Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt và cấu hình các công cụ sau:

*   **Docker:** Để xây dựng và chạy các container.
*   **kubectl:** Công cụ dòng lệnh để tương tác với Kubernetes.
*   **Minikube/kind/Kubernetes cluster:** Một cụm Kubernetes đang hoạt động (bạn có thể dùng Minikube hoặc kind cho môi trường phát triển, hoặc một cluster trên cloud).
*   **Quyền truy cập DNS:** Bạn cần quyền truy cập vào nhà cung cấp DNS của bạn để cấu hình tên miền.

-   [Mục Tiêu Dự Án](#mục-tiêu-dự-án)
-   [Yêu Cầu Tiên Quyết](#yêu-cầu-tiên-quyết)
-   [Cấu Trúc Thư Mục `k8s_config`](#cấu-trúc-thư-mục-k8s_config)
-   [Các Bước Triển Khai](#các-bước-triển-khai)
    -   [Giai Đoạn 1: Thiết Lập Bộ Nhớ Bền Vững](#giai-đoạn-1-thiết-lập-bộ-nhớ-bền-vững)
    -   [Giai Đoạn 2: Triển Khai Các Dịch Vụ](#giai-đoạn-2-triển-khai-các-dịch-vụ)
## Cấu Trúc Thư Mục `k8s_config`

Thư mục `k8s_config` chứa tất cả các file cấu hình Kubernetes cần thiết. Cấu trúc như sau:
```
k8s_config/
├── ingress/                      # Cấu hình Ingress
│   └── ingress.yaml              # Định nghĩa cách lưu lượng bên ngoài đến các dịch vụ
├── storage/                      # Cấu hình bộ nhớ bền vững
│   ├── mysql-pv.yaml             # PersistentVolume cho MySQL
│   ├── mysql-pvc.yaml            # PersistentVolumeClaim cho MySQL
│   ├── n8n-pv.yaml               # PersistentVolume cho N8N
│   ├── n8n-pvc.yaml              # PersistentVolumeClaim cho N8N
│   ├── postgres-pv.yaml          # PersistentVolume cho Postgres
│   ├── postgres-pvc.yaml         # PersistentVolumeClaim cho Postgres
│   ├── registry-pv.yaml          # PersistentVolume cho Registry
│   └── registry-pvc.yaml         # PersistentVolumeClaim cho Registry
└── services/                     # Cấu hình dịch vụ
    ├── clusterissuer/
    │   └── clusterissuer.yaml    # chứng chỉ cấp
    ├── mysql/                    # Cấu hình MySQL
    │   ├── mysql-configmap.yaml  # Cấu hình cơ sở dữ liệu MySQL
    │   ├── mysql-deployment.yaml # Deployment cho MySQL
    │   └── mysql-service.yaml    # Service để cung cấp quyền truy cập MySQL
    ├── n8n/                      # Cấu hình N8N
    │   ├── n8n-configmap.yaml    # Cấu hình N8N
    │   ├── n8n-deployment.yaml   # Deployment cho N8N
    │   ├── n8n-secrets.yaml      # Dữ liệu nhạy cảm cho N8N
    │   ├── n8n-service.yaml      # Service để cung cấp quyền truy cập N8N
    │   ├── postgres-secrets.yaml # Dữ liệu nhạy cảm cho Postgres
    │   ├── postgres-service.yaml      # Service để cung cấp quyền truy cập Postgres
    │   └── postgres-statefulset.yaml  # Statefulset cho Postgres
    ├── phpmyadmin/               # Cấu hình phpMyAdmin
    │   ├── phpmyadmin-configmap.yaml # ConfigMap cho phpMyAdmin
    │   ├── phpmyadmin-deployment.yaml# Deployment cho phpMyAdmin
    │   └── phpmyadmin-service.yaml   # Service để cung cấp quyền truy cập phpMyAdmin
    └── registry/                 # Cấu hình Registry
        ├── deployment.yaml       # Deployment cho Docker Registry
        └── service.yaml          # Service để cung cấp quyền truy cập Docker Registry
```
## Hướng Dẫn Triển Khai

### Giai Đoạn 1: Thiết Lập Bộ Nhớ Bền Vững

1.  **Persistent Volumes (PVs):**
```
bash
    kubectl apply -f k8s_config/storage/mysql-pv.yaml
    kubectl apply -f k8s_config/storage/postgres-pv.yaml
    kubectl apply -f k8s_config/storage/n8n-pv.yaml
    kubectl apply -f k8s_config/storage/registry-pv.yaml
    
```
2.  **Persistent Volume Claims (PVCs):**
```
bash
    kubectl apply -f k8s_config/storage/mysql-pvc.yaml
    kubectl apply -f k8s_config/storage/postgres-pvc.yaml
    kubectl apply -f k8s_config/storage/n8n-pvc.yaml
    kubectl apply -f k8s_config/storage/registry-pvc.yaml
    
```
### Giai Đoạn 2: Triển Khai Các Dịch Vụ

1.  **MySQL:**
```
bash
    kubectl apply -f k8s_config/services/mysql/mysql-configmap.yaml
    kubectl apply -f k8s_config/services/mysql/mysql-deployment.yaml
    kubectl apply -f k8s_config/services/mysql/mysql-service.yaml
    
```
2.  **Postgres:**
```
bash
    kubectl apply -f k8s_config/services/n8n/postgres-secrets.yaml
    kubectl apply -f k8s_config/services/n8n/postgres-service.yaml
    kubectl apply -f k8s_config/services/n8n/postgres-statefulset.yaml
    
```
3.  **N8N:**
```
bash
    kubectl apply -f k8s_config/services/n8n/n8n-configmap.yaml
    kubectl apply -f k8s_config/services/n8n/n8n-secrets.yaml
    kubectl apply -f k8s_config/services/n8n/n8n-deployment.yaml
    kubectl apply -f k8s_config/services/n8n/n8n-service.yaml
    
```
4.  **phpMyAdmin:**
```
bash
    kubectl apply -f k8s_config/services/phpmyadmin/phpmyadmin-configmap.yaml
    kubectl apply -f k8s_config/services/phpmyadmin/phpmyadmin-deployment.yaml
    kubectl apply -f k8s_config/services/phpmyadmin/phpmyadmin-service.yaml
    
```
5. **Registry:**
```
bash
    kubectl apply -f k8s_config/services/registry/deployment.yaml
    kubectl apply -f k8s_config/services/registry/service.yaml
    
```
6. **Clusterissuer:**
```
bash
     kubectl apply -f k8s_config/services/clusterissuer/clusterissuer.yaml
    
```
### Giai Đoạn 3: Cung Cấp Quyền Truy Cập với Ingress

1.  **Ingress Controller:** Cài đặt Ingress Controller (ví dụ: NGINX Ingress Controller) trên cluster của bạn.
2. **Ingress Resource:**
```
bash
      kubectl apply -f k8s_config/ingress/ingress.yaml
   
```
*   **Quan Trọng:**  Sửa đổi file `ingress.yaml` để định nghĩa các `rules` phù hợp với tên miền và dịch vụ của bạn.

### Giai Đoạn 4: Thiết Lập DNS

1.  **Lấy IP Ingress:**
```
bash
    kubectl get service -n ingress-nginx
    
```
Lấy địa chỉ IP từ cột `EXTERNAL-IP`.
2.  **Bản Ghi DNS:**
    *   Tạo các bản ghi `A` cho các subdomain của bạn (ví dụ: `mysql.devhub.io.vn`, `n8n.devhub.io.vn`, `phpmyadmin.devhub.io.vn`) trỏ đến IP của Ingress Controller.
    * Nếu bạn muốn thêm, chỉ cần tạo thêm bản ghi A trỏ tới ingress controller

## Truy Cập Các Dịch Vụ

Sau khi triển khai thành công, bạn có thể truy cập các dịch vụ bằng các subdomain đã cấu hình:

*   **phpMyAdmin:** `phpmyadmin.devhub.io.vn` (ví dụ)
*   **N8N:** `n8n.devhub.io.vn` (ví dụ)
* **Mysql:** `mysql.devhub.io.vn` (ví dụ)
*   **Lưu ý:** Thay `devhub.io.vn` bằng domain của bạn.

## Kiểm Tra

*   Sử dụng `kubectl get all -n default` để kiểm tra trạng thái của tất cả các tài nguyên.
* Kiểm tra log của các pod để tìm ra vấn đề.

## Hướng Dẫn Thêm

*   **CI/CD:** Xem xét việc thiết lập CI/CD để tự động hóa quá trình triển khai.
*   **Scaling:** Hướng dẫn cách scale các dịch vụ lên xuống.
*   **Monitoring:** Thiết lập giám sát để theo dõi trạng thái các dịch vụ.
*   **Security:** Thực hiện các biện pháp bảo mật để bảo vệ hệ thống.

## Liên Hệ

Nếu bạn có bất kỳ câu hỏi hoặc đề xuất nào, xin vui lòng liên hệ với chúng tôi.