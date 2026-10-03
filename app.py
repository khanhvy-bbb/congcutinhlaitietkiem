# Khách hàng gửi 500 triệu trong 3 tháng
# Lãi suất 1%/tháng, lãnh lãi cuối kỳ

C = 500000000   # Số tiền gửi ban đầu
i = 0.01        # Lãi suất 1%/tháng
n = 3           # Thời gian gửi 3 tháng

# Lãi đơn: An = C * (1 + i*n)
An = C * (1 + i*n)

# Lãi kép: Bn = C * (1 + i)**n
Bn = C * (1 + i)**n

print("Số tiền nhận được theo lãi đơn:", An, "đồng")
print("Số tiền nhận được theo lãi kép:", Bn, "đồng")
