import streamlit as st
from PIL import Image
import io
import os

# Page config
st.set_page_config(
    page_title="Image Extension Converter",
    page_icon="🖼️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 2rem;
}
.upload-section {
    border: 2px dashed #4CAF50;
    border-radius: 10px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🖼️ Image Extension Converter")
st.markdown("Upload, preview, convert, rename, and download images")
st.markdown("</div>", unsafe_allow_html=True)


# Function to convert image properly
def convert_image(uploaded_file, output_ext):
    img = Image.open(uploaded_file)

    # Handle transparency when converting PNG -> JPG
    if output_ext in ["jpg", "jpeg"]:
        img = img.convert("RGB")

    buffer = io.BytesIO()

    if output_ext == "png":
        img.save(buffer, format="PNG")
        mime = "image/png"

    elif output_ext in ["jpg", "jpeg"]:
        img.save(buffer, format="JPEG", quality=95)
        mime = "image/jpeg"

    buffer.seek(0)
    return buffer, mime


# Upload file
upload_image = st.file_uploader(
    "Choose Your Image",
    type=["png", "jpg", "jpeg"]
)

if upload_image is not None:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📸 Preview")
        st.image(upload_image, use_container_width=True)

    with col2:
        st.markdown("### 📋 File Info")
        st.info(f"**Original Name:** `{upload_image.name}`")
        st.info(f"**File Size:** `{upload_image.size/1024:.2f} KB`")
        st.info(f"**File Type:** `{upload_image.type}`")

    st.markdown("---")

    # Get original filename without extension
    base_name = os.path.splitext(upload_image.name)[0]

    st.markdown("### ✏️ Output Settings")

    new_name = st.text_input("Enter File Name", value=base_name)

    output_format = st.selectbox(
        "Choose Output Format",
        ["png", "jpg", "jpeg"]
    )

    final_filename = f"{new_name}.{output_format}"

    # Convert image
    converted_file, mime_type = convert_image(upload_image, output_format)

    st.markdown("---")
    st.markdown("### ⬇️ Download")

    st.download_button(
        label="📥 Download Converted Image",
        data=converted_file,
        file_name=final_filename,
        mime=mime_type,
        use_container_width=True
    )

    st.success(f"✅ Ready: `{final_filename}`")

    with st.expander("💡 Tips"):
        st.markdown("""
        - PNG supports transparency
        - JPG/JPEG gives smaller size
        - Conversion now changes actual image format (not just filename)
        """)

else:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("### 📤 No Image Selected")
    st.markdown("Upload an image to begin")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Now converts the real image format correctly</p>",
    unsafe_allow_html=True
)