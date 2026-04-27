import streamlit as st

# Page config for better appearance
st.set_page_config(
    page_title="Image Extension Converter",
    page_icon="🖼️",
    layout="centered"
)

# Custom CSS for better styling
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
    .image-preview {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .success-message {
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🖼️ Image Extension Converter")
st.markdown("Upload, preview, rename, and download your images in different formats")
st.markdown('</div>', unsafe_allow_html=True)

upload_image = st.file_uploader(
    "Choose Your Image",
    type=["png", "jpg", "jpeg"],
    help="Supported formats: PNG, JPG, JPEG"
)

if upload_image is not None:
    # Create columns for better layout
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
    
    # File naming section
    st.markdown("### ✏️ Customize Output")
    file_name = st.text_input(
        "Enter Image Name Before Download (.jpg/.png/.jpeg)",
        value=upload_image.name,
        help="Include the extension (e.g., my_image.jpg)"
    )
    
    st.markdown("---")
    
    # Download section
    st.markdown("### ⬇️ Download")
    
    col3, col4, col5 = st.columns([1, 2, 1])
    with col3:
        st.download_button(
            label="📥 Download Image",
            data=upload_image.getvalue(),
            file_name=file_name,
            mime=upload_image.type,
            use_container_width=True
        )
    
    # Success message
    st.success(f"✅ Ready to download: `{file_name}`")
    
    # Tips section
    with st.expander("💡 Tips"):
        st.markdown("""
        - **Change extension** in the filename to convert formats (e.g., `image.jpg` → `image.png`)
        - Supported formats: PNG, JPG, JPEG
        - The download button will use the filename you provide
        """)

else:
    # Empty state with instructions
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown("### 📤 No Image Selected")
    st.markdown("Upload an image using the button above to get started")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Supported formats info
    with st.expander("ℹ️ Supported Formats"):
        st.markdown("""
        - **PNG** (.png)
        - **JPEG** (.jpg, .jpeg)
        """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Upload any image, rename it with any supported extension</p>",
    unsafe_allow_html=True
)