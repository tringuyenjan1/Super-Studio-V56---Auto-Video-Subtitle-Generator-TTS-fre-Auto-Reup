import os
import shutil

def clear_folder(folder_path="results"):
    # Kiểm tra xem thư mục có tồn tại hay không
    if not os.path.exists(folder_path):
        print(f"Thư mục '{folder_path}' không tồn tại.")
        return

    # Lặp qua tất cả các mục (file và thư mục con) bên trong thư mục
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Nếu là file hoặc shortcut (symlink), thì xóa file
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # Nếu là thư mục, thì xóa toàn bộ thư mục đó
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Không thể xóa {file_path}. Lý do: {e}")
            
    print(f"Đã dọn sạch toàn bộ dữ liệu trong thư mục '{folder_path}'.")

# Gọi hàm để thực thi (đảm bảo thư mục 'results' nằm cùng cấp với file script này)
clear_folder("results")