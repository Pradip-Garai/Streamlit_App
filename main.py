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

# Custom CSS for unique, modern UI
st.markdown("""
<style>
    /* Dark theme with neon accents */
    .stApp {
        background: #0a0e27;
        background-image: radial-gradient(circle at 10% 20%, rgba(255, 107, 107, 0.05) 0%, rgba(0, 0, 0, 0) 50%);
    }
    
    /* Glass morphism container */
    .glass-container {
        background: rgba(15, 25, 45, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 25px 45px rgba(0, 0, 0, 0.3);
    }
    
    /* Neon header */
    .neon-header {
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .neon-header h1 {
        font-size: 3rem;
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 3s ease infinite;
        margin: 0;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .neon-header p {
        color: #8892b0;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Floating upload zone */
    .upload-zone {
        background: rgba(255, 255, 255, 0.03);
        border: 2px dashed rgba(78, 205, 196, 0.5);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        margin-bottom: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }
    
    .upload-zone:hover {
        border-color: #4ECDC4;
        background: rgba(78, 205, 196, 0.05);
        transform: translateY(-5px);
    }
    
    .upload-zone h3 {
        color: #4ECDC4;
        margin-bottom: 0.5rem;
    }
    
    .upload-zone p {
        color: #8892b0;
    }
    
    /* Card design */
    .info-card {
        background: linear-gradient(135deg, rgba(78, 205, 196, 0.1), rgba(69, 183, 209, 0.1));
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 3px solid #4ECDC4;
        transition: transform 0.2s;
    }
    
    .info-card:hover {
        transform: translateX(5px);
    }
    
    /* Custom file uploader */
    .stFileUploader > div > button {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(78, 205, 196, 0.3);
        border-radius: 12px;
        color: white;
        padding: 0.6rem 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4ECDC4;
        box-shadow: 0 0 10px rgba(78, 205, 196, 0.3);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(78, 205, 196, 0.3);
        border-radius: 12px;
        color: white;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #4ECDC4, #45B7D1);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stDownloadButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(78, 205, 196, 0.4);
    }
    
    /* Image preview */
    .stImage {
        border-radius: 15px;
        overflow: hidden;
        border: 2px solid rgba(78, 205, 196, 0.3);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(78, 205, 196, 0.1);
        border-radius: 12px;
        color: #4ECDC4;
        font-weight: bold;
    }
    
    /* Success message */
    .stAlert {
        background: rgba(78, 205, 196, 0.1);
        border-left: 4px solid #4ECDC4;
        border-radius: 12px;
        color: #4ECDC4;
    }
    
    /* Custom divider */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #4ECDC4, #FF6B6B, #4ECDC4, transparent);
        margin: 1.5rem 0;
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        background: rgba(255, 107, 107, 0.2);
        color: #FF6B6B;
        padding: 0.2rem 0.8rem;
        border-radius: 50px;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #8892b0;
        padding: 2rem;
        font-size: 0.9rem;
    }
    
    /* Neon glow effect */
    .neon-glow {
        text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);
    }
    
    /* Animation for preview */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .glass-container {
            padding: 1rem;
        }
        
        .neon-header h1 {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Main container
# st.markdown('<div class="glass-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="neon-header">
    <h1>✨ IMAGE FORGE ✨</h1>
    <p>Transform your images with precision and style</p>
    <span class="badge">⚡ Instant Conversion</span>
</div>
""", unsafe_allow_html=True)

# Function to convert image (unchanged)
def convert_image(uploaded_file, output_ext):
    img = Image.open(uploaded_file)
    
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
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)

if upload_image is not None:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.markdown("### 🎨 Preview")
        st.image(upload_image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📊 Details")
        
        # File size in appropriate unit
        size_kb = upload_image.size / 1024
        if size_kb < 1024:
            size_display = f"{size_kb:.2f} KB"
        else:
            size_display = f"{size_kb/1024:.2f} MB"
        
        st.markdown(f"""
        <div class="info-card">
            <span style="color: #4ECDC4;">📛 NAME</span><br>
            <code style="color: white;">{upload_image.name}</code>
        </div>
        <div class="info-card">
            <span style="color: #4ECDC4;">💾 SIZE</span><br>
            <code style="color: white;">{size_display}</code>
        </div>
        <div class="info-card">
            <span style="color: #4ECDC4;">🔖 TYPE</span><br>
            <code style="color: white;">{upload_image.type}</code>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Get original filename without extension
    base_name = os.path.splitext(upload_image.name)[0]
    
    st.markdown("### ⚙️ Configuration")
    
    colA, colB = st.columns(2)
    
    with colA:
        new_name = st.text_input("Filename", value=base_name, help="Enter the output filename")
    
    with colB:
        output_format = st.selectbox(
            "Format",
            ["png", "jpg", "jpeg"],
            help="Choose the output format"
        )
    
    final_filename = f"{new_name}.{output_format}"
    
    # Convert image
    converted_file, mime_type = convert_image(upload_image, output_format)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 💾 Export")
    
    colBtn1, colBtn2, colBtn3 = st.columns([1, 2, 1])
    with colBtn2:
        st.download_button(
            label="🚀 DOWNLOAD NOW",
            data=converted_file,
            file_name=final_filename,
            mime=mime_type,
            use_container_width=True
        )
    
    st.success(f"✓ Ready for download: `{final_filename}`")
    
    with st.expander("💡 Quick Guide"):
        colTip1, colTip2 = st.columns(2)
        with colTip1:
            st.markdown("""
            **PNG Format**
            - ✓ Transparency support
            - ✓ Lossless compression
            - ✓ Best for graphics
            """)
        with colTip2:
            st.markdown("""
            **JPG Format**
            - ✓ Smaller file size
            - ✓ Best for photos
            - ✓ 95% quality preserved
            """)

else:
    st.markdown("""
    <div class="upload-zone">
        <div style="font-size: 4rem;">🎯</div>
        <h3>Drop Zone Active</h3>
        <p>Click browse or drag & drop your image here</p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">Supported: PNG, JPG, JPEG</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>⚡ Real format conversion • Zero data retention • Instant processing</p>
    <p style="font-size: 0.7rem;">Image Forge v2.0 — Convert with confidence</p>
</div>
""", unsafe_allow_html=True)