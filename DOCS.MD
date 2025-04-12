project/
├── services/
│   ├── airflow/
│   │   ├── deployment.yaml          # Cấu hình Deployment cho Apache Airflow
│   │   ├── service.yaml             # Cấu hình Service để expose Airflow
│   │   ├── ingress.yaml             # Cấu hình Ingress cho Airflow
│   │   └── configmap.yaml           # Cấu hình ConfigMap nếu cần
│   ├── n8n/
│   │   ├── deployment.yaml          # Cấu hình Deployment cho n8n
│   │   ├── service.yaml             # Cấu hình Service để expose n8n
│   │   ├── ingress.yaml             # Cấu hình Ingress cho n8n
│   │   └── configmap.yaml           # Cấu hình ConfigMap nếu cần
│   ├── other-service/
│   │   ├── deployment.yaml          # Cấu hình Deployment cho dịch vụ khác
│   │   ├── service.yaml             # Cấu hình Service để expose dịch vụ khác
│   │   ├── ingress.yaml             # Cấu hình Ingress cho dịch vụ khác
│   │   └── configmap.yaml           # Cấu hình ConfigMap nếu cần
├── ingress/
│   ├── ingress-controller.yaml      # Cấu hình Ingress Controller (NGINX)
├── namespace.yaml                   # Khai báo namespace dùng chung
├── kustomization/
│   ├── base/
│   │   ├── namespace.yaml           # Cấu hình namespace mặc định
│   │   ├── common-resources.yaml    # Tài nguyên chung cho cluster
│   └── overlays/
│       ├── dev/                     # Overlay cho môi trường phát triển
│       └── prod/                    # Overlay cho môi trường sản xuất
├── .github/
│   └── workflows/
│       └── ci-cd.yaml               # GitHub Actions để triển khai tự động
├── README.md                        # Mô tả dự án và hướng dẫn sử dụng
├── LICENSE                          # File giấy phép nếu cần
