import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 APP TÍNH LÃI GỬI TIẾT KIỆM NGÂN HÀNG")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

so_tien_gui = st.number_input(
    "💰 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=500000000.0,
    step=1000000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=3,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=12.0,
    step=0.1
)

hinh_thuc = st.selectbox(
    "💵 Hình thức nhận lãi",
    ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
)

# =========================
# TÍNH TOÁN
# =========================

if st.button("TÍNH TIỀN LÃI", type="primary", use_container_width=True):

    # Đổi lãi suất năm sang lãi suất tháng
    lai_suat_thang = lai_suat / 100 / 12

    # Tổng tiền lãi theo lãi đơn
    tong_tien_lai = so_tien_gui * lai_suat_thang * ky_han

    # Xác định tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
        so_ky_nhan_lai = 1
        ten_ky = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = so_tien_gui * lai_suat_thang
        so_ky_nhan_lai = ky_han
        ten_ky = "mỗi tháng"

    else:  # Hàng quý
        lai_moi_quy = so_tien_gui * lai_suat_thang * 3

        so_quy_day_du = ky_han // 3
        thang_le = ky_han % 3

        # Nếu kỳ hạn không chia hết cho 3
        if thang_le == 0:
            tien_lai_dinh_ky = lai_moi_quy
        else:
            tien_lai_dinh_ky = lai_moi_quy

        so_ky_nhan_lai = so_quy_day_du
        ten_ky = "mỗi quý"

    # Tổng gốc + lãi
    tong_goc_va_lai = so_tien_gui + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.divider()
    st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tiền gửi ban đầu",
            f"{so_tien_gui:,.0f} VNĐ"
        )

        st.metric(
            f"Tiền lãi {ten_ky}",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

        st.metric(
            "Tổng gốc + lãi",
            f"{tong_goc_va_lai:,.0f} VNĐ"
        )

    # =========================
    # THÔNG TIN CHI TIẾT
    # =========================

    st.subheader("📋 Chi tiết khoản tiền gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc == "Cuối kỳ":
        st.info(
            f"Khách hàng nhận toàn bộ tiền lãi "
            f"{tong_tien_lai:,.0f} VNĐ khi kết thúc kỳ hạn."
        )

    elif hinh_thuc == "Hàng tháng":
        st.info(
            f"Mỗi tháng khách hàng nhận {tien_lai_dinh_ky:,.0f} VNĐ tiền lãi. "
            f"Trong {ky_han} tháng, tổng tiền lãi là {tong_tien_lai:,.0f} VNĐ."
        )

    else:
        lai_quy = so_tien_gui * lai_suat_thang * 3
        so_quy = ky_han // 3
        thang_le = ky_han % 3

        st.info(
            f"Mỗi quý đầy đủ khách hàng nhận khoảng "
            f"{lai_quy:,.0f} VNĐ tiền lãi."
        )

        if thang_le > 0:
            lai_thang_le = so_tien_gui * lai_suat_thang * thang_le

            st.write(
                f"Kỳ hạn còn dư **{thang_le} tháng**, "
                f"tiền lãi phần thời gian này là "
                f"**{lai_thang_le:,.0f} VNĐ**."
            )

    # =========================
    # CÔNG THỨC
    # =========================

    with st.expander("📚 Xem công thức tính"):
        st.write("### Công thức")
        st.latex(
            r"\text{Tiền lãi} = C \times \frac{i}{12} \times n"
        )

        st.write("""
        Trong đó:

        - **C**: Số tiền gửi ban đầu
        - **i**: Lãi suất năm
        - **n**: Số tháng gửi
        """)

st.divider()
st.caption("Ứng dụng tính lãi tiền gửi tiết kiệm - Python Streamlit")
