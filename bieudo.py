import matplotlib.pyplot as plt

print("--- THONG KE TY LE NAM NU (BIEU DO COT) ---")
nam = int(input("Nhap so luong sinh vien Nam: "))
nu = int(input("Nhap so luong sinh vien Nu: "))

labels = ['Nam', 'Nu']
sizes = [nam, nu]
colors = ['#3498db', '#e74c3c']

# Vẽ biểu đồ cột
bars = plt.bar(labels, sizes, color=colors, width=0.5)

# Hiển thị con số chính xác trên đỉnh mỗi cột
for bar in bars:
    chieucao = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, chieucao + 0.5, str(int(chieucao)), 
             ha='center', va='bottom', fontweight='bold')

plt.title('So luong sinh vien Nam va Nu')
plt.xlabel('Gioi tinh')
plt.ylabel('So luong')

# Tạo khoảng trống phía trên đỉnh cột để số không bị lẹm và kẻ lưới ngang
plt.ylim(0, max(sizes) + (max(sizes) * 0.2)) 
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('bieudo.png')
print("=> Da luu bieu do cot vao file bieudo.png thanh cong!")
